@echo off
echo ================================================
echo     YouTube MP3 Downloader - Crear Ejecutable
echo ================================================
echo.

echo Instalando PyInstaller...
pip install pyinstaller
echo.

echo Creando ejecutable...
echo Esto puede tomar unos minutos...
echo.

pyinstaller --onefile --windowed --name "YouTube MP3 Downloader" --icon=NONE downloader.py

echo.
echo ================================================
echo.

if exist "dist\YouTube MP3 Downloader.exe" (
    echo ✅ Ejecutable creado exitosamente!
    echo.
    echo 📁 Ubicacion: dist\YouTube MP3 Downloader.exe
    echo.
    echo 📌 Proximos pasos:
    echo    1. Ve a la carpeta 'dist'
    echo    2. Haz clic derecho en 'YouTube MP3 Downloader.exe'
    echo    3. Selecciona 'Crear acceso directo'
    echo    4. Mueve el acceso directo a tu Escritorio
    echo    5. Haz clic derecho y selecciona 'Anclar a la barra de tareas'
    echo.
) else (
    echo ❌ Error al crear el ejecutable
    echo.
)

pause
