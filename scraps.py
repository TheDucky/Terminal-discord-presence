import os
import psutil

if "gnome-terminal-server" in (i.name() for i in psutil.process_iter()):
    print("YES")
else:
    print("NO")

theshell = os.system("$SHELL --version")
smn = filter(str.isdigit, theshell)
numeric = "".join(smn)
print(numeric)