# Changelog - YouTube MP3 Downloader

## Versión 2.1 - Calidad de Audio Premium (2025-12-28)

### 🎵 Mejoras de Calidad

#### 📈 Actualización de Calidad de Audio
- **Bitrate aumentado**: De 192 kbps a **320 kbps** (máxima calidad MP3)
- **Sample Rate configurado**: **44100 Hz** (calidad estándar CD)
- **Resultado**: Audio de calidad profesional, equivalente a CDs de audio

#### 🔧 Cambios Técnicos
- Modificado `preferredquality` en configuración de yt-dlp a '320'
- Agregado parámetro `postprocessor_args` con `-ar 44100` para FFmpeg
- Archivos MP3 resultantes tendrán mayor tamaño pero calidad superior

#### 💡 Beneficios
- 🎧 Mejor experiencia de audio para audiófilos
- 🎼 Preservación de más detalles en la música
- 📀 Calidad equivalente a CDs originales
- ⭐ Ideal para escuchar con equipos de audio de alta gama

---

## Versión 2.0 - Historial de Descargas (2025-12-28)

### ✨ Nuevas Funcionalidades

#### 📋 Cola de Archivos Descargados
- **Nueva sección visual**: Ahora la aplicación muestra dos áreas separadas:
  - **Cola de descargas**: URLs pendientes de descarga
  - **Archivos descargados**: Historial completo de archivos descargados exitosamente

#### 🎨 Características del Historial
- ✅ Muestra el título completo de cada archivo descargado
- 📅 Incluye fecha y hora de cada descarga (timestamp)
- 🔄 Los archivos más recientes aparecen primero
- 🎨 Diseño con fondo verde claro para distinguirlo de la cola de descargas

#### 📂 Acceso Rápido a Archivos
- **Nuevo botón "Abrir Carpeta"**: Accede directamente a la carpeta de descargas con un solo clic
- Abre el explorador de Windows en `C:\Users\Angel J Ragel\Music\New Music`

### 🎨 Mejoras de Interfaz
- Ventana redimensionada de 700x600 a 700x750 pixeles para acomodar el nuevo contenido
- Cola de descargas ajustada a altura 8 (antes 10) para dar espacio al historial
- Historial de descargas con altura 6 líneas
- Nuevo botón verde "📂 Abrir Carpeta" junto a los controles existentes

### 📊 Información Guardada
Para cada descarga exitosa se registra:
- Título completo del video
- URL original
- Fecha y hora exacta de la descarga

### 🎯 Beneficios
1. **Seguimiento completo**: Ya no perderás el rastro de lo que has descargado
2. **Historial permanente**: Los archivos descargados se acumulan en la sesión actual
3. **Acceso rápido**: Botón directo para abrir la carpeta de descargas
4. **Organización visual**: Colores diferenciados para cola pendiente (blanco) vs descargados (verde)

### 🔧 Detalles Técnicos
- Uso de `datetime` para timestamps precisos
- Lista dinámica `self.downloaded_files` para almacenar información
- Método `update_downloaded_display()` para actualizar la visualización
- Método `open_downloads_folder()` usando `subprocess.Popen` con explorer

---

## Versión Anterior - Sistema de Cola

### Funcionalidades Base
- Cola de descargas múltiples
- Procesamiento secuencial automático
- Botones de control (Limpiar, Detener, Salir)
- Descarga exclusiva de audio MP3 a 320kbps y 44100 Hz
- Prevención de descarga de playlists completas
