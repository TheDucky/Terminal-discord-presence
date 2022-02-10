# for Windows terminals, CMD and Powershell!

import time
import psutil
from pypresence import Presence

LaunchCode = "939904925494829086"

# identifying terminal
if "powershell.exe" in (i.name() for i in psutil.process_iter()):
    presenceState = "On Powershell"
    presenceLargeImage = "powershell"
    presenceLargeText="Powershell"
    
elif "cmd.exe" in (i.name() for i in psutil.process_iter()):
    presenceState = "On CMD"
    presenceLargeImage = "cmd"
    presenceLargeText = "CMD"
    
elif "" in (i.name() for i in psutil.process_iter()):
    presenceState = "On Windows-Terminal"
    presenceLargeImage = "winterminal"
    presenceLargeText = "Windows-Terminal"

timeOfStart = time.time() # shows the elapsed time at the bottom (needs to be started in Slushy.update()

print("started\n")

while True:
    try:
        Slushy = Presence(client_id=LaunchCode)
        Slushy.connect()
        Slushy.update(state=presenceState,
                      start=timeOfStart,
                      large_image=presenceLargeImage,
                      large_text=presenceLargeText)
        print("Connect success!")
        time.sleep(30)
    except:
        print("Failed to connect\nWaiting...\n")
        time.sleep(5)
        pass
