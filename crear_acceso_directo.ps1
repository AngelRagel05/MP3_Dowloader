# Script para crear acceso directo del YouTube MP3 Downloader

$SourceFileLocation = "$PSScriptRoot\launch.bat"
$ShortcutLocation = "$HOME\Desktop\YouTube MP3 Downloader.lnk"

# Crear objeto de acceso directo
$WScriptShell = New-Object -ComObject WScript.Shell
$Shortcut = $WScriptShell.CreateShortcut($ShortcutLocation)

# Configurar propiedades del acceso directo
$Shortcut.TargetPath = $SourceFileLocation
$Shortcut.WorkingDirectory = $PSScriptRoot
$Shortcut.WindowStyle = 0  # Ventana minimizada (oculta la consola)
$Shortcut.Description = "YouTube MP3 Downloader con Cola de Descargas"

# Usar icono de Python si está disponible, sino usar icono predeterminado
$PythonPath = (Get-Command python -ErrorAction SilentlyContinue).Source
if ($PythonPath) {
    $Shortcut.IconLocation = "$PythonPath,0"
} else {
    # Usar icono de carpeta de música como alternativa
    $Shortcut.IconLocation = "%SystemRoot%\System32\SHELL32.dll,108"
}

# Guardar el acceso directo
$Shortcut.Save()

Write-Host ""
Write-Host "✅ Acceso directo creado exitosamente en:" -ForegroundColor Green
Write-Host "   $ShortcutLocation" -ForegroundColor Cyan
Write-Host ""
Write-Host "📌 Para anclar a la barra de tareas:" -ForegroundColor Yellow
Write-Host "   1. Ve a tu Escritorio" -ForegroundColor White
Write-Host "   2. Haz clic derecho en 'YouTube MP3 Downloader'" -ForegroundColor White
Write-Host "   3. Selecciona 'Anclar a la barra de tareas'" -ForegroundColor White
Write-Host ""
