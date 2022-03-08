from PIL import Image, ImageDraw, ImageFont
import os
font = ImageFont.truetype('./Project #1/arialbd.ttf',60)
color = (66, 133, 244)
namesFile = open("./Project #1/names.txt","r")
names = namesFile.read().split("\n")
mid = 500
startH = 225

try:
    os.mkdir("./Project #1/Output")
except:
    pass

for name in names:
    name = name.upper()
    img = Image.open('./Project #1/GDSC cert.png')
    draw = ImageDraw.Draw(img)
    width,height = draw.textsize(name)
    numberOfLetters = width/6
    overAllPixels = (numberOfLetters-1)*40
    draw.text(xy=(mid-(overAllPixels/2),startH),text=f"{name}",fill=color,font=font)
    #img.show()
    img.save(f"./Project #1/output/{name}.png")
namesFile.close()