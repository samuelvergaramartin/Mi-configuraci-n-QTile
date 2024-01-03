from src.build.netcat_qt_builder import *
from src.modules.hooks.hook_loader import hook, autostart, start_dunst

def netcat_qtile():
    netcat_builder()

@hook.subscribe.startup_once
def autostart_fnc():
    autostart()
def start_dunst_fnc():
    start_dunst()