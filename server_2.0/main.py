import socketserver
import file_funcs as ff
from startup import *

buff = []

class TcpThreads(socketserver.ThreadingMixIn, socketserver.TCPServer):
    socketserver.TCPServer.allow_reuse_address = True #reuse address when the server is restarted
    pass

class ServerHandler(socketserver.BaseRequestHandler):
    def setup(self):
        print("Nueva conexion desde: ",self.client_address[0])
        #pass
    def handle(self):
        global buff
        self.data = self.request.recv(2048)
        #detects whether a sensor is connecting or a browser
        if 'User' in str(self.data):
            pass
        else:
            try:
                #print(self.data)
                tmp = ff.parser(self.data,configuration,sensors,cameras)
                buff.append(tmp)
                if len(buff) >= int(configuration['n_of_l']): #block and write the file
                    ff.writer(buff,configuration)
                    buff = []
            except:
                print('Error handling the lecture from sensor, it may be corrupted contact support')

if __name__ == "__main__":
   
    configuration = read_conf_server()
    sensors = read_conf_sensors()
    cameras = read_conf_cameras()
    print('Configuration:', configuration)
    print('sensors:\n', sensors)
    print('cameras:\n', cameras)
    startup(configuration)
    address = (configuration['ip'], int(configuration['port']))
    servidor = TcpThreads(address, ServerHandler) #uses the TcpThread class then handler class
    run(servidor)
