#!/usr/bin/env python

import socket
import time
import os
import sys

address = ('127.0.0.1', 3600)
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.bind(address)
sck.listen(5)
newSck, clientAddress = sck.accept()
while True:
    #newSck, clientAddress = sck.accept()
    curTime = time.strftime('%Y/%m/%d/%H/%M/%S')
    newSck.send('server: ' + curTime) 
    recvData = newSck.recv(512)
    if recvData:
        if recvData == 'exit':
            newSck.close()
            sck.close()
            sys.exit()
        else:
            print(recvData)
    #newSck.close()

