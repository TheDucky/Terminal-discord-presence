#!/usr/bin/python3

import time
import subprocess
from tkinter import E
from pypresence import Presence

APP_ID = "941253431836934164"

while True: # start the handshake loop!
    try:
        nanoScent = Presence(client_id=APP_ID)
        nanoScent.connect()
        print("Handshake successfully!")
        break
    except:
        print("ERROR initializing handshake!\nWaiting..." )
        time.sleep(10)

timeOfStart = time.time() # shows the elapsed time at the bottom needs to be started in nanoScent.update()

while True:

    runPGREP = subprocess.run(["pgrep", "-af", "nano"], capture_output=True)
    pidInfo = runPGREP.stdout.decode().split()
    if len(pidInfo):
        fileName = str(', '.join(pidInfo[2:3]))
        editingFile = "Editing " + fileName
        nanoScent.update(details=editingFile, large_image="nano", large_text="GNU-nano", start=timeOfStart)
    else:
        pass
    
    time.sleep(5)