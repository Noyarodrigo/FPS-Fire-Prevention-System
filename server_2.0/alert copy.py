#alert process send a mail when a value goes higher than spected
import camara
import os
import smtplib , ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def sendmail(configuration):
    
    password = configuration["password"]
    fromaddr = configuration["sender"]
    toaddr = configuration["reciever"]
    """
    try:
        name = camara.capturar() #camara.py
        img_data = open(name, 'rb').read()
    except:
        print("No se pudo abrir la imagen")
    """
    msg = MIMEMultipart()
    msg['Subject'] = 'PYLogger defense system'
    msg['From'] = fromaddr
    msg['To'] = toaddr
    try:
        text = MIMEText("\nWARNING! One of your sensors passed the limit\nContact information: +542616123311 -Roi")
        msg.attach(text)
        #image = MIMEImage(img_data, name="captura.png")
        #msg.attach(image)
    except:
        print("No se pudo adjuntar")
    
    port = 465
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(configuration["sender"], configuration["password"])
            server.sendmail(configuration["sender"], configuration["reciever"], msg)
            print("\tALERT SENT!\n------------------------------")

    except:
        print("Error de servidor")

-------------------------


        import smtplib,glob,os
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import camara

def sendmail(configuration):
    
    password = configuration["password"]
    fromaddr = configuration["sender"]
    toaddr = configuration["reciever"]

    COMMASPACE = ', '
    try:
        msg = MIMEMultipart()
        msg['Subject'] = 'PYLogger defense system'
        msg['From'] = fromaddr
        msg['To'] = COMMASPACE.join(toaddr)
        msg.preamble = '\nWARNING! One of your sensors passed the limit\nContact information: +542616123311 -Roi'
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
    try:    
        # Send the email via our own SMTP server.
        s = smtplib.SMTP("localhost")
        print("SERVIDOR ABIERTO")
        s.sendmail(fromaddr, toaddr, msg.as_string())
        s.quit()
    except:
        print("Error servidor")