from PIL import Image, ImageDraw, ImageFont
import os
font = ImageFont.truetype('arialbd.ttf',60)
color = (66, 133, 244)
namesFile = open("names.txt","r")
names = namesFile.read().split("\n")
mid = 500
startH = 225

try:
    os.mkdir("Output")
except:
    pass

for name in names:
    name = name.upper()
    img = Image.open('GDSC cert.png')
    draw = ImageDraw.Draw(img)
    width,height = draw.textsize(name)
    numberOfLetters = width/6
    overAllPixels = (numberOfLetters-1)*40
    draw.text(xy=(mid-(overAllPixels/2),startH),text=f"{name}",fill=color,font=font)
    #img.show()
    img.save(f"output/{name}.png")
namesFile.close()