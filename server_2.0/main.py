import socketserver
import file_funcs as ff
from startup import *
#import graf as gr
#import multiprocessing

buff = []

class TcpThreads(socketserver.ThreadingMixIn, socketserver.TCPServer):
    socketserver.TCPServer.allow_reuse_address = True #reuse address when the server is restarted
    pass

class ServerHandler(socketserver.BaseRequestHandler):
    def setup(self):
        pass
        print("New connection from: ",self.client_address[0])
    def handle(self):
        global buff
        self.data = self.request.recv(2048)
        #detects whether a sensor is connecting or a browser
        if 'User' in str(self.data):
            pass
        else:
            #prepare the string to add to the queue
            try:
                tmp = ff.parser(self.data,configuration)
                buff.append(tmp)
                if len(buff) >= int(configuration['n_of_l']): #block and write the file
                    ff.writer(buff,configuration)
                    buff = []
            except:
                print('Error handling the lecture from sensor, it may be corrupted contact support')

if __name__ == "__main__":
    """q = multiprocessing.Queue()
    graficador = multiprocessing.Process(target=gr.animate, args=(q,)) #cretes and start writter process
    graficador.start()
    """
    configuration = read_conf()
    print('Configuration:', configuration)
    startup(configuration)
    address = (configuration['ip'], int(configuration['port']))
    servidor = TcpThreads(address, ServerHandler) #uses the TcpThread class then handler class
    run(servidor)
