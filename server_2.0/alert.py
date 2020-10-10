import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import camara

def sendmail(configuration):
    port = 465

    password = configuration["password"]
    fromaddr = configuration["sender"]
    toaddr = configuration["reciever"]
    message = "Subject: PYlogger Defense system \nWARNING! One of your sensors passed the limit\nContact information: +542616123311 -Roi"

    COMMASPACE = ', '
    try:
        msg = MIMEMultipart()
        msg['Subject'] = 'PYLogger defense system'
        msg['From'] = fromaddr
        #msg['To'] = COMMASPACE.join(toaddr)
        msg['To'] = toaddr

        text = MIMEText("\nWARNING! One of your sensors passed the limit\nContact information: +542616123311 -Roi")
        msg.attach(text)
        #msg.preamble = '\nWARNING! One of your sensors passed the limit\nContact information: +542616123311 -Roi'
    except:     
        print("Error cabeceras")

    try:
        name = camara.capturar() #camara.py
    except:
        print("No se pudo abrir la imagen")

    try:
        fp = open(name, 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)
    except:
        print("Error adjuntar")

    context = ssl.create_default_context()
    print('\n\n---------------------------------')
  
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddr, msg.as_string())
        print("\tALERT SENT!\n------------------------------")
