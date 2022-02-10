# for Linux terminals!

import os
import time
import psutil
from pypresence import Presence

LaunchCode = "939904925494829086" # paste your client id here
theShell = os.environ['SHELL']

# identifying terminal
if "gnome-terminal" in (i.name() for i in psutil.process_iter()):
    presenceState = "On GNOME-terminal"
    presenceLargeImage = "terminal"
    presenceLargeText = "GNOME-terminal"

elif "konsole" in (i.name() for i in psutil.process_iter()):
    presenceState = "On KDE-Konsole"
    presenceLargeImage = "konsole"
    presenceLargeText = "KDE-Konsole"

#identifying shell
shells = ["ZSH", "Bash", "Tmux", "Fish", "Dash"]
for shell in shells:
    if theShell == f"/usr/bin/{shell.lower()}":
        presenceDetails = f"Using {shell} shell"
        presenceSmallImage = shell.lower()
        presenceSmallText = f"{shell} shell"

timeOfStart = time.time() # shows the elapsed time at the bottom (needs to be started in Slushy.update())

print("started\n")

while True:
    try:
        Slushy = Presence(client_id=LaunchCode)
        Slushy.connect()
        Slushy.update(state=presenceState,
                      details=presenceDetails,
                      start=timeOfStart,
                      large_image=presenceLargeImage,
                      large_text=presenceLargeText,
                      small_image=presenceSmallImage,
                      small_text=presenceSmallText)
        print("Connect success!")
        time.sleep(30)
    except:
        print("Failed to connect\nWaiting...\n")
        time.sleep(5)
        pass