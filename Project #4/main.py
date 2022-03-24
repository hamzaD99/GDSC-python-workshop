from PIL import Image, ImageDraw, ImageFont
import os
import sendEmail as email
font = ImageFont.truetype('arialbd.ttf',60)
color = (66, 133, 244)
namesFile = open("names.txt","r")
lines = namesFile.read().split("\n")
mid = 500
startH = 225

sender_email = "hamzaserver89@gmail.com"
password = "Python@gdsc2022"

server = email.openConnection(sender_email,password)

try:
    os.mkdir("Output")
except:
    pass

for line in lines:
    line = line.split(",")
    name = line[0]
    perEmail = line[1]
    name = name.upper()
    img = Image.open('GDSC cert.png')
    draw = ImageDraw.Draw(img)
    width,height = draw.textsize(name)
    numberOfLetters = len(name)
    overAllPixels = (numberOfLetters-1)*40
    draw.text(xy=(mid-(overAllPixels/2),startH),text=f"{name}",fill=color,font=font)
    #img.show()
    img.save(f"Output/{name}.png")
    if perEmail != "-":
        email.send_email(server,perEmail,name,sender_email)
namesFile.close()