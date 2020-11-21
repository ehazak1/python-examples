'''
A Simple HTTP client
'''

import socket
from gzip import GzipFile
from StringIO import StringIO

host = 'www.cisco.com'
port = 80
address = host, port
resource = '/'
request = 'GET %s HTTP/1.1\r\n' % resource
request += 'Host: %s\r\n' % host
request += 'Connection: close\r\n'
request += 'User-Agent: My Fun HTTP Client\r\n'
request += 'Accept-encoding: gzip\r\n'
request += '\r\n'

s = socket.socket() # AF_INET, SOCK_STREAM
s.connect(address)

s.sendall(request)

data = []

while True:
    chunk = s.recv(4096)
    if not chunk:
        break;
    data.append(chunk)
response = ''.join(data)

header, content = response.split('\r\n\r\n', 1)
if 'Content-Encoding: gzip' in header.splitlines():
    fake_file = StringIO(content)
    content = GzipFile(fileobj=fake_file).read()
    
