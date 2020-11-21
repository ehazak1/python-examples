'''
A simple TCP server.
'''
import socket
import time
import os

def greetings(c, who):
    print 'Connected with', who
    c.sendall(b'Hello!')
    c.close()

def heartbeat(c, who):
    print 'Connected with', who
    for i in range(10):
        c.sendall(time.ctime())
        time.sleep(1)
    c.close()
    print 'Closed connection with', who

def hardwork(c, who):
    print 'Connected with', who
    c.sendall('Doing hard work...')
    sum(xrange(int(1e9)))
    c.sendall('Done!')
    c.close()

def server(handler, host, port):
    address = host, port
    s = socket.socket() # AF_INET, SOCK_STREAM
    s.bind(address)
    s.listen(5)
    try:
        while True:
            c, who = s.accept()
            pid = os.fork()
            if pid: # I am the parent
                c.close()
            else: # I am the child
                handler(c, who)
                os._exit(0)
    except KeyboardInterrupt:
        pass
    finally:
        s.close()

if __name__ == '__main__':
    server(hardwork, 'localhost', 9000)
