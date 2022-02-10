# for Linux terminals!

import os
import time
import psutil
from pypresence import Presence

LaunchCode = "939904925494829086" # paste your client id here
theShell = os.environ['SHELL']

# identify terminal and get terminal data
def getData():
    if "gnome-terminal" in (i.name() for i in psutil.process_iter()):
        state = "On GNOME-terminal"
        largeImage = "terminal"
        largeText = "GNOME-terminal"

    elif "konsole" in (i.name() for i in psutil.process_iter()):
        state = "On KDE-Konsole"
        largeImage = "konsole"
        largeText = "KDE-Konsole"

    #identifying shell
    shells = ["ZSH", "Bash", "Tmux", "Fish", "Dash"]
    for shell in shells:
        if theShell == f"/usr/bin/{shell.lower()}":
            details = f"Using {shell} shell"
            smallImage = shell.lower()
            smallText = f"{shell} shell"
    
    return state, largeImage, largeText, details, smallImage, smallText

timeOfStart = time.time() # shows the elapsed time at the bottom (needs to be started in Slushy.update())

print("started\n")

while True:
    try:
        (state, largeImage, largeText, details, smallImage, smallText) = getData()
        
        Slushy = Presence(client_id=LaunchCode)
        Slushy.connect()
        Slushy.update(start=timeOfStart,
                      state=state,
                      large_image=largeImage,
                      large_text=largeText,
                      details=details,
                      small_image=smallImage,
                      small_text=smallText)
        print("Connect success!")
        time.sleep(30)
    except:
        print("Failed to connect\nWaiting...\n")
        time.sleep(5)
        pass
