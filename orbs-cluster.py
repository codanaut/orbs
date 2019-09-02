import os
import random
import threading
import subprocess
import openrazer.client
import colorsys
from colorz import colorz

#Path to pictures
path = "/home/cody/Pictures/Wallpapers"

#Time In Seconds ex. 300 = 5min, 120 = 2min, 60=1min
time = 30


def getBackground():
    background = random.choice(os.listdir(path))
    if os.path.isfile(os.path.join(path, background)) and background.lower().endswith(('.png', '.jpg', '.jpeg')):
        return background
    else:
        print("Not Img File - Trying Again! Error File: " + background)
        return getBackground()

def getColor(background):
    backgroundFile = background
    filePath = path + "/" + backgroundFile
    for c in colorz(filePath, n=3):
        cStrip = c.lstrip('#')
        rgb = tuple(int(cStrip[i:i+2], 16) for i in (0, 2, 4))
        return rgb

def setBackground(background):
    backgroundFile = background
    print("changing background to - " + backgroundFile)
    subprocess.call("gsettings set org.gnome.desktop.background picture-uri file://{0}/{1}".format(path,backgroundFile), shell=True)

def setlightColor(rgb):
    device_manager = openrazer.client.DeviceManager()

    device_manager.sync_effects = False

    for device in device_manager.devices:
        #Get the Color
        color = rgb
        #print info
        print("Setting {} to {},{},{}".format(device.name,color[0],color[1],color[2]))
        
        # Set the effect
        device.fx.static(color[0],color[1],color[2])
        device.brightness = 100

def setAll():
    print("-")
    background = getBackground()
    color = getColor(background)
    setBackground(background)
    setlightColor(color)
    print("-")


def run():
    threading.Timer(time, run).start()
    setAll()

#Run the program
run()





