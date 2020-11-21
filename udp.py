'''
A Simple UDP client
'''

import socket
import time

address = 'localhost', 9000

s = socket.socket(socket.AF_INET,
                  socket.SOCK_DGRAM)

s.sendto('Hello?', address)
for i in range(10):
    s.sendto(time.ctime(), address)
    time.sleep(1)
