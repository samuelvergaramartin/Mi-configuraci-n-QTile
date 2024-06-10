from libqtile.lazy import lazy
from libqtile.config import Key
from src.modules.objects.keyboard import *
from src.modules.variables.config_extra import navegador_web_por_defecto, usuario

keys = [

    # _________________________BASE_________________________

    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html


    # Switch between windows

    Key([windows], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([windows], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([windows], "j", lazy.layout.down(), desc="Move focus down"),
    Key([windows], "k", lazy.layout.up(), desc="Move focus up"),
    Key([windows], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.

    Key([windows, shift], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([windows, shift], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([windows, shift], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([windows, shift], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.

    Key([windows, control], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([windows, control], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([windows, control], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([windows, control], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([windows], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes

    Key([windows, shift], intro, lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # Toggle between different layouts as defined below

    Key([windows], tab, lazy.next_layout(), desc="Toggle between layouts"),
    Key([windows], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([windows, control], "r", lazy.reload_config(), desc="Reload the config"),
    Key([windows, control], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    #_________________________Aplicaciones_________________________

    #teclas para lanzar alacritty
    Key([windows], intro, lazy.spawn("alacritty"), desc="Lanzar Alacritty terminal"),

    #teclas para lanzar rofi
    Key([windows], "m", lazy.spawn("rofi -show drun"), desc="Abrir menu"),

    #teclas para lanzar discord
    Key([windows], "d", lazy.spawn("discord-canary"), desc="Lanzar Discord"),

    #teclas para lanzar Visual Studio Code
    Key([windows], "v", lazy.spawn("code"), desc="Lanzar Visual Studio Code"),

    #teclas para lanzar NetCat-Browser
    Key([windows, shift], "n", lazy.spawn("NetCat-Browser"), desc="Lanzar NetCat Browser v0.4 Beta"),

    #teclas para abrir Spotube
    Key([windows, shift], "m", lazy.spawn("spotube"), desc="Lanzar Spotube"),

    #teclas para lanzar LyriaDCE
    Key([windows], "l", lazy.spawn("LyriaDCE"), desc="Lanzar LyriaDCE"),

    #teclas para abrir el visor de imágenes
    Key([windows], "i", lazy.spawn("geeqie"), desc="Lanzar el visor de imágenes"),

    #teclas para abrir la configuración bluetooth
    Key([windows, shift], "b", lazy.spawn("blueman-manager"), desc="Abrir la configuración de bluetooth"),

    #teclas para abrir el mezclador de volumen
    Key([windows, shift], "v", lazy.spawn("pavucontrol"), desc="Abrir el mezclador de volumen"),

    #Teclas para abrir el navegador web Brave
    Key([windows], "b", lazy.spawn("brave"), desc="Lanzar el navegador web de brave"),
    
    #_________________________Páginas Web_________________________
    
    #teclas para lanzar Youtube en el navegador
    Key([windows], "y", lazy.spawn(navegador_web_por_defecto + "https://youtube.com"),
        desc="Lanzar Youtube"
    ),

    #teclas para lanzar Youtube Music
    Key([windows, shift], "y", lazy.spawn(navegador_web_por_defecto + "https://music.youtube.com"),
        desc="Lanzar Youtube Music"
    ),

    #teclas para lanzar Twitch
    Key([windows], "t", lazy.spawn(navegador_web_por_defecto + "https://twitch.tv"),
        desc="Lanzar Twitch"
    ),

    #teclas para lanzar Discord Developer Portal

    Key([windows, shift], "d", lazy.spawn(navegador_web_por_defecto +"https://discord.com/developers/docs/intro"),
        desc="Lanzar Discord Developer Portal"
    ),

    #_________________________Funciones Especiales_________________________

    #teclas para el control del volumen
    
    Key([], disminuir_volumen, lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
        desc="Bajar el volumen un 5%"
    ),
    Key([], aumentar_volumen, lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
        desc="Subir el volumen un 5%"
    ),
    Key([], mute, lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
        desc="Mutear o desmutear"
    ),

    #teclas para el control del brillo de la pantalla

    Key([], aumentar_brillo, lazy.spawn("brightnessctl s +10"),
        desc="Subir el brillo un 10%"
    ),
    Key([], disminuir_brillo, lazy.spawn("brightnessctl s 10-"),
        desc="Bajar el brillo un 10%"
    ),

    #teclas para realizar captura de pantalla

    Key([windows], "s", lazy.spawn("scrot"), desc="Capturas la pantalla completa"),
    Key([windows, shift], "s", lazy.spawn("flameshot"), desc="Capturar un área de la pantalla"),

    #_________________________Scripts Personalizados_________________________

    #teclas para lanzar el kit de programación del instituto

    Key([windows], "p", lazy.spawn("bash /home/" + usuario + "/Scripts/'Modulo Programación'/programacionkit.sh"),
        desc="Lanzar kit de programación"
    ),

    # Teclas para realizar una backup de NetCatQTile

    Key([alt], "b", lazy.spawn("bash /home/" + usuario + "/.config/qtile/src/modules/functions/create_backup.netcatqt"),
        desc="Crear backup de NetCatQTile"
    ),
]
