import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import camara

def sendmail(configuration,cleaned,sensors,cameras):
    port = 465

    password = configuration["password"]
    fromaddr = configuration["sender"]
    toaddr = configuration["reciever"]
    try:
        msg = MIMEMultipart()
        msg['Subject'] = 'PYLogger defense system'
        msg['From'] = fromaddr
        msg['To'] = toaddr

        mensaje = "\nWARNING! One of your sensors passed the limit\n"+ str(cleaned) +"\nContact information: +542616123311 -Roi"
        text = MIMEText(mensaje)
        msg.attach(text)
        
    except:     
        print("Error cabeceras")

    try:
        names = camara.capturar(cleaned[0],sensors,cameras) #camara.py
    except:
        print("No se pudo abrir la imagen")

    try:
        for name in names:
            fp = open(name, 'rb')
            img = MIMEImage(fp.read())
            fp.close()
            msg.attach(img)
    except:
        print("Error adjuntar")

    context = ssl.create_default_context()
  
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddr, msg.as_string())
        print("\n\n---------------------------------\nALERT SENT!\n------------------------------")
    
    camara.clean_captures(names)