'''
Show the current number of packages listed on the Python Package Index (PyPI)

Michael's Guidelines for Building a Regular Expression Pattern
==============================================================
1. start by using re.findall
2. write a small pattern
3. refine it by trial-and-error

        Make sure to look at the original data!
        It might not be what you think it is.
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

