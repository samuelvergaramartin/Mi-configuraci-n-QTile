from libqtile.utils import guess_terminal
from libqtile import layout
from src.modules.dictionaries.widgets_dictionary import widget_defaults
from src.modules.objects.float_rules_config import float_rules

dispositivo_red="wlo1"
mod = "mod4"
terminal = guess_terminal()

extension_defaults = widget_defaults.copy()
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wmname = "LG3D"