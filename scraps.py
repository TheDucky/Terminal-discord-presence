from tkinter import N
from tkinter.messagebox import NO, YES
import psutil

if "gnome-terminal-server" in (i.name() for i in psutil.process_iter()):
    print(YES)
else:
    print(NO)