from libqtile.config import Drag, Click
from libqtile.lazy import lazy
from src.modules.objects.keyboard import windows
from src.modules.objects.mouse_buttons import *

# Drag floating layouts.

mouse = [
    Drag([windows], boton_izquierdo, lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([windows], boton_derecho, lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([windows], boton_rueda, lazy.window.bring_to_front()),
]