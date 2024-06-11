from libqtile.config import Key
from libqtile.lazy import lazy
from src.modules.objects.work_areas import groups
from src.modules.objects.layouts_config import layouts
from src.modules.dictionaries.widgets_dictionary import widget_defaults
from src.modules.variables.config_extra import extension_defaults
from src.modules.objects.shortcuts import keys
from src.modules.objects.screens_qt import screens
from src.modules.objects.mouse_config import mouse
from src.modules.objects.float_rules_config import float_rules

from src.modules.variables.config_extra import *
from src.modules.objects.keyboard import windows, shift

def netcat_builder():
    for i, group in enumerate(groups):
        numeroEscritorio =str(i+1)
        keys.extend(
            [
                Key(
                    [windows],
                    numeroEscritorio,
                    lazy.group[group.name].toscreen(),
                    desc="Switch to group {}".format(group.name),
                ),
                Key([windows, shift], numeroEscritorio, lazy.window.togroup(group.name, switch_group=False),
                     desc="move focused window to group {}".format(group.name)),
            ]
        )