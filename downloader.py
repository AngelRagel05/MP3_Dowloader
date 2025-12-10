import tkinter as tk
from tkinter import messagebox, scrolledtext
import yt_dlp
import imageio_ffmpeg as ffmpeg
import os
import threading
from pathlib import Path
from queue import Queue


class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube MP3 Downloader - Cola de Descargas")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        
        # Configurar colores y estilo
        self.root.configure(bg="#f0f0f0")
        
        # Variables para controlar la descarga
        self.is_downloading = False
        self.download_cancelled = False
        self.download_queue = Queue()
        self.queue_list = []
        self.processing_queue = False
        
        # Contenedor principal con padding
        main_frame = tk.Frame(root, bg="#f0f0f0")
        main_frame.pack(expand=True, fill="both", padx=30, pady=30)
        
        # Título/Instrucción
        title_label = tk.Label(
            main_frame,
            text="YouTube MP3 Downloader",
            font=("Segoe UI", 20, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=(0, 10))
        
        # Subtítulo
        subtitle_label = tk.Label(
            main_frame,
            text="Añade URLs a la cola - se descargarán automáticamente",
            font=("Segoe UI", 11),
            bg="#f0f0f0",
            fg="#666666"
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Campo de entrada URL
        url_frame = tk.Frame(main_frame, bg="#f0f0f0")
        url_frame.pack(fill="x", pady=(0, 15))
        
        self.url_entry = tk.Entry(
            url_frame,
            font=("Segoe UI", 12),
            relief="solid",
            borderwidth=1
        )
        self.url_entry.pack(side="left", fill="x", expand=True, ipady=8)
        self.url_entry.bind('<Return>', lambda e: self.add_to_queue())
        
        # Botón añadir a cola
        add_button = tk.Button(
            url_frame,
            text="➕ Añadir",
            font=("Segoe UI", 11, "bold"),
            bg="#2196F3",
            fg="white",
            activebackground="#1976D2",
            activeforeground="white",
            cursor="hand2",
            relief="flat",
            command=self.add_to_queue
        )
        add_button.pack(side="left", padx=(10, 0), ipady=8, ipadx=15)
        
        # Etiqueta de cola
        queue_label = tk.Label(
            main_frame,
            text="Cola de descargas:",
            font=("Segoe UI", 12, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        queue_label.pack(anchor="w", pady=(10, 5))
        
        # Lista de cola con scroll
        queue_frame = tk.Frame(main_frame, bg="#ffffff", relief="solid", borderwidth=1)
        queue_frame.pack(fill="both", expand=True, pady=(0, 15))
        
        self.queue_text = scrolledtext.ScrolledText(
            queue_frame,
            font=("Consolas", 10),
            bg="#ffffff",
            fg="#333333",
            relief="flat",
            state="disabled",
            wrap="word",
            height=10
        )
        self.queue_text.pack(fill="both", expand=True, padx=2, pady=2)
        
        # Contenedor para botones de control
        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.pack(pady=(0, 15))
        
        # Botón de limpiar cola
        self.clear_button = tk.Button(
            button_frame,
            text="🗑️ Limpiar Cola",
            font=("Segoe UI", 11, "bold"),
            bg="#9E9E9E",
            fg="white",
            activebackground="#757575",
            activeforeground="white",
            cursor="hand2",
            relief="flat",
            command=self.clear_queue
        )
        self.clear_button.pack(side="left", padx=5, ipady=8, ipadx=15)
        
        # Botón de detener descarga
        self.stop_button = tk.Button(
            button_frame,
            text="⏸️ Detener",
            font=("Segoe UI", 11, "bold"),
            bg="#FF9800",
            fg="white",
            activebackground="#F57C00",
            activeforeground="white",
            cursor="hand2",
            relief="flat",
            command=self.stop_download,
            state="disabled"
        )
        self.stop_button.pack(side="left", padx=5, ipady=8, ipadx=15)
        
        # Etiqueta de estado
        self.status_label = tk.Label(
            main_frame,
            text="⏳ Esperando URLs...",
            font=("Segoe UI", 11),
            bg="#f0f0f0",
            fg="#666666"
        )
        self.status_label.pack(pady=(0, 15))
        
        # Botón de salir
        exit_button = tk.Button(
            main_frame,
            text="❌ Salir",
            font=("Segoe UI", 11, "bold"),
            bg="#F44336",
            fg="white",
            activebackground="#D32F2F",
            activeforeground="white",
            cursor="hand2",
            relief="flat",
            command=self.exit_app
        )
        exit_button.pack(ipady=8, ipadx=30)
        
        # Obtener ruta de FFmpeg
        self.ffmpeg_path = ffmpeg.get_ffmpeg_exe()
        
    def get_downloads_folder(self):
        """Obtiene la carpeta de música personalizada del usuario"""
        download_path = r"C:\Users\Angel J Ragel\Music\New Music"
        # Crear la carpeta si no existe
        os.makedirs(download_path, exist_ok=True)
        return download_path
    
    def update_status(self, message, color="#666666"):
        """Actualiza el mensaje de estado"""
        self.status_label.config(text=message, fg=color)
        self.root.update_idletasks()
    
    def add_to_queue(self):
        """Añade una URL a la cola de descargas"""
        url = self.url_entry.get().strip()
        
        if not url:
            messagebox.showwarning("URL vacía", "Por favor, pega un enlace de YouTube")
            return
        
        if "youtube.com" not in url and "youtu.be" not in url:
            messagebox.showwarning("URL inválida", "Por favor, introduce un enlace válido de YouTube")
            return
        
        # Añadir a la cola
        self.queue_list.append(url)
        self.download_queue.put(url)
        self.url_entry.delete(0, tk.END)
        
        # Actualizar visualización
        self.update_queue_display()
        self.update_status(f"✅ URL añadida | {len(self.queue_list)} en cola", "#4CAF50")
        
        # Si no está procesando, iniciar procesamiento
        if not self.processing_queue:
            self.process_queue()
    
    def update_queue_display(self):
        """Actualiza la visualización de la cola"""
        self.queue_text.config(state="normal")
        self.queue_text.delete(1.0, tk.END)
        
        if not self.queue_list:
            self.queue_text.insert(tk.END, "No hay URLs en la cola.\n\n")
            self.queue_text.insert(tk.END, "Añade enlaces de YouTube usando el campo de arriba.")
        else:
            for i, url in enumerate(self.queue_list, 1):
                status = "⏳ Descargando..." if i == 1 and self.is_downloading else "⏱️ En espera"
                self.queue_text.insert(tk.END, f"{i}. {status}\n")
                self.queue_text.insert(tk.END, f"   {url}\n\n")
        
        self.queue_text.config(state="disabled")
        self.queue_text.see(1.0)  # Scroll al inicio
    
    def clear_queue(self):
        """Limpia la cola de descargas"""
        if self.is_downloading:
            result = messagebox.askyesno(
                "Descarga en curso",
                "Hay una descarga en curso. ¿Deseas detenerla y limpiar la cola?"
            )
            if not result:
                return
            self.download_cancelled = True
        
        # Limpiar cola
        while not self.download_queue.empty():
            try:
                self.download_queue.get_nowait()
            except:
                break
        
        self.queue_list.clear()
        self.update_queue_display()
        self.update_status("🗑️ Cola limpiada", "#9E9E9E")
    
    def process_queue(self):
        """Procesa la cola de descargas una por una"""
        if self.processing_queue:
            return
        
        self.processing_queue = True
        
        # Crear hilo para procesar la cola
        queue_thread = threading.Thread(target=self._queue_worker)
        queue_thread.daemon = True
        queue_thread.start()
    
    def _queue_worker(self):
        """Worker que procesa la cola en segundo plano"""
        while not self.download_queue.empty() and not self.download_cancelled:
            try:
                url = self.download_queue.get()
                self.download_audio(url)
                
                # Remover de la lista visual
                if self.queue_list and self.queue_list[0] == url:
                    self.queue_list.pop(0)
                    self.update_queue_display()
                
            except Exception as e:
                print(f"Error procesando cola: {e}")
        
        self.processing_queue = False
        
        if not self.download_cancelled and self.download_queue.empty():
            self.update_status("✅ Todas las descargas completadas", "#4CAF50")

    
    def download_audio(self, url):
        """Descarga el audio de YouTube y lo convierte a MP3"""
        try:
            # Resetear flag de cancelación
            self.download_cancelled = False
            self.is_downloading = True
            
            # Actualizar estado y botones
            self.update_status("⏬ Descargando...", "#FF9800")
            self.stop_button.config(state="normal")
            self.update_queue_display()  # Actualizar para mostrar "Descargando..."
            
            # Configuración de yt-dlp
            downloads_path = self.get_downloads_folder()
            
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),
                'ffmpeg_location': self.ffmpeg_path,
                'quiet': False,
                'no_warnings': False,
                'noplaylist': True,  # Descargar solo el video, no la lista completa
            }
            
            # Descargar
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # Verificar si se canceló antes de descargar
                if self.download_cancelled:
                    self.update_status("⏸️ Descarga cancelada", "#FF9800")
                    return
                    
                info = ydl.extract_info(url, download=True)
                
                # Verificar si se canceló durante la descarga
                if self.download_cancelled:
                    self.update_status("⏸️ Descarga cancelada", "#FF9800")
                    return
                
                video_title = info.get('title', 'video')
            
            # Éxito
            remaining = len(self.queue_list) - 1
            if remaining > 0:
                self.update_status(f"✅ '{video_title[:30]}...' completado | {remaining} restantes", "#4CAF50")
            else:
                self.update_status(f"✅ '{video_title[:30]}...' guardado en Music\\New Music", "#4CAF50")
            
        except Exception as e:
            # Error
            if not self.download_cancelled:
                self.update_status(f"❌ Error al descargar", "#F44336")
                # No mostrar messagebox para no interrumpir la cola
                print(f"Error: {str(e)}")
        
        finally:
            # Reactivar botón y limpiar
            self.is_downloading = False
            if self.download_queue.empty():
                self.stop_button.config(state="disabled")
    
    
    def stop_download(self):
        """Detiene la descarga en curso y limpia la cola"""
        if self.is_downloading or self.processing_queue:
            result = messagebox.askyesno(
                "Detener descargas",
                "¿Deseas detener la descarga actual y cancelar las restantes?"
            )
            if not result:
                return
            
            self.download_cancelled = True
            self.processing_queue = False
            
            # Limpiar cola
            while not self.download_queue.empty():
                try:
                    self.download_queue.get_nowait()
                except:
                    break
            
            self.queue_list.clear()
            self.update_queue_display()
            self.update_status("⏸️ Descargas detenidas", "#FF9800")
            self.stop_button.config(state="disabled")
    
    def exit_app(self):
        """Cierra la aplicación"""
        if self.is_downloading or not self.download_queue.empty():
            result = messagebox.askyesno(
                "Salir",
                "Hay descargas pendientes. ¿Deseas salir de todos modos?"
            )
            if not result:
                return
        
        self.root.destroy()




def main():
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()


if __name__ == "__main__":
    main()
