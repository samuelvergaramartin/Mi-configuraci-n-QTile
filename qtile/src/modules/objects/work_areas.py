from libqtile.config import Group,Key
from libqtile.lazy import lazy
from src.modules.variables.config_extra import mod
from src.modules.objects.shortcuts import keys

groups = [Group(i) for i in [
    "󰙯","","󰈹","","","","󰝰", ""
]]

for i, group in enumerate(groups):
        numeroEscritorio =str(i+1)
        keys.extend(
            [
                Key(
                    [mod],
                    numeroEscritorio,
                    lazy.group[group.name].toscreen(),
                    desc="Switch to group {}".format(group.name),
                ),
                Key([mod, "shift"], numeroEscritorio, lazy.window.togroup(group.name, switch_group=False),
                     desc="move focused window to group {}".format(group.name)),
            ]
        )