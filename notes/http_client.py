'''
A simple HTTP client.
'''

import socket
from gzip import GzipFile
from StringIO import StringIO

host = 'www.cisco.com'
port = 80
resource = '/'
address = host, port

request = 'GET %s HTTP/1.1\r\n' % resource
request += 'Host: %s\r\n' % host
request += 'User-Agent: My Fun HTTP Client\r\n'
request += 'Connection: close\r\n'
request += 'Accept-encoding: gzip\r\n'
request += '\r\n'

s = socket.socket() # AF_INET, SOCK_STREAM
s.connect(address)

s.sendall(request)

data = []
while True:
    chunk = s.recv(4096)
    if not chunk:
        break
    data.append(chunk)
response = ''.join(data)

header, content = response.split('\r\n\r\n', 1)
if 'Content-Encoding: gzip' in header.splitlines():
    fakefile = StringIO(content)
    content = GzipFile(fileobj=fakefile).read()
