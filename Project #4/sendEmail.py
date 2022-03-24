import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def openConnection(sender_email,password):
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
    server.login(sender_email, password)
    return server

def send_email(server,receiver_email,name,sender_email):
    subject = "Your Certificate from GDSC"
    bodyName = name.split(" ")[0].lower().capitalize()
    body = f"Hello {bodyName}!\nPlease find attached your certificate.\nBest regards,\nI'm bot BTW!"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    #message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))
    filename = f"./Output/{name}.png"

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {name.lower().capitalize()} Certificate.png",
    )

    message.attach(part)
    text = message.as_string()

    server.sendmail(sender_email, receiver_email, text) 