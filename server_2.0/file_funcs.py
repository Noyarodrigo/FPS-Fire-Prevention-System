#aathis submodule contains the reader/writter/prepare functions for main.py (server)
from datetime import datetime
from startup import *

def writer(data, configuration):
    buff = [] #this would be a buffer to save a certain amounts of lectures until you open the file and write, it's a performance test
    print(data)
    """
    limit = int(configuration[3]) #this limit should be taken from the conf file
    if float(data[1]) >= limit: #alarm
        print('--Sending Alert--')
    """
    buff.append(data)
    if len(buff) >= int(configuration['n_of_l']): #block and write the file
        with open(configuration['file'], 'a') as lectures:
            print('-.-.-writing in file-.-.-')
            for el in buff:
                lectures.write(str(el)+'\n')
            buff = []
