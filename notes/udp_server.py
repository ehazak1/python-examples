'''
A simple UDP server.
'''

import socket

address = 'localhost', 9000
s = socket.socket(socket.AF_INET,
                  socket.SOCK_DGRAM)
s.bind(address)
try:
    while True:
        data, who = s.recvfrom(4096)
        print data, who
except KeyboardInterrupt:
    pass
finally:
    s.close()
    print '...goodbye!'
