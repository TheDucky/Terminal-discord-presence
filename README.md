# Terminal-discord-presence
a simple script that detects when the command-line is open, grabs basic terminal info and displays it as Discord Rich Presence

## Requirements
- python3<br>
`sudo apt install python3` or 
`sudo dnf install python3` etc.

- psutil and pypresence<br>
`pip install pypresence` & `pip install psutil`

## How to setup Terminal-discord-presence
1. Click on 'Code' and download the zip file
2. extract the zip file to your preferred location
3. create a new discord application by going to: https://discord.com/developers/applications/
4. upload all the images from the icon folder to the /rich-presence/assets on the discord developer page
5. copy the APPLICATION ID and paste it in `LaunchCode` variable on line 10
6. choose the correct `.py` file for your system 
    * <u>UnixDRP.py</u> - For GNOME-terminal and KDE-Konsole
    * <u>WindowsDRP.py</u> - For Windows CMD, Powershell and Terminal
 
7. run the file `python3 file_name.py`

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

## Showcase 

GNOME-terminal             |KDE konsole
:-------------------------:|:-------------------------:
![GNOME-terminal ZSH](/showcase/1.png) | ![KDE konsole fish](/showcase/3.png)
![GNOME-terminal Tmux](/showcase/4.png) | ![KDE konsole Bash](/showcase/2.png)
