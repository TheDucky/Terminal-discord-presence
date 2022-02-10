# for Windows terminals, CMD and Powershell!

import time
import psutil
from pypresence import Presence

LaunchCode = "939904925494829086"

# identify terminal and get terminal data
def getData():
    if "powershell.exe" in (i.name() for i in psutil.process_iter()):
        state = "On Powershell"
        largeImage = "powershell"
        largeText ="Powershell"
    
    elif "cmd.exe" in (i.name() for i in psutil.process_iter()):
        state = "On CMD"
        largeImage = "cmd"
        largeText = "CMD"
        
    elif "" in (i.name() for i in psutil.process_iter()):
        state = "On Windows-Terminal"
        largeImage = "winterminal"
        largeText = "Windows-Terminal"
    
    return state, largeImage, largeText

timeOfStart = time.time() # shows the elapsed time at the bottom (needs to be started in Slushy.update()

print("started\n")

while True:
    try:
        (state, largeImage, largeText) = getData()
        Slushy = Presence(client_id=LaunchCode)
        Slushy.connect()
        Slushy.update(start=timeOfStart,
                      state=state,
                      large_image=largeImage,
                      large_text=largeText)
        print("Connect success!")
        time.sleep(30)
    except:
        print("Failed to connect\nWaiting...\n")
        time.sleep(5)
        pass
