import smtplib
from email.message import EmailMessage
import imghdr

def email_alert(subject, body, to, file):
    msg = EmailMessage()
    msg.set_content(body)

    user = "robotic.arm.delpozzo@gmail.com"
    password = "lwoahwsncgwjocgp"

    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = user
    with open(file, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    msg.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    
    server = smtplib.SMTP("smtp.gmail.com")
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()
