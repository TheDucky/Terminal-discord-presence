# for Windows terminals, CMD and Powershell!

import os
import time
import psutil
from pypresence import Presence
from dotenv import load_dotenv

load_dotenv()
LaunchCode = os.getenv("CLIENT_ID") # paste your client id here
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

    if "powershell.exe" in (i.name() for i in psutil.process_iter()):

            Slushy.update(state="On Powershell",
                          start=timeOfStart,
                          large_image="winterminal",
                          large_text="Powershell")

    elif "cmd.exe" in (i.name() for i in psutil.process_iter()):

            Slushy.update(state="On CMD",
                          start=timeOfStart,
                          large_image="cmd",
                          large_text="CMD")
    time.sleep(15)
