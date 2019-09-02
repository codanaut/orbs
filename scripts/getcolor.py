try:
    import Image
except ImportError:
    from PIL import Image

def getColor(background):
    img = Image.open(background)
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
    hexVal = '#{:02x}{:02x}{:02x}'.format( rgb[0],rgb[1],rgb[2] )
    print(hexVal)


path = "/home/cody/Pictures/Wallpapers/jasnbiyat3vy.png"

getColor(path)