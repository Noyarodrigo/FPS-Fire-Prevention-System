#aathis submodule contains the reader/writter/prepare functions for main.py (server)
from datetime import datetime
import time
import alert as al

ultima_alarma = time.time()

def writer(data, configuration):
    with open(configuration['file'], 'a') as lectures:
        print('-.-.-writing in file-.-.-')
        for el in data:
            lectures.write(str(el)+'\n')
        buff = []

def parser(data,configuration):
    global ultima_alarma
    cleaned = []
    splited = str(data).split('&')
    tmp1 = str(splited[1].split('=')[1])
    cleaned.append(tmp1)
    hum = str(splited[2].split('=')[1])
    cleaned.append(hum)
    tmp2 = str(splited[3].split('=')[1])[:5]
    cleaned.append(tmp2)
    print(cleaned)
    tiempo = time.time() - ultima_alarma
    print(tiempo)
    if tiempo >= 30:
        limit = float(configuration['temp']) #this limit has been taken from the conf file
        if float(tmp1) >= limit or float(tmp2) >= limit: #alarm
            print('--...SENDING ALERT...--')
            al.sendmail(configuration)
            ultima_alarma = time.time()
    return cleaned
