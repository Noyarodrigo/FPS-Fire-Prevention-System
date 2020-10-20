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

def parser(data,configuration,sensors,cameras):
    global ultima_alarma
    cleaned = []
    ide = str(data[-6:]).strip("b'\\n\\r\\n[]")
    cleaned.append(ide)
    splited = str(data).split('&')
    tmp1 = str(splited[1].split('=')[1])
    cleaned.append(tmp1)
    hum = str(splited[2].split('=')[1])
    cleaned.append(hum)
    tmp2 = str(splited[3].split('=')[1])
    cleaned.append(tmp2)
    gas = str(splited[4].split('=')[1])[:4].strip('\ r')
    cleaned.append(gas)
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    cleaned.append(timestamp)
    print(cleaned)
    tiempo = time.time() - ultima_alarma
    print("Tiempo desde la ultima alarma: ", tiempo)
    if tiempo >= int(configuration["alert_time"]) and configuration["enable"] == "1":
        tmp_limit = float(configuration['tmp_limit']) #this limit has been taken from the conf file
        hum_limit = float(configuration['hum_limit']) #this limit has been taken from the conf file
        gas_limit = float(configuration['gas_limit']) #this limit has been taken from the conf file
        if float(tmp1) >= tmp_limit or float(tmp2) >= tmp_limit or float(hum) <= hum_limit or float(gas) >= gas_limit: #alarm
            ultima_alarma = time.time()
            print('--...SENDING ALERT...--')
            al.sendmail(configuration,cleaned,sensors,cameras)
    return cleaned
