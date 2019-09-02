import os
import random
import threading
import subprocess
import openrazer.client
try:
    import Image
except ImportError:
    from PIL import Image

#Path to pictures
path = "/home/cody/Pictures/Wallpapers"

#Time In Seconds ex. 300 = 5min, 120 = 2min, 60=1min
time = 10


def getBackground():
    background = random.choice(os.listdir(path))
    #background = "m4Qw8yB.jpg"
    #background = "space.jpg"

    if os.path.isfile(os.path.join(path, background)) and background.lower().endswith(('.png', '.jpg', '.jpeg')):
        return background
    else:
        print("Not Img File - Trying Again! Error File: " + background)
        return getBackground()

def getColor(background):
    backgroundFile = background
    filePath = path + "/" + backgroundFile
    img = Image.open(filePath)
    img.thumbnail((200, 200))
    w, h = img.size

    #w, h = image.size
    pixels = img.getcolors(w * h)
    most_frequent_pixel = pixels[0]
    

    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)

    rgb = most_frequent_pixel[1]
    print(rgb)

    if rgb[0] == 0 and rgb[1] == 0 and rgb[2] == 0 or rgb[0] == 1 and rgb[1] == 1 and rgb[2] == 1 or rgb[0] == 2 and rgb[1] == 2 and rgb[2] == 2:
        print("No Color Matched - Default to Backlight")
        rgb = (255,255,255)
        return rgb
    
    else:
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





