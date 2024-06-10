from libqtile.config import Group,Key
from libqtile.lazy import lazy
from src.modules.objects.keyboard import windows, shift
from src.modules.objects.shortcuts import keys

groups = [Group(i) for i in [
    "󰙯","","󰈹","","","","󰝰", ""
]]

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