from libqtile import hook, qtile
import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/src/start/autostart.sh'])

    # Ruta al archivo AppImage
    appimage_path = "/home/sam170703dev/Aplicaciones/NetCat-Browser/NetCat-Browser-0.0.3.AppImage"

    # Regla para ejecutar el AppImage
    start_appimage_rule = dict(
        wm_class="netcat-browser",
        command=appimage_path,
        screen=0
    )

    # Añade la regla
    if start_appimage_rule not in qtile.config.rules:
        qtile.config.rules.append(start_appimage_rule)
def start_dunst():
    # Inicia dunst al arrancar QTile
    qtile.cmd_spawn('dunst')
