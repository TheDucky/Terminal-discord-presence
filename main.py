import os
import time
import psutil
from pypresence import Presence

theShell = os.environ['SHELL']

clid = '--' # paste your client id here
Slushy = Presence(client_id=clid)

while True: # start the handshake loop!
    try:
        Slushy.connect()
        print("Handshake successfully!")
        break
    except:
        print("ERROR initializing handshake!\nWaiting..." )
        time.sleep(5)

timeOfStart = time.time() # shows the elapsed time at the bottom (needs to be started in Slushy.update()

while True:

    if "gnome-terminal-server" in (i.name() for i in psutil.process_iter()):

        if theShell == "/usr/bin/zsh":
            Slushy.update(state="On GNOME-terminal", details="Using ZSH shell", start=timeOfStart,
                          large_image="terminal", large_text="GNOME-terminal",
                          small_image="zsh", small_text="ZSH shell")

        elif theShell == "/usr/bin/bash":
            Slushy.update(state="On GNOME-terminal", details="Using Bash shell", start=timeOfStart,
                          large_image="terminal", large_text="GNOME-terminal",
                          small_image="bash", small_text="Bash shell")

        elif theShell == "/usr/bin/tmux":
            Slushy.update(state="On GNOME-terminal", details="Using Tmux shell", start=timeOfStart,
                          large_image="terminal", large_text="GNOME-terminal",
                          small_image="tmux", small_text="Tmux shell")

        elif theShell == "/usr/bin/fish":
            Slushy.update(state="On GNOME-terminal", details="Using Fish shell", start=timeOfStart,
                          large_image="terminal", large_text="GNOME-terminal",
                          small_image="fish", small_text="Fish shell")  

        elif theShell == "/usr/bin/dash":
            Slushy.update(state="On GNOME-terminal", details="Using Dash shell", start=timeOfStart,
                          large_image="terminal", large_text="GNOME-terminal",
                          small_image="dash", small_text="Dash shell")                                  
        else:
            Slushy.clear()      
    else:
        Slushy.clear() 
        
    time.sleep(5)
