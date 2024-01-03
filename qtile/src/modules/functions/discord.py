import subprocess
from libqtile import widget
# Agrega este bloque donde configuras tus widgets
class DiscordUnreadCounter(widget.TextBox):
    def __init__(self, **config):
        super().__init__("", **config)
        self.update()

    def update(self):
        unread_messages = int(subprocess.check_output(["python", "/home/sam170703dev/Scripts/Discord/Discord-Counter.py"]).decode())
        #self.text = f"Discord: {unread_messages} mensajes sin leer"
        #contador += 1
        #self.text = f"Test {contador1}"
        #time.sleep(1)