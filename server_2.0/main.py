import socketserver
import file_funcs as ff
from startup import *

class TcpThreads(socketserver.ThreadingMixIn, socketserver.TCPServer):
    socketserver.TCPServer.allow_reuse_address = True #reuse address when the server is restarted
    pass

class ServerHandler(socketserver.BaseRequestHandler):
    def setup(self):
        pass
        print("New connection from: ",self.client_address[0])
    def handle(self):
        self.data = self.request.recv(1024)
        #detects whether a sensor is connecting or a browser
        if 'User' in str(self.data):
            pass
        else:
            #prepare the string to add to the queue
            try:
                ff.writer(self.data, configuration)
            except:
                splited = str(self.data).split('/')
                splited = [i.strip('THID=') for i in splited]
                print('Error handling the lecture from sensor {}, it may be corrupted contact support'.format(splited[1]))

if __name__ == "__main__":
    configuration = read_conf() #from startup file
    print('Configuration:', configuration)

    startup(configuration)
    address = (configuration['ip'], int(configuration['port']))
    servidor = TcpThreads(address, ServerHandler) #uses the TcpThread class then handler class
    run(servidor)
