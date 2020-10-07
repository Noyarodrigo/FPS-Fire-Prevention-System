#aathis submodule contains the reader/writter/prepare functions for main.py (server)
from datetime import datetime
import time

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
    print("tmp2: ", tmp2)
    cleaned.append(tmp2)
    print(cleaned)
    tiempo = time.time() - ultima_alarma
    if tiempo >= 30:
        print("AAAAAAA")
        limit = float(configuration['temp']) #this limit has been taken from the conf file
        print(limit)
        print(float(tmp2))
        if float(tmp2) >= limit:
            print("ALARMAAAAAAAAAa")
        if float(tmp1) >= limit or float(tmp2) >= limit: #alarm
            print('--Sending Alert--')
            ultima_alarma = time.time()
    return cleaned
