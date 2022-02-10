# for Linux terminals!

import os
import time
import psutil
from pypresence import Presence

LaunchCode = "939904925494829086" # paste your client id here
theShell = os.environ['SHELL']

<<<<<<< HEAD
while True: # start the handshake loop!
    try:
        Slushy = Presence(client_id=LaunchCode)
        Slushy.connect()
        print("Handshake successfully!")
        break
    except:
        print("ERROR initializing handshake!\nWaiting..." )
        time.sleep(10)

timeOfStart = time.time() # shows the elapsed time at the bottom needs to be started in Slushy.update()

while True:

    if "gnome-terminal" in (i.name() for i in psutil.process_iter()):

        if theShell == "/usr/bin/zsh":
            Slushy.update(state="On GNOME-terminal",
                          details="Using ZSH shell",
                          start=timeOfStart,
                          large_image="terminal",
                          large_text="GNOME-terminal",
                          small_image="zsh",
                          small_text="ZSH shell")

        elif theShell == "/usr/bin/bash":
            Slushy.update(state="On GNOME-terminal",
                          details="Using Bash shell",
                          start=timeOfStart,
                          large_image="terminal",
                          large_text="GNOME-terminal",
                          small_image="bash",
                          small_text="Bash shell")
=======
# identifying terminal
if "gnome-terminal" in (i.name() for i in psutil.process_iter()):
    presenceState = "On GNOME-terminal"
    presenceLargeImage = "terminal"
    presenceLargeText = "GNOME-terminal"
>>>>>>> 57993461d883d60e50ccb18cdcd0e87eba25ca7b

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
