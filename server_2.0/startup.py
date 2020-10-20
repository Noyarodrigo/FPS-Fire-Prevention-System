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

def read_conf_server():
    configuration = {} 
    try:
        with open ('config/config_server.txt', 'r') as conf_file:
            for line in conf_file:
                if line[0] != '#':
                    clean = line.split('=')
                    configuration[clean[0].strip('\n')] = clean[1].strip('\n')
            return configuration

    except:
        print('Unable to load the server configuration file, shuting down the server')
        sys.exit() #terminate program

def read_conf_sensors():
    sensors = {} 
    try:
        with open ('config/config_sensors.txt', 'r') as conf_file:
            for line in conf_file:
                if line[0] != '#':
                    clean = line.split('=')
                    sensors[clean[0].strip('\n')] = clean[1].strip('\n').split(',')
            return sensors

    except:
        print('Unable to load the sensor configuration file, shuting down the server')
        sys.exit() #terminate program 
        
def read_conf_cameras():
    cameras = {} 
    try:
        with open ('config/config_camera.txt', 'r') as conf_file:
            for line in conf_file:
                if line[0] != '#':
                    clean = line.split('=')
                    cameras[clean[0].strip('\n')] = clean[1].strip('\n').split(',')
            return cameras

    except:
        print('Unable to load the camera configuration file, shuting down the server')
        sys.exit() #terminate program