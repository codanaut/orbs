# ORBS <br> Open Razer Background Switcher

ORBS is a basic python script for randomly setting the background image from a pool of background images and then setting a matching or predefined color to Razer Devices using the [OpenRazer](https://github.com/openrazer/openrazer) library. 

Several options are available for configuring the background pool and color scheme to apply for each one. For each script just set the path to either the wallpaper folder or config file and then set the time for how long you'd like the background to stay before changing. 

## ORBS

### [orbs-pixel.py](orbs-pixel.py)

orbs-pixel works by finding the most common pixel in the image and then sets the back light to that color. This works great most the time but does have it's downsides. Sometimes the most common pixel in the image isn't what you would expect and for darker images you may end up with black which will shut off the back light. If the most common pixel comes back as nothing the back light will get set to a default of white. 

### [orbs-cluster.py](orbs-cluster.py) 

orbs-cluster works by using the colorz.py script I found on [THIS](https://charlesleifer.com/blog/using-python-and-k-means-to-find-the-dominant-colors-in-images/) blog post to get a group of pixels from the image and then sets the keyboard to that. This one sometimes works better then orbs-pixel but it depends on the image. The advantage is that orbs-pixel will always return the same pixel but orbs-cluster will usually return slightly different colors depending on where it clustered from. (Make sure to move the colorz.py from the scripts into the same folder you save orbs-cluster.py to.)

### [orbs-json.py](orbs-json.py)

orbs-json uses a json file containing the path to the background and a hex value of the color you'd like the back light set to. I created this one because i wanted a way to set only certain images with predefined colors without having to create a new folders and move around images from a pool of them. There's also a sqlite version of this i may also release later. 

## Requirements

You will need to have the [OpenRazer](https://github.com/openrazer/openrazer) drivers and library installed.

orbs-cluster may also need <code>colorsys</code> installed and will need the <code>colorz.py</code> file from the scripts folder moved into the same directory. 

## How To Use

Once you have decided on which script to go with open it with your favorite editor and change the <code>PATH</code> and <code>TIME</code> to the path of a folder full of wallpapers you would like to use. If your using the orbs-json then set the path to the json file and then fill in the path to each photo and the hex of each color. The more you add the less chance of getting the same one multiple times when being randomly selected. 
Once you have the path set run the script with
<code>python3 orbs-”pixel,cluster,json”.py</code>

## Scripts
<code>getcolor.py</code> - this uses the same function from orbs-pixel to get the most common pixel and print the hex and rgb values in the terminal. I tend to use this when adding a new background to the orbs-json and then adjust the values from there.

<code>colorz.py</code> – This script came from [THIS](https://charlesleifer.com/blog/using-python-and-k-means-to-find-the-dominant-colors-in-images/) blog post and is used to generate the colors for orbs-cluster. It must be moved into the same folder as where you store orbs-cluster.py

<code>themes.json</code> – this is an example theme file for orbs-json. Set the path of each background and the color you would like to be set with it. 

## Supported Devices & Systems

ORBS was created while using gnome so the default command for all the scripts is using <code>gsettings set org.gnome.desktop.background</code>. This can be changed to <code>feh --bg-scale</code> when using i3 and should still work. It has been tested a little but not with every script.

Two Razer keyboards have been tested and worked without issue but have not had a mouse available for testing. I think it should work but I can't say for sure yet. 

