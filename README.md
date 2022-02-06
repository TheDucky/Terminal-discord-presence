# Terminal-discord-presence
a simple script that grabs basic terminal info and displays it as Discord Rich Presence

## Requirements
- python3<br>
`sudo apt install python3`
`sudo dnf install python3` etc.

- psutil and pypresence<br>
`pip install pypresence` & `pip install psutil`

## How to setup Terminal-discord-presence
1. Press the "Code" button and download zip file.
2. extract the zip file to your preferred location
3. create a new discord application by going to: https://discord.com/developers/applications/
4. upload all the images from the icon folder to the /rich-presence/assets on the discord developer page
5. copy the APPLICATION ID and paste it in `clid` variable on line 10
6. run the file `python3 main.py`

### ! the script will not run if discord is not open in the background !

## Showcase 

![GNOME-terminal ZSH](showcase.png)