#!/usr/bin/env python3

import socket

HOST = '192.168.1.35'  # The server's hostname or IP address
PORT = 80        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'AGO3Y6O5OF03OMSB&field1=22.75&field2=33.00&field3=80.00&field4=0\r\n\r\n[2]')