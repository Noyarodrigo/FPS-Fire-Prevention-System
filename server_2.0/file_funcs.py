#aathis submodule contains the reader/writter/prepare functions for main.py (server)
from datetime import datetime
from startup import *
import time

ultima_alarma = 1290 

def writer(data, configuration):
    with open(configuration['file'], 'a') as lectures:
        print('-.-.-writing in file-.-.-')
        for el in data:
            lectures.write(str(el)+'\n')
        buff = []

def parser(data,configuration):
    global ultima_alarma
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    tmp = str(data).split('HTTP')[0]
    splited = tmp[8:].split(',')
    splited.append(timestamp)
    print(splited)
    time_elapsed = time.time() - ultima_alarma
    if get_date(60):
        limit = int(configuration['temp']) #this limit should be taken from the conf file
        if float(splited[0]) >= limit or float(splited[2]) >= limit: #alarm
            print('--Sending Alert--')
            time_now = datetime.now().strftime("%H:%M:%S").split(':')
            ultima_alarma = ((int(time_now[0])*60)+int(time_now[1])+(int(time_now[2])/60))
    return splited

def get_date(sampling_time):
    time_now = datetime.now().strftime("%H:%M:%S").split(':')
    delta_time = ((int(time_now[0])*60)+int(time_now[1])+(int(time_now[2])/60))-(ultima_alarma)
    print(delta_time)
    if delta_time >= int(sampling_time) or delta_time<0:
        return True
    return False
