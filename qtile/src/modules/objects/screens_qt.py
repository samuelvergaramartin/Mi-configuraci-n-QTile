from libqtile.config import Screen
from libqtile import bar, widget
from src.modules.variables.colors import *
from src.modules.variables.sizes import *
from src.modules.variables.config_extra import dispositivo_red

screens = [
        Screen(
            top=bar.Bar(
                [
                    widget.Sep(
                        linewidth=0,
                        padding=6,
                        foreground="#00ff74",
                        background=color_separador
                    ),
                    widget.GroupBox(
                        active="#00ffff",
                        highlight_method="line",
                        background=tito_color_barra,#ae00ff
                        margin_x=5,
                        margin_y=5,
                        padding=5,
                        rounded=True,
                        this_current_screen_border="#ff00d4",
                        this_screen_border="#ff8700",
                        block_highlight_text_color="#ff8700",
                        inactive="#0ce53a",
                        disable_drag=True,
                        fontsize=tamano_grupo_areas_trabajo,
                        urgent_alert_method="block",
                        urgent_border="#fffb00"
                    ),
                    widget.Sep(
                        linewidth=0,
                        padding=6,
                        foreground="#00ff74",
                        background=color_separador
                    ),
                    widget.Prompt(),
                    widget.WindowName(
                        background=tito_color_barra,#ff00b6
                        empty_group_string="Entorno de trabajo de Samuel",
                        foreground="#ff8700",#00ff74
                        fontsize=tamano_fuente_area_actividad_actual,
                        padding=10
                    ),
                    widget.Sep(
                        linewidth=0,
                        padding=6,
                        foreground="#00ff74",
                        background=color_separador
                    ),
                    widget.Systray(
                        icon_size=tito_tamano_iconos,#26
                        background=tito_color_barra#00f31a
                    ),
                    #DiscordUnreadCounter(),
                
                    widget.Sep(
                        linewidth=0,
                        padding=6,
                        foreground="#00ff74",
                        background=color_separador
                    ),
                    
                    #comienzo del grupo 1
                    widget.TextBox(
                        text=" ",  
                        #foreground=tito_color_fg,
                        foreground=tito_color_grupo1,
                        background=tito_color_bg,
                        fontsize=tito_tamano_barra + 5,
                        padding=-3
                    ),
                    widget.TextBox(
                        text="  : ",#temperatura
                        foreground=tito_color_fg,
                        background=tito_color_grupo1,
                        fontsize=tamano_iconos
                    ),
                    widget.ThermalSensor(
                        foreground=tito_color_fg,
                        background=tito_color_grupo1,
                        threshold=50,
                        tag_sensor="Composite",
                        fmt='{} '
                    ),
                    widget.TextBox(
                        text=" 󰍛 :",#RAM
                        foreground=tito_color_fg,
                        background=tito_color_grupo1,
                        fontsize=tamano_iconos

                    ),
                    widget.Memory(
                        foreground=tito_color_fg,
                        background=tito_color_grupo1
                    ),
                    #widget.Sep(
                        #linewidth=0,
                    # padding=6,
                    #  foreground="#00ff74",
                    #   background=color_separador
                    #),
                    widget.TextBox(
                        text="",
                        foreground=tito_color_grupo1,
                        background=tito_color_bg,
                        fontsize=tito_tamano_barra,
                        padding=-1

                    ),
                    #fin del grupo 1
                    #comienzo del grupo 2
                    widget.TextBox(
                        text=" ",  
                        #foreground=tito_color_fg,
                        foreground=tito_color_grupo2,
                        background=tito_color_bg,
                        fontsize=tito_tamano_barra + 5,
                        padding=-3
                    ),
                    widget.TextBox(
                        text=" 󰚰 : ", #Updates
                        foreground=tito_color_fg,
                        background=tito_color_grupo2,
                        fontsize=tamano_iconos
                    ),
                    widget.CheckUpdates(
                        background=tito_color_grupo2,
                        color_have_updates=tito_color_actualizaciones,
                        color_no_updates=tito_color_fg,
                        no_update_string='0',
                        display_format='{updates}',
                        update_interval=1800,
                        distro='Arch_checkupdates'
                    ),
                    widget.TextBox(
                        text=" 󱄙 :",
                        foreground=tito_color_fg,
                        background=tito_color_grupo2,
                        fontsize=15
                    ),
                    widget.Net(
                        foreground=tito_color_fg,
                        background=tito_color_grupo2,
                        format='  : {down}  : {up}',
                        interface=dispositivo_red,
                        use_bits='true'
                    ),
                    #widget.Sep(
                        #linewidth=0,
                    # padding=6,
                    #  foreground="#00ff74",
                    #   background=color_separador
                    #),
                    widget.TextBox(
                        text="",
                        foreground=tito_color_grupo2,
                        background=tito_color_bg,
                        fontsize=tito_tamano_barra,
                        padding=-1

                    ),
                    #fin del grupo 2

                    #comienzo del grupo 3
                    #widget.Clock(format="%d/%m/%Y %A %h:%mm tt"),
                    widget.TextBox(
                        text=" ",  
                        #foreground=tito_color_fg,
                        foreground=tito_color_grupo3,
                        background=tito_color_bg,
                        fontsize=tito_tamano_barra + 5,
                        padding=-3
                    ),
                    widget.Clock(
                        background=tito_color_grupo3,
                        foreground=tito_color_fg,
                        format="%A %d/%m/%Y %I:%M:%S %p"
                    
                    ),
                    widget.TextBox(
                        text="  : ",
                        background=tito_color_grupo3,
                        foreground=tito_color_fg,
                        fontsize=15
                    ),
                    #widget.PulseVolume(
                    #   foreground=tito_color_fg,
                    #   background=tito_color_grupo3,
                    #   limit_max_volume=True,
                    #   fontsize=tito_tamano_fuente
                    #),
                    widget.Volume(
                        foreground=tito_color_fg,
                        background=tito_color_grupo3,
                        max_chars=3,
                        font='sans',
                        #device='default',
                        #channel='Master',
                        volume_app='pavucontrol',
                        #update_interval=0.2
                        check_mute_string='[off]'
                    ),
                    #widget.Sep(
                        #linewidth=0,
                    # padding=6,
                    #  foreground="#00ff74",
                    #   background=color_separador
                    #),
                    widget.TextBox(
                        text="",
                        foreground=tito_color_grupo3,
                        background=tito_color_bg,
                        fontsize=tito_tamano_barra,
                        padding=-1

                    ),
                    #fin  del grupo 3
                    #widget.QuickExit(), #Antiguo botón "Shutdown"

                    #inicio del grupo 4
                    widget.TextBox(
                        text=" ",  
                        #foreground=tito_color_fg,
                        foreground=color_barra,
                        background=tito_color_bg,
                        fontsize=tito_tamano_barra + 5,
                        padding=-3
                    ),
                    widget.CurrentLayoutIcon(
                        #background=tito_color_grupo4,
                        scale=0.7
                    ),
                    widget.CurrentLayout(
                        #background=tito_color_grupo4
                    ),
                    widget.TextBox(
                        text="",
                        foreground=color_barra,
                        background=tito_color_bg,
                        fontsize=tito_tamano_barra,
                        padding=-1

                    ),
                    #widget.Sep(
                        #linewidth=0,
                    # padding=6,
                    #  foreground="#00ff74",
                    #   background=color_separador
                    #),
                    #fin del grupo 4
                    
                ],
                tamano_barra,
                background=color_barra,
                # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            ),
        ),
    ]