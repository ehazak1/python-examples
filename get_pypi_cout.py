'''
Show the current number of packages listed on the Python  Package Index (Pypi)

Michael's Guidlines for Building a Regular Expression Pattern
=============================================================
1. start by using re.findall
'''

from urllib import urlopen
import re

url = 'https://pypi.python.org/pypi'
response = urlopen(url)
data = response.read()
text = data.decode('utf-8')

mo = re.search('There are currently\n.*?([0-9]+).*\npackages here', text)
if mo is not None:
    print mo.group(1)
