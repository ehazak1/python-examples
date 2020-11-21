'''
A simple TCP client
'''

import socket

address = 'localhost', 9000

s = socket.socket() # AF_INET, SOCK_STREAM
s.connect(address)
try:
    while True:
        data = s.recv(4096)
        if not data: # If we have an empty str
            break
        print data
finally:
    s.close()
