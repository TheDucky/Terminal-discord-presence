# for Windows terminals, CMD and Powershell!

import time
import psutil
from pypresence import Presence

<<<<<<< HEAD
LaunchCode = "939904925494829086" # paste your client id here
Slushy = Presence(client_id=LaunchCode)
=======
load_dotenv()
LaunchCode = os.getenv("CLIENT_ID") # paste your client id here
>>>>>>> 5e5e6a6098b5d84f097a5839989dc3ff0096bcc7

while True: # start the handshake loop!
    try:
        Slushy = Presence(client_id=LaunchCode)
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
                          large_image="powershell",
                          large_text="Powershell")

    elif "cmd.exe" in (i.name() for i in psutil.process_iter()):

            Slushy.update(state="On CMD",
                          start=timeOfStart,
                          large_image="cmd",
                          large_text="CMD")

    elif "" in (i.name() for i in psutil.process_iter()):

            Slushy.update(state="On Windows-Terminal",
                          start=timeOfStart,
                          large_image="winterminal",
                          large_text="Windows-Terminal")


    time.sleep(15)
