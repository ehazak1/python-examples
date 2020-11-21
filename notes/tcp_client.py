'''
A simple TCP client.
'''
import socket

address = 'localhost', 9000
s = socket.socket() # AF_INET, SOCK_STREAM
s.connect(address)
try:
    while True:
        data = s.recv(4096)
        if not data:
            break
        print data.decode('utf-8')
finally:
    s.close()
