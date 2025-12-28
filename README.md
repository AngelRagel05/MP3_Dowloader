# YouTube to MP3 Downloader - Cola de Descargas

Aplicación de escritorio con sistema de cola para descargar múltiples audios de YouTube en formato MP3.

## Características

✅ **Sistema de cola de descargas** - Añade múltiples URLs y se descargarán automáticamente  
✅ **Historial de archivos descargados** - Ve todos los archivos que has descargado con fecha y hora  
✅ **Acceso rápido a carpeta** - Botón para abrir directamente la carpeta de descargas  
✅ **Máxima calidad de audio** - Descarga en MP3 a 320 kbps y 44100 Hz (calidad CD)  
✅ Interfaz intuitiva y moderna  
✅ Descarga directa a tu carpeta de música personalizada  
✅ No requiere instalación manual de FFmpeg  
✅ Totalmente en español  
✅ Control completo de descargas (detener, limpiar cola)  
✅ Visualización en tiempo real del estado de la cola  
✅ Procesamiento automático uno por uno  
✅ Ignora listas de reproducción (solo descarga el video específico)

## Requisitos

- Python 3.7 o superior

## Instalación

1. **Instala las dependencias:**

```bash
pip install -r requirements.txt
```

O manualmente:

```bash
pip install yt-dlp imageio-ffmpeg
```

## Uso

1. **Ejecuta la aplicación:**

```bash
python downloader.py
```

2. **Cómo usar la cola de descargas:**
   - Pega un enlace de YouTube en el campo de entrada
   - Presiona **Enter** o haz clic en "➕ Añadir" para añadirlo a la cola
   - Repite para añadir todos los enlaces que desees
   - La aplicación comenzará a descargar automáticamente uno por uno
   - Puedes seguir añadiendo URLs mientras se están descargando otras
   - Los archivos MP3 se guardarán en `C:\Users\Angel J Ragel\Music\New Music`

3. **Controles disponibles:**
   - **➕ Añadir**: Añade la URL actual a la cola
   - **🗑️ Limpiar Cola**: Vacía la cola de descargas pendientes
   - **📂 Abrir Carpeta**: Abre la carpeta de descargas en el explorador de Windows
   - **⏸️ Detener**: Detiene la descarga actual y cancela las pendientes
   - **❌ Salir**: Cierra la aplicación (pregunta si hay descargas pendientes)

4. **Historial de descargas:**
   - La aplicación muestra automáticamente todos los archivos descargados
   - Cada archivo incluye su nombre completo y fecha/hora de descarga
   - Los archivos más recientes aparecen primero en la lista

## Crear Acceso Directo y Anclar a la Barra de Tareas

### Opción 1: Acceso Directo Rápido (Ya Creado) ✅

Ya se ha creado automáticamente un acceso directo en tu escritorio llamado **"YouTube MP3 Downloader"**.

**Para anclarlo a la barra de tareas:**
1. Ve a tu **Escritorio**
2. Busca el acceso directo **"YouTube MP3 Downloader"**
3. Haz **clic derecho** sobre él
4. Selecciona **"Anclar a la barra de tareas"**

¡Listo! Ahora puedes iniciar la aplicación desde tu barra de tareas.

### Opción 2: Crear Ejecutable Profesional (Recomendado)

Si quieres un archivo `.exe` independiente que no requiera Python:

1. **Ejecuta el script de creación:**
   ```bash
   crear_ejecutable.bat
   ```

2. **Espera** a que se complete (puede tomar unos minutos)

3. **Encuentra el ejecutable** en la carpeta `dist/YouTube MP3 Downloader.exe`

4. **Crea un acceso directo:**
   - Haz clic derecho en el `.exe`
   - Selecciona "Crear acceso directo"
   - Mueve el acceso directo a tu Escritorio o anclalo directo a la barra de tareas

## Estructura del Proyecto

```
MP3_Download/
├── downloader.py                  # Aplicación principal
├── requirements.txt               # Dependencias Python
├── requirements_dev.txt           # Dependencias de desarrollo (PyInstaller)
├── launch.bat                     # Script de lanzamiento sin consola
├── crear_acceso_directo.ps1      # Script para crear acceso directo
├── crear_ejecutable.bat          # Script para crear .exe
└── README.md                     # Este archivo
```

## Solución de Problemas

### Error: "No module named 'yt_dlp'"
Asegúrate de haber instalado las dependencias:
```bash
pip install -r requirements.txt
```

### La descarga falla
- Verifica que el enlace sea válido de YouTube
- Comprueba tu conexión a internet
- Algunos videos pueden tener restricciones de descarga

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación
- **tkinter**: Interfaz gráfica
- **yt-dlp**: Descarga de videos/audio de YouTube
- **imageio-ffmpeg**: Conversión de audio a MP3 (sin instalación manual)
