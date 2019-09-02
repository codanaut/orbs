import json
import os
import random
import threading
import subprocess
import openrazer.client


#Time In Seconds ex. 300 = 5min, 120 = 2min, 60=1min
time = 10

themesFile = "./scripts/themes.json"

def getBackground():
    with open(themesFile) as json_file:
        json_data = json.load(json_file)
        count = len(json_data)
        count2 = count - 1
        ranNum = random.randint(0,count2)
        print("random number: " + str(ranNum))
        theme = json_data[str(ranNum)]
        return theme


def setBackground(background):
    backgroundFile = background
    print("changing background to - " + backgroundFile)
    subprocess.call("gsettings set org.gnome.desktop.background picture-uri file://{0}".format(backgroundFile), shell=True)

def setlightColor(rgb):
    device_manager = openrazer.client.DeviceManager()

    device_manager.sync_effects = False

    for device in device_manager.devices:
        #Get the Color
        rgbStrip = rgb.lstrip('#')
        color = tuple(int(rgbStrip[i:i+2], 16) for i in (0, 2, 4))
        
        #print info
        print("Setting {} to {}".format(device.name,color))
        
        # Set the effect
        device.fx.static(color[0],color[1],color[2])
        device.brightness = 100

def setAll():
    print("-")
    background = getBackground()
    path = background['path']
    color = background['rgb']
    print("hex: " + color)
    #print(path)
    setBackground(path)
    setlightColor(color)
    print("-")


def run():
    threading.Timer(time, run).start()
    setAll()

#Run the program
run()




