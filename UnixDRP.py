# for Linux terminals!

import os
import time
import psutil
from pypresence import Presence

LaunchCode = "939904925494829086" # paste your client id here
theShell = os.environ['SHELL']
Slushy = Presence(client_id=LaunchCode)

while True: # start the handshake loop!
    try:
        Slushy.connect()
        print("Handshake successfully!")
        break
    except:
        print("ERROR initializing handshake!\nWaiting..." )
        time.sleep(10)

timeOfStart = time.time() # shows the elapsed time at the bottom (needs to be started in Slushy.update()

while True:

    if "gnome-terminal-server" in (i.name() for i in psutil.process_iter()):

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

        elif theShell == "/usr/bin/tmux":
            Slushy.update(state="On GNOME-terminal",
                          details="Using Tmux shell",
                          start=timeOfStart,
                          large_image="terminal",
                          large_text="GNOME-terminal",
                          small_image="tmux",
                          small_text="Tmux shell")

        elif theShell == "/usr/bin/fish":
            Slushy.update(state="On GNOME-terminal",
                          details="Using Fish shell",
                          start=timeOfStart,
                          large_image="terminal",
                          large_text="GNOME-terminal",
                          small_image="fish",
                          small_text="Fish shell")

        elif theShell == "/usr/bin/dash":
            Slushy.update(state="On GNOME-terminal",
                          details="Using Dash shell",
                          start=timeOfStart,
                          large_image="terminal",
                          large_text="GNOME-terminal",
                          small_image="dash",
                          small_text="Dash shell")

    if "konsole" in (i.name() for i in psutil.process_iter()):

        if theShell == "/usr/bin/zsh":
            Slushy.update(state="On KDE-Konsole",
                          details="Using ZSH shell",
                          start=timeOfStart,
                          large_image="konsole",
                          large_text="KDE-Konsolel",
                          small_image="zsh",
                          small_text="ZSH shell")

        elif theShell == "/usr/bin/bash":
            Slushy.update(state="On KDE-Konsole",
                          details="Using Bash shell",
                          start=timeOfStart,
                          large_image="konsole",
                           arge_text="KDE-Konsole",
                          small_image="bash",
                           mall_text="Bash shell")

        elif theShell == "/usr/bin/tmux":
            Slushy.update(state="On KDE-Konsole",
                          details="Using Tmux shell",
                          start=timeOfStart,
                          large_image="konsole",
                          large_text="KDE-Konsole",
                          small_image="tmux",
                          small_text="Tmux shell")

        elif theShell == "/usr/bin/fish":
            Slushy.update(state="On KDE-Konsole",
                          details="Using Fish shell",
                          start=timeOfStart,
                          large_image="konsole",
                          large_text="KDE-Konsole",
                          small_image="fish",
                          small_text="Fish shell")

        elif theShell == "/usr/bin/dash":
            Slushy.update(state="On KDE-Konsole",
                          details="Using Dash shell",
                          start=timeOfStart,
                          large_image="konsole",
                          large_text="KDE-Konsole",
                          small_image="dash",
                          small_text="Dash shell")

    time.sleep(15)
