import os
import psutil

if "gnome-terminal-server" in (i.name() for i in psutil.process_iter()):
    print("YES")
else:
    print("NO")

theshell = os.system("SHELL")
print(theshell)