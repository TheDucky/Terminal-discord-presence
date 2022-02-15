# Terminal-discord-presence
A simple script that detects when the command-line is open, grabs basic terminal info and displays it as Discord Rich Presence

## Requirements
- python3<br>
`sudo apt install python3` or 
`sudo dnf install python3` etc.

- psutil and pypresence<br>
`pip install pypresence` & `pip install psutil`

## How to setup Terminal-discord-presence
1. Press the "Code" button and download zip file.

2. Choose the correct `.py` file for your system 
    * [UnixDRP.py] - For GNOME-terminal and KDE-Konsole
    * [WindowsDRP.py] - For Windows CMD, Powershell and Terminal
 
3. Run the file `python3 file_name.py` 

**AND YOU ARE DONE!. ITS THAT SIMPLE**

## Make the python file run on startup
- Copy the python file to /bin:<br>
`sudo cp -i /path/to/your_main.py /bin`

- Add A New Cron Job:<br>
`sudo crontab -e`

- Scroll to the bottom and add the following line (after all the #'s):<br>
`@reboot python /bin/your_main.py &`

- The “&” at the end of the line means the command is run in the background and it won’t stop the system booting up.

- Finally:<br>
`sudo reboot`

## Nano rich presence!

run the [NanoPresence.py] to show rich presence for the nano CLI editor! <br/>
<img width=200px src="showcase/8.png">

## Showcase 

GNOME-terminal             |KDE konsole               |Windows
:-------------------------:|:-------------------------: |:-------------------------:
![GNOME-terminal ZSH](/showcase/1.png) | ![KDE konsole fish](/showcase/3.png) | ![powershell](/showcase/5.png)
![GNOME-terminal Tmux](/showcase/4.png) | ![KDE konsole Bash](/showcase/2.png) | ![Windowsterminal](/showcase/6.png)
| | | ![cmd](/showcase/7.png)

<!-- Resources -->

[herelink]: https://discord.com/developers/applications/
[UnixDRP.py]: UnixDRP.py
[WindowsDRP.py]: WindowsDRP.py
[NanoPresence.py]: NanoPresence.py
