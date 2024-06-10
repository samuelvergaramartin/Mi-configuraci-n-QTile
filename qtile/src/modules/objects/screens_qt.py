from libqtile.config import Screen
from libqtile import bar, widget
from src.modules.variables.colors import *
from src.modules.variables.sizes import *
from src.modules.variables.config_extra import adaptador_de_red
from src.modules.themes.dark_grey import *
from src.modules.variables.fonts import fuente_predeterminada

#Definicion de funciones

def base(fg=text,bg=dark):
    return {
        'foreground': fg,
        'background': bg
    }

def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)

def icon(fg=text, bg=dark, fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )

def powerline(fg=light, bg=dark):
    return widget.TextBox(
        **base(fg, bg),
        text="\uE0B2", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg=light),
            font=fuente_predeterminada,
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=active,
            inactive=inactive,
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=urgent,
            this_current_screen_border=focus,
            this_screen_border=grey,
            other_current_screen_border=dark,
            other_screen_border=dark,
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg=red_light), fontsize=14, padding=5),
        separator(),
    ]

screens = [
    Screen(
        top=bar.Bar(
            widgets=[
                *workspaces(),
                separator(),
                powerline(yellow_light,dark),
                icon(fg=grey,bg=yellow_light, text=''), # Icon: nf-fa-download
                widget.CheckUpdates(
                    background=yellow_light,
                    colour_have_updates=red_light,
                    colour_no_updates=grey,
                    no_update_string='0',
                    display_format='{updates}',
                    update_interval=1800,
                    custom_command='checkupdates',
                ),
                powerline(orange_light,yellow_light),
                icon(fg=grey,bg=orange_light, text=' '),  # Icon: nf-fa-feed
                widget.Net(**base(fg=grey,bg=orange_light), interface=adaptador_de_red),
                powerline(red_light, orange_light),
                widget.CurrentLayoutIcon(**base(fg=grey,bg=red_light), scale=0.65),
                widget.CurrentLayout(**base(fg=grey,bg=red_light), padding=5),
                powerline(purple, red_light),
                icon(fg=grey,bg=purple, fontsize=17, text='󰃰 '), # Icon: nf-mdi-calendar_clock
                widget.Clock(**base(fg=grey,bg=purple), format='%d/%m/%Y - %I:%M:%S %p '),
                powerline(inactive, purple),
                widget.Systray(background=inactive, padding=5),
            ],
            size=tamano_barra,
            background=dark,
        ),
    ),
]
