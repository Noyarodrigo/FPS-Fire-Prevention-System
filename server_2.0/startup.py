#settings for the server when it starts
import file_funcs as ff
import alert as al
import os
import sys

def startup(configuration):
    if not os.path.exists(configuration['file']): #check if the file exists and create if it doesn't  
        os.mknod(configuration['file'])

def run(servidor):
    try:
        print('Server Process ... OK')
        servidor.serve_forever() #serve until ctrl+c (or other) is passed
    except KeyboardInterrupt:
        servidor.shutdown()
        servidor.socket.close()

def read_conf():
    configuration = {} 
    try:
        with open ('config.txt', 'r') as conf_file:
            for line in conf_file:
                if line[0] != '-':
                    clean = line.split('=')
                    configuration[clean[0].strip('\n')] = clean[1].strip('\n')
            return configuration

    except:
        print('Unable to load the configuration file, shuting down the server')
        sys.exit() #terminate program with multiprocessing
        

