# ORBS <br> Open Razr Background Switcher

ORBS is a basic python script for randomly setting the background image from a pool of background images and then setting a matching or predefined color to Razer Devices using the OpenRazer library. 

Several options are available for configuring the background pool and color scheme to apply for each one. For each script just set the path to either the wallpaper folder or config file and set the time to however long you'd like the background the stay before changing. 

## ORBS

orbs-pixel.py

orbs-pixel works by finding the most common pixel in the image and then sets the backlight to that color. This works great most the time but does have it's downsides. Sometimes the most common pixel in the image isn't what you would expect and for darker images you may end up with black which will shut off the backlight. If the most common pixel comes back as nothing the backlight will get set to a default of white. 

orbs-cluster.py 

orbs-cluster works by using the colorz.py script I found on THIS blog post to get a group of pixels from the image and then sets the keyboard to that. This one sometimes works better then orbs-pixel but it depends on the image. The advantage is that orbs-pixel will always return the same pixel but orbs-cluster will usually return sliglty different colors depending on where it clustered from. (Make sure to move the colorz.py from the scripts into the same folder you save orbs-cluster.py to.)

orbs-json.py

orbs-json uses a json file containing the path to the background and a hex value of the color you'd like the backlight set to. I created this one because i wanted a way to set only certain images with predefined colors without having to create a new folders and move around images from a pool of them. Theres also a sqlite version of this i may also release later. 

## Requirements

You will need to have the OpenRazer drivers and library installed.

orbs-cluster may also need colorsys installed and will need the colorz.py file from the scripts folder moved into the same directory. 

## Supported Devices & Systems

ORBS was created while using gnome so the default command for all the scripts is using <code>gsettings set org.gnome.desktop.background</code>. This can be changed to <code>feh --bg-scale</code> when using i3 and should still work. It has been tested a little but not with every script.

Two Razer keyboards have been tested and worked without issue but have not had a mouse available for testing. I think it should work but I can't say for sure yet. 