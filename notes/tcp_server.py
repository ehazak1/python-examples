'''
A simple TCP server.
'''
import socket
import time

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

def server(handler, host, port):
    address = host, port
    s = socket.socket() # AF_INET, SOCK_STREAM
    s.bind(address)
    s.listen(5)
    try:
        while True:
            c, who = s.accept()
            handler(c, who)
    except KeyboardInterrupt:
        pass
    finally:
        s.close()

if __name__ == '__main__':
    server(heartbeat, 'localhost', 9000)
