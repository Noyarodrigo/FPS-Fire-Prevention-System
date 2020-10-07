#alert process send a mail when a value goes higher than spected
import smtplib, ssl

def sendmail(configuration):
    port = 465

    sender = configuration["sender"] 
    password = configuration["password"]
    recieve = configuration["reciever"]

    message = "Subject: PYlogger Defense system \nWARNING! One of your sensors passed the limit\nContact information: +542616123311 -Roi"

    context = ssl.create_default_context()
    print('\n\n---------------------------------')
  
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, message)
        print("\tALERT SENT!\n------------------------------")