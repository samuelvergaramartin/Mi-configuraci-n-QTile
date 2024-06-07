from libqtile.lazy import lazy
from libqtile.config import Key
from src.modules.variables.config_extra import mod

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    
    #teclas para lanzar alacritty
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    #teclas para lanzar rofi
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Abrir menu"),

#teclas para lanzar discord
Key([mod], "d", lazy.spawn("discord-canary"), desc="Lanzar Discord"),

#teclas para lanzar Visual Studio Code
Key([mod], "v", lazy.spawn("code"), desc="Lanzar Visual Studio Code"),

#teclas para lanzar NetCat-Browser
Key([mod, "shift"], "n", lazy.spawn("NetCat-Browser"), desc="Lanzar NetCat Browser v0.4 Beta"),
Key([mod], "p", lazy.spawn("brave https://mail.proton.me/u/4/inbox"), desc="Abrir ProtonMail"),

#teclas para el control del volumen
Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="Bajar el volumen un 5%"),
Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="Subir el volumen un 5%"),
Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toogle"), desc="Mutear o desmutear"),

#teclas para el control del brillo de la pantalla
Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%"), desc="Subir el brillo un 10%"),
Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set -10%"), desc="Bajar el brillo un 10%"),

#teclas para realizar captura de pantalla
Key([mod], "s", lazy.spawn("scrot"), desc="Capturas la pantalla completa"),
Key([mod, "shift"], "s", lazy.spawn("flameshot"), desc="Capturar un área de la pantalla"),

#teclas para abrir spotify
Key([mod, "shift"], "m", lazy.spawn("spotube"), desc="Lanzar Spotube"),


    #teclas para ver en directo a Lordzas en Twitch
    #Key([mod], "l", lazy.spawn("brave https://twitch.tv/lordzas0110"), desc="Lanzar directamente el canal de Twitch de Lordzas en Firefox"),
    Key([mod], "l", lazy.spawn("LyriaDCE"), desc="Lanzar LyriaDCE"),
    #teclas para lanzar Youtube en el navegador
    Key([mod], "y", lazy.spawn("brave https://youtube.com"), desc="Lanzar Youtube"),

    #teclas para lanzar Youtube Music
    Key([mod, "shift"], "y", lazy.spawn("brave https://music.youtube.com"), desc="Lanzar Youtube Music"),

    #teclas para lanzar Twitch
    Key([mod], "t", lazy.spawn("brave https://twitch.tv"), desc="Lanzar Twitch"),

    #teclas para lanzar Discord Developer Portal

    Key([mod, "shift"], "d", lazy.spawn("brave https://discord.com/developers/docs/intro"), desc="Lanzar Discord Developer Portal"),

    #teclas para abrir el visor de imágenes
    Key([mod], "i", lazy.spawn("geeqie"), desc="Lanzar el visor de imágenes"),

    #teclas para abrir la configuración bluetooth
    Key([mod], "b", lazy.spawn("blueman-manager"), desc="Abrir la configuración de bluetooth"),

    #teclas para abrir el mezclador de volumen
    #
    Key([mod, "shift"], "v", lazy.spawn("pavucontrol"), desc="Abrir el mezclador de volumen"),

    #teclas para lanzar Battly Launcher
    Key([mod, "shift"], "l", lazy.spawn("Battly-Launcher"), desc="Lanzar Battly Launcher"),

    #teclas para lanzar el kit de programación del instituto
    Key([mod], "p", lazy.spawn("bash /home/sam170703dev/Scripts/'Modulo Programación'/programacionkit.sh"), desc="Lanzar kit de programación"),

    Key([mod], "b", lazy.spawn("brave"), desc="Lanzar el navegador web de brave"),
    #teclas para lanzar Premid
    #Key([mod], "p", lazy.spawn("bash /home/sam170703dev/launchers/premid.sh"), desc="Lanzar Premid"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]
