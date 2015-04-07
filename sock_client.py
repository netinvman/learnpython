#!/usr/bin/env python

import socket
import os
import sys

address = ('127.0.0.1', 3600)
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.connect(address)
while True:
    recvData = sck.recv(512)
    print(recvData)
    clientData = raw_input('client: ')
    if clientData == 'exit':
        sck.send(clientData)
        sck.close()
        sys.exit()
    else:
        sck.send(clientData)
