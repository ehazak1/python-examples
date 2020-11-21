Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 26 2016, 12:10:39) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
>>> qr_url_template
'https://chart.googleapis.com/chart?cht=qr&chl=Hello+world&choe=UTF-8&chs=300x300'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import urllib
>>> 
>>> urllib.urlopen
<function urlopen at 0x103a7bb18>
>>> 
>>> # in Python 3:    urllib.request.urlopen
>>> 
>>> 
>>> urllib.urlopen(qr_url_template)
<addinfourl at 4355520848 whose fp = <socket._fileobject object at 0x103a663d0>>
>>> _
<addinfourl at 4355520848 whose fp = <socket._fileobject object at 0x103a663d0>>
>>> 2 + 2
4
>>> response = urllib.urlopen(qr_url_template)
>>> data = response.read()
>>> type(data)
<type 'str'>
>>> len(data)
1264
>>> data[:100]
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01,\x00\x00\x01,\x08\x02\x00\x00\x00\xf6\x1f\x19"\x00\x00\x00\x06bKGD\x00\xff\x00\xff\x00\xff\xa0\xbd\xa7\x93\x00\x00\x04\xa5IDATx\x9c\xed\xdd\xb1n\xdb0\x14@\xd1\xaa\xc8\xff\xff\xb2\xbat\x08:\x08\t\x18\xea\x92\xec9k`G\xb6|\xf1\x96\x07\xea\xba\xef\xfb\x17\xd0'
>>> data.decode()

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    data.decode()
UnicodeDecodeError: 'ascii' codec can't decode byte 0x89 in position 0: ordinal not in range(128)
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/vcard.py", line 28, in <module>
    vcard = template % (last, first, fullname, title, phone, email)
NameError: name 'template' is not defined
>>> __doc__
'\nMaking vCards for the brother-in-law.\n'
>>> 
>>> import vcard

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    import vcard
  File "/Users/mike/teaching/2016-09-19/vcard.py", line 28, in <module>
    vcard = template % (last, first, fullname, title, phone, email)
NameError: name 'template' is not defined
>>> vcard

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    vcard
NameError: name 'vcard' is not defined
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
>>> import vcard
>>> help(vcard)
Help on module vcard:

NAME
    vcard - Making vCards for the brother-in-law.

FILE
    /Users/mike/teaching/2016-09-19/vcard.py

DATA
    contacts_file = <closed file 'notes/raisin_team.csv', mode 'r'>
    email = 'gertrude@example.com'
    filename = 'Schmidt.Gertrude.vcf'
    first = 'Gertrude'
    fullname = 'Gertrude Schmidt'
    last = 'Schmidt'
    line = 'Schmidt,Gertrude,VP Business Development,gertrude@example.com,...
    phone = '559-555-6700'
    qr_url_template = 'https://chart.googleapis.com/chart?cht=qr&chl=%s&ch...
    title = 'VP Business Development'
    vcard = 'BEGIN:VCARD\nVERSION:2.1\nN:Schmidt;Gertrude\nFN:Ge... of Ame...
    vcard_file = <closed file 'Schmidt.Gertrude.vcf', mode 'w'>
    vcard_template = 'BEGIN:VCARD\nVERSION:2.1\nN:%s;%s\nFN:%s\nORG:Califo...


>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
>>> 
>>> 
>>> 
>>> import math
>>> 
>>> math.sqrt(4)
2.0
>>> math.sin(0)
0.0
>>> math.cos(0)
1.0
>>> 
>>> 
>>> 
>>> 
>>> dir()
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'contacts_file', 'email', 'filename', 'first', 'fullname', 'last', 'line', 'math', 'phone', 'qr_img', 'qr_img_file', 'qr_url', 'qr_url_template', 'response', 'title', 'urllib', 'vcard_file', 'vcard_template', 'vcard_text']
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> import math
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'math']
>>> 
>>> sin

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    sin
NameError: name 'sin' is not defined
>>> 
>>> sin = math.sin
>>> sin
<built-in function sin>
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'math', 'sin']
>>> 
>>> sin is math.sin
True
>>> 
>>> 
>>> cos = math.cos
>>> tan = math.tan
>>> 
>>> del math
>>> 
>>> cos(0)
1.0
>>> 
>>> 
>>> math.arcsin

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    math.arcsin
NameError: name 'math' is not defined
>>> 
>>> import math
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> import math
>>> sin = math.sin
>>> del math
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> from math import sin
>>> 
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sin']
>>> 
>>> from math import sin, cos
>>> from math import sin, cos, tan, atan
>>> from math import sin, cos, tan, atan, acos, asin, sqrt, log, log1p, exp
>>> from math import sin, cos, tan, atan, acos, asin, sqrt, log, log1p, exp
>>> 
>>> from math import *
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> 
>>> from gzip import *
>>> from urllib import *
>>> from json import *
>>> from pickle import *
>>> dir()
['APPEND', 'APPENDS', 'BINFLOAT', 'BINGET', 'BININT', 'BININT1', 'BININT2', 'BINPERSID', 'BINPUT', 'BINSTRING', 'BINUNICODE', 'BUILD', 'DICT', 'DUP', 'EMPTY_DICT', 'EMPTY_LIST', 'EMPTY_TUPLE', 'EXT1', 'EXT2', 'EXT4', 'FALSE', 'FLOAT', 'FancyURLopener', 'GET', 'GLOBAL', 'GzipFile', 'HIGHEST_PROTOCOL', 'INST', 'INT', 'JSONDecoder', 'JSONEncoder', 'LIST', 'LONG', 'LONG1', 'LONG4', 'LONG_BINGET', 'LONG_BINPUT', 'MARK', 'NEWFALSE', 'NEWOBJ', 'NEWTRUE', 'NONE', 'OBJ', 'PERSID', 'POP', 'POP_MARK', 'PROTO', 'PUT', 'PickleError', 'Pickler', 'PicklingError', 'REDUCE', 'SETITEM', 'SETITEMS', 'SHORT_BINSTRING', 'STOP', 'STRING', 'TRUE', 'TUPLE', 'TUPLE1', 'TUPLE2', 'TUPLE3', 'UNICODE', 'URLopener', 'Unpickler', 'UnpicklingError', '__builtins__', '__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'basejoin', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'dump', 'dumps', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'ftperrors', 'gamma', 'getproxies', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'load', 'loads', 'localhost', 'log', 'log10', 'log1p', 'modf', 'open', 'pathname2url', 'pi', 'pow', 'quote', 'quote_plus', 'radians', 'sin', 'sinh', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'sqrt', 'tan', 'tanh', 'thishost', 'trunc', 'unquote', 'unquote_plus', 'unwrap', 'url2pathname', 'urlcleanup', 'urlencode', 'urlopen', 'urlretrieve']
>>> with open('raisin_team.csv') as f:
	text = f.read()

	

Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    with open('raisin_team.csv') as f:
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/gzip.py", line 34, in open
    return GzipFile(filename, mode, compresslevel)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/gzip.py", line 94, in __init__
    fileobj = self.myfileobj = __builtin__.open(filename, mode or 'rb')
IOError: [Errno 2] No such file or directory: 'raisin_team.csv'
>>> with open('notes/raisin_team.csv') as f:
	text = f.read()

	

Traceback (most recent call last):
  File "<pyshell#100>", line 2, in <module>
    text = f.read()
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/gzip.py", line 261, in read
    self._read(readsize)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/gzip.py", line 303, in _read
    self._read_gzip_header()
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/gzip.py", line 197, in _read_gzip_header
    raise IOError, 'Not a gzipped file'
IOError: Not a gzipped file
>>> dir()
['APPEND', 'APPENDS', 'BINFLOAT', 'BINGET', 'BININT', 'BININT1', 'BININT2', 'BINPERSID', 'BINPUT', 'BINSTRING', 'BINUNICODE', 'BUILD', 'DICT', 'DUP', 'EMPTY_DICT', 'EMPTY_LIST', 'EMPTY_TUPLE', 'EXT1', 'EXT2', 'EXT4', 'FALSE', 'FLOAT', 'FancyURLopener', 'GET', 'GLOBAL', 'GzipFile', 'HIGHEST_PROTOCOL', 'INST', 'INT', 'JSONDecoder', 'JSONEncoder', 'LIST', 'LONG', 'LONG1', 'LONG4', 'LONG_BINGET', 'LONG_BINPUT', 'MARK', 'NEWFALSE', 'NEWOBJ', 'NEWTRUE', 'NONE', 'OBJ', 'PERSID', 'POP', 'POP_MARK', 'PROTO', 'PUT', 'PickleError', 'Pickler', 'PicklingError', 'REDUCE', 'SETITEM', 'SETITEMS', 'SHORT_BINSTRING', 'STOP', 'STRING', 'TRUE', 'TUPLE', 'TUPLE1', 'TUPLE2', 'TUPLE3', 'UNICODE', 'URLopener', 'Unpickler', 'UnpicklingError', '__builtins__', '__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'basejoin', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'dump', 'dumps', 'e', 'erf', 'erfc', 'exp', 'expm1', 'f', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'ftperrors', 'gamma', 'getproxies', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'load', 'loads', 'localhost', 'log', 'log10', 'log1p', 'modf', 'open', 'pathname2url', 'pi', 'pow', 'quote', 'quote_plus', 'radians', 'sin', 'sinh', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'sqrt', 'tan', 'tanh', 'thishost', 'trunc', 'unquote', 'unquote_plus', 'unwrap', 'url2pathname', 'urlcleanup', 'urlencode', 'urlopen', 'urlretrieve']
>>> from gzip import *
>>> open
<function open at 0x103a4f848>
>>> import gzip
>>> gzip.open is open
True
>>> 
>>> 
>>> del open
>>> open
<built-in function open>
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
>>> import gzip
>>> gzip
<module 'gzip' from '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/gzip.pyc'>
>>> 
>>> 
>>> from gzip import open as gopen
>>> gopen
<function open at 0x103a4f848>
>>> gopen is gzip.open
True
>>> 
>>> 
>>> import numpy as np
>>> 
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/download.py ============
======= Source: https://dl.dropboxusercontent.com/u/54337323/2016-09-19/links.txt ========
                      Starting download at Tue Sep 20 10:47:53 2016                       
https://dl.dropboxusercontent.com/u/54337323/2016-09-19/links.txt
304  NOT MODIFIED https://dl.dropboxusercontent.com/u/3967849/shared/PythonAwesome.pdf
200* OK           https://dl.dropboxusercontent.com/u/54337323/data/symlinks.txt
                  --> notes/symlinks.txt        (current)
200* OK           https://dl.dropboxusercontent.com/u/54337323/data/show_int_brief.xml
                  --> notes/show_int_brief.xml  (current)
200* OK           https://dl.dropboxusercontent.com/u/3967849/shared/ipv4_int_bri.txt
                  --> notes/ipv4_int_bri.txt    (current)
200* OK           https://dl.dropboxusercontent.com/u/3967849/shared/books.xml
                  --> notes/books.xml           (current)
304  NOT MODIFIED https://dl.dropboxusercontent.com/u/3967849/shared/raisin_team.csv
304  NOT MODIFIED https://dl.dropboxusercontent.com/u/3967849/shared/__init__.py
200* OK           https://dl.dropboxusercontent.com/u/54337323/data/show_int_brief.json
                  --> notes/show_int_brief.json (current)
304  NOT MODIFIED https://dl.dropboxusercontent.com/u/3967849/shared/BeautifulSoup.py
200* OK           https://dl.dropboxusercontent.com/u/54337323/data/alltimegross.html
                  --> notes/alltimegross.html   (current)
200* OK           https://dl.dropboxusercontent.com/u/54337323/data/nasa.log.sample
                  --> notes/nasa.log.sample     (current)
200* OK           https://dl.dropboxusercontent.com/u/54337323/data/enron.lay-k.inbox.sample
                  --> notes/enron.lay-k.inbox.sample (current)
200* OK           https://dl.dropboxusercontent.com/u/3967849/shared/interfaces.xml
                  --> notes/interfaces.xml      (current)
200* OK           https://dl.dropboxusercontent.com/u/3967849/shared/books.json
                  --> notes/books.json          (current)
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/brief.py =============
Interface                      IP-Address      Status                Protocol
Loopback0                      51.51.51.51     Up                    Up
MgmtEth0/RSP0/CPU0/0           1.20.30.40      Up                    Up
MgmtEth0/RSP0/CPU0/1           unassigned      Down                  Down
MgmtEth0/RSP1/CPU0/0           unassigned      Up                    Up
HundredGigE0/1/0/0             unassigned      Shutdown              Down
HundredGigE0/1/0/1             unassigned      Shutdown              Down
TenGigE0/2/0/0                 unassigned      Down                  Down
TenGigE0/2/0/1                 unassigned      Down                  Down
TenGigE0/2/0/2                 unassigned      Down                  Down
TenGigE0/2/0/4                 unassigned      Down                  Down
TenGigE0/2/0/5                 unassigned      Down                  Down
TenGigE0/2/0/6                 unassigned      Down                  Down
TenGigE0/2/0/7                 unassigned      Down                  Down
GigabitEthernet0/3/0/1         unassigned      Up                    Up
GigabitEthernet0/3/0/2         unassigned      Down                  Down
GigabitEthernet0/3/0/3         unassigned      Up                    Up
GigabitEthernet0/3/0/4         unassigned      Down                  Down
GigabitEthernet0/3/0/5         unassigned      Down                  Down
GigabitEthernet0/3/0/6         unassigned      Down                  Down
GigabitEthernet0/3/0/7         unassigned      Down                  Down
GigabitEthernet0/3/0/8         unassigned      Down                  Down
GigabitEthernet0/3/0/9         unassigned      Down                  Down
GigabitEthernet0/3/0/10        unassigned      Down                  Down
GigabitEthernet0/3/0/11        unassigned      Down                  Down
GigabitEthernet0/3/0/12        unassigned      Down                  Down
GigabitEthernet0/3/0/13        unassigned      Down                  Down
GigabitEthernet0/3/0/14        unassigned      Down                  Down
GigabitEthernet0/3/0/15        unassigned      Down                  Down
GigabitEthernet0/3/0/16        unassigned      Down                  Down
GigabitEthernet0/3/0/17        unassigned      Down                  Down
GigabitEthernet0/3/0/18        unassigned      Down                  Down
GigabitEthernet0/3/0/19        unassigned      Down                  Down
TenGigE0/3/1/0                 unassigned      Up                    Up
TenGigE0/3/1/1                 unassigned      Down                  Down
TenGigE0/3/1/2                 unassigned      Down                  Down
TenGigE0/3/1/3                 unassigned      Up                    Up
GigabitEthernet0/4/0/0         unassigned      Down                  Down
TenGigE0/4/0/0                 unassigned      Up                    Up
GigabitEthernet0/4/0/1         unassigned      Down                  Down
TenGigE0/4/0/1                 unassigned      Down                  Down
GigabitEthernet0/4/0/2         unassigned      Down                  Down
GigabitEthernet0/4/0/3         unassigned      Down                  Down
GigabitEthernet0/4/0/4         unassigned      Down                  Down
GigabitEthernet0/4/0/5         unassigned      Down                  Down
GigabitEthernet0/4/0/6         unassigned      Down                  Down
GigabitEthernet0/4/0/7         unassigned      Down                  Down
GigabitEthernet0/4/0/8         unassigned      Down                  Down
GigabitEthernet0/4/0/9         unassigned      Down                  Down
GigabitEthernet0/4/0/10        unassigned      Down                  Down
GigabitEthernet0/4/0/11        unassigned      Down                  Down
GigabitEthernet0/4/0/12        unassigned      Down                  Down
GigabitEthernet0/4/0/13        unassigned      Down                  Down
GigabitEthernet0/4/0/14        unassigned      Down                  Down
GigabitEthernet0/4/0/15        unassigned      Down                  Down
GigabitEthernet0/4/0/16        unassigned      Down                  Down
GigabitEthernet0/4/0/17        unassigned      Down                  Down
GigabitEthernet0/4/0/18        unassigned      Down                  Down
GigabitEthernet0/4/0/19        unassigned      Down                  Down
FortyGigE0/5/0/0               unassigned      Shutdown              Down
FortyGigE0/5/0/1               unassigned      Shutdown              Down
TenGigE0/5/1/0                 unassigned      Shutdown              Down
TenGigE0/5/1/1                 111.1.1.1       Up                    Up
GigabitEthernet0/7/0/0         unassigned      Down                  Down
GigabitEthernet0/7/0/1         unassigned      Down                  Down
GigabitEthernet0/7/0/2         unassigned      Down                  Down
GigabitEthernet0/7/0/3         unassigned      Down                  Down
GigabitEthernet0/7/0/4         unassigned      Down                  Down
GigabitEthernet0/7/0/5         unassigned      Down                  Down
GigabitEthernet0/7/0/6         unassigned      Down                  Down
GigabitEthernet0/7/0/7         unassigned      Down                  Down
GigabitEthernet0/7/0/8         unassigned      Down                  Down
GigabitEthernet0/7/0/9         unassigned      Down                  Down
GigabitEthernet0/7/0/10        unassigned      Down                  Down
GigabitEthernet0/7/0/11        unassigned      Down                  Down
GigabitEthernet0/7/0/12        unassigned      Down                  Down
GigabitEthernet0/7/0/13        unassigned      Down                  Down
GigabitEthernet0/7/0/14        unassigned      Down                  Down
GigabitEthernet0/7/0/15        unassigned      Up                    Up
GigabitEthernet0/7/0/16        unassigned      Down                  Down
GigabitEthernet0/7/0/17        unassigned      Down                  Down
GigabitEthernet0/7/0/18        unassigned      Down                  Down
GigabitEthernet0/7/0/19        unassigned      Down                  Down
GigabitEthernet0/7/0/20        unassigned      Down                  Down
GigabitEthernet0/7/0/21        unassigned      Down                  Down
GigabitEthernet0/7/0/22        unassigned      Down                  Down
GigabitEthernet0/7/0/23        unassigned      Down                  Down
GigabitEthernet0/7/0/24        unassigned      Down                  Down
GigabitEthernet0/7/0/25        unassigned      Down                  Down
GigabitEthernet0/7/0/26        unassigned      Down                  Down
GigabitEthernet0/7/0/27        unassigned      Down                  Down
GigabitEthernet0/7/0/28        unassigned      Down                  Down
GigabitEthernet0/7/0/29        unassigned      Down                  Down
GigabitEthernet0/7/0/30        unassigned      Down                  Down
GigabitEthernet0/7/0/31        unassigned      Down                  Down
GigabitEthernet0/7/0/32        unassigned      Down                  Down
GigabitEthernet0/7/0/33        unassigned      Down                  Down
GigabitEthernet0/7/0/34        unassigned      Down                  Down
GigabitEthernet0/7/0/35        unassigned      Down                  Down
GigabitEthernet0/7/0/36        unassigned      Down                  Down
GigabitEthernet0/7/0/37        unassigned      Down                  Down
GigabitEthernet0/7/0/38        unassigned      Down                  Down
GigabitEthernet0/7/0/39        unassigned      Down                  Down
>>> line
'GigabitEthernet0/7/0/39        unassigned      Down                  Down\n'
>>> line.split()
['GigabitEthernet0/7/0/39', 'unassigned', 'Down', 'Down']
>>> fields = line.split()
>>> len(fields)
4
>>> interface, address, status, protocol = fields
>>> interface
'GigabitEthernet0/7/0/39'
>>> address
'unassigned'
>>> status
'Down'
>>> protocol
'Down'
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/brief.py =============
>>> line
'GigabitEthernet0/7/0/39        unassigned      Down                  Down\n'
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/brief.py =============
Loopback0 51.51.51.51
MgmtEth0/RSP0/CPU0/0 1.20.30.40
MgmtEth0/RSP1/CPU0/0 unassigned
GigabitEthernet0/3/0/1 unassigned
GigabitEthernet0/3/0/3 unassigned
TenGigE0/3/1/0 unassigned
TenGigE0/3/1/3 unassigned
TenGigE0/4/0/0 unassigned
TenGigE0/5/1/1 111.1.1.1
GigabitEthernet0/7/0/15 unassigned
>>> help(str.split)
Help on method_descriptor:

split(...)
    S.split([sep [,maxsplit]]) -> list of strings
    
    Return a list of the words in the string S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are removed
    from the result.

>>> ',,,,,chamelion'.split(',')
['', '', '', '', '', 'chamelion']
>>> ',,,,, chamelion'.split(',')
['', '', '', '', '', ' chamelion']
>>> ',,,,, chamelion'.split('am')
[',,,,, ch', 'elion']
>>> import string
>>> string.whitespace
'\t\n\x0b\x0c\r '
>>> help(str.split)
Help on method_descriptor:

split(...)
    S.split([sep [,maxsplit]]) -> list of strings
    
    Return a list of the words in the string S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are removed
    from the result.

>>> import math
>>> math.pi
3.141592653589793
>>> 
>>> math.pi = 3
>>> math.pi
3
>>> 
=============================== RESTART: Shell ===============================
>>> import socket
>>> socket.AF_INET
2
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/brief.py =============
Loopback0 51.51.51.51
MgmtEth0/RSP0/CPU0/0 1.20.30.40
MgmtEth0/RSP1/CPU0/0 unassigned
GigabitEthernet0/3/0/1 unassigned
GigabitEthernet0/3/0/3 unassigned
TenGigE0/3/1/0 unassigned
TenGigE0/3/1/3 unassigned
TenGigE0/4/0/0 unassigned
TenGigE0/5/1/1 111.1.1.1
GigabitEthernet0/7/0/15 unassigned
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/brief.py =============
Loopback0                      51.51.51.51
MgmtEth0/RSP0/CPU0/0           1.20.30.40
MgmtEth0/RSP1/CPU0/0           unassigned
GigabitEthernet0/3/0/1         unassigned
GigabitEthernet0/3/0/3         unassigned
TenGigE0/3/1/0                 unassigned
TenGigE0/3/1/3                 unassigned
TenGigE0/4/0/0                 unassigned
TenGigE0/5/1/1                 111.1.1.1
GigabitEthernet0/7/0/15        unassigned
>>> '%s' % 5
'5'
>>> '%d' % 5
'5'
>>> '%04d' % 5
'0005'
>>> '%04f' % 5
'5.000000'
>>> '%.2f' % 5
'5.00'
>>> '%s' % 'hello'
'hello'
>>> '%30s' % 'hello'
'                         hello'
>>> '%-30s' % 'hello'
'hello                         '
>>> '%-30s' % 5
'5                             '
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/brief.py =============
Loopback0                      51.51.51.51
MgmtEth0/RSP0/CPU0/0           1.20.30.40
MgmtEth0/RSP1/CPU0/0           unassigned
GigabitEthernet0/3/0/1         unassigned
GigabitEthernet0/3/0/3         unassigned
TenGigE0/3/1/0                 unassigned
TenGigE0/3/1/3                 unassigned
TenGigE0/4/0/0                 unassigned
TenGigE0/5/1/1                 111.1.1.1
GigabitEthernet0/7/0/15        unassigned
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/brief.py =============
Loopback0                      51.51.51.51
MgmtEth0/RSP0/CPU0/0           1.20.30.40
MgmtEth0/RSP1/CPU0/0           unassigned
GigabitEthernet0/3/0/1         unassigned
GigabitEthernet0/3/0/3         unassigned
TenGigE0/3/1/0                 unassigned
TenGigE0/3/1/3                 unassigned
TenGigE0/4/0/0                 unassigned
TenGigE0/5/1/1                 111.1.1.1
GigabitEthernet0/7/0/15        unassigned
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/brief.py =============
Loopback0                      51.51.51.51

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/brief.py", line 7, in <module>
    interface, address, status, protocol = line.split()
ValueError: too many values to unpack
>>> line.split()
['MgmtEth0', 'RSP0', 'CPU0', '0', '1.20.30.40', 'Up', 'Up']
>>> 
>>> len(line.split())
7
>>> line[0:32]
'MgmtEth0 RSP0 CPU0 0           1'
>>> line[:31]
'MgmtEth0 RSP0 CPU0 0           '
>>> line[31:47]
'1.20.30.40      '
>>> line[47:70]
'Up                    U'
>>> line[47:69]
'Up                    '
>>> line[69:]
'Up\n'
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/brief.py =============
>>> status
'Down                  '
>>> len(status)
22
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/brief.py =============
Loopback0                      51.51.51.51
MgmtEth0   RSP0 CPU0 0         1.20.30.40
MgmtEth0/RSP1/CPU0/0           unassigned
GigabitEthernet0/3/0/1         unassigned
GigabitEthernet0/3/0/3         unassigned
TenGigE0/3/1/0                 unassigned
TenGigE0/3/1/3                 unassigned
TenGigE0/4/0/0                 unassigned
TenGigE0/5/1/1                 111.1.1.1
GigabitEthernet0/7/0/15        unassigned
>>> 
========= RESTART: /Users/mike/teaching/2016-09-19/get_pypi_count.py =========
>>> len(data)
23917
>>> type(data)
<type 'str'>
>>> text = data.decode('utf-8')
>>> type(text)
<type 'unicode'>
>>> text[:100]
u'<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN'
>>> 
>>> 
>>> import re
>>> re.search
<function search at 0x1006a8410>
>>> re.search # find the first occurrance
<function search at 0x1006a8410>
>>> re.findall # find all occurrances of a pattern
<function findall at 0x1006bc758>
>>> len(text)
23916
>>> re.findall('Python', text)
[u'Python', u'Python', u'Python', u'Python', u'Python', u'Python', u'Python', u'Python', u'Python', u'Python', u'Python', u'Python', u'Python', u'Python', u'Python', u'Python', u'Python', u'Python', u'Python', u'Python', u'Python', u'Python', u'Python', u'Python']
>>> len(re.findall('Python', text))
24
>>> re.search('Python', text)
<_sre.SRE_Match object at 0x1031ced98>
>>> mo = re.search('Python', text)
>>> mo.start()
349
>>> len(re.findall('python', text))
33
>>> len(re.findall('Python|python', text))
57
>>> 57 == 33 + 24
True
>>> len(re.findall('[Pp]ython', text))
57
>>> len(re.findall('[JPp]ython', text))
57
>>> len(re.findall('[0123456789]', text))
736
>>> re.findall('[0123456789]', text)
[u'1', u'0', u'8', u'3', u'1', u'0', u'3', u'1', u'1', u'3', u'1', u'9', u'9', u'9', u'8', u'4', u'0', u'4', u'0', u'4', u'0', u'4', u'4', u'7', u'0', u'9', u'3', u'1', u'1', u'0', u'1', u'2', u'0', u'3', u'0', u'3', u'3', u'3', u'3', u'4', u'0', u'3', u'4', u'0', u'6', u'6', u'1', u'5', u'0', u'5', u'1', u'3', u'5', u'0', u'4', u'1', u'5', u'4', u'4', u'3', u'3', u'3', u'1', u'6', u'1', u'6', u'1', u'6', u'1', u'6', u'1', u'1', u'8', u'9', u'0', u'3', u'7', u'6', u'6', u'1', u'5', u'0', u'5', u'1', u'3', u'5', u'0', u'4', u'0', u'3', u'0', u'4', u'0', u'3', u'0', u'4', u'0', u'3', u'3', u'0', u'3', u'0', u'4', u'0', u'0', u'3', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'3', u'0', u'0', u'3', u'0', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'1', u'0', u'1', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'8', u'0', u'2', u'8', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'2', u'0', u'1', u'2', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'0', u'0', u'1', u'0', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'3', u'1', u'1', u'3', u'1', u'1', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'6', u'0', u'2', u'6', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'7', u'1', u'5', u'0', u'7', u'1', u'5', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'8', u'2', u'0', u'1', u'5', u'8', u'2', u'0', u'1', u'5', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'2', u'0', u'2', u'0', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'0', u'1', u'0', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'5', u'0', u'0', u'5', u'0', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'5', u'1', u'6', u'0', u'5', u'1', u'6', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'1', u'1', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'2', u'0', u'1', u'6', u'1', u'0', u'4', u'2', u'0', u'1', u'6', u'1', u'0', u'4', u'2', u'0', u'1', u'6', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'6', u'9', u'1', u'6', u'9', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'0', u'1', u'0', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'4', u'0', u'2', u'4', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'1', u'0', u'1', u'1', u'0', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'3', u'2', u'0', u'3', u'2', u'0', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'1', u'6', u'1', u'1', u'6', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'5', u'3', u'1', u'5', u'3', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'2', u'0', u'1', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'0', u'6', u'0', u'0', u'6', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'2', u'0', u'2', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'9', u'5', u'0', u'9', u'5', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'2', u'0', u'2', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'2', u'0', u'2', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'2', u'0', u'2', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'1', u'1', u'1', u'1', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'2', u'0', u'2', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'2', u'0', u'2', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'2', u'0', u'1', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'4', u'0', u'1', u'8', u'4', u'0', u'1', u'8', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'8', u'0', u'1', u'8', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'3', u'0', u'2', u'3', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'3', u'1', u'1', u'3', u'1', u'3', u'2', u'1', u'6', u'6', u'6', u'0', u'2', u'2', u'2', u'0', u'3', u'3', u'3', u'1', u'9', u'9', u'0', u'2', u'0', u'1', u'6', u'1', u'0', u'1', u'5', u'5', u'9', u'6', u'1', u'9', u'1', u'1', u'1', u'3', u'2', u'2', u'6', u'6', u'3', u'4', u'4', u'0', u'0', u'1', u'1', u'1', u'1', u'1', u'1', u'0', u'0', u'2', u'3', u'4']
>>> re.findall('[0-9]', text)
[u'1', u'0', u'8', u'3', u'1', u'0', u'3', u'1', u'1', u'3', u'1', u'9', u'9', u'9', u'8', u'4', u'0', u'4', u'0', u'4', u'0', u'4', u'4', u'7', u'0', u'9', u'3', u'1', u'1', u'0', u'1', u'2', u'0', u'3', u'0', u'3', u'3', u'3', u'3', u'4', u'0', u'3', u'4', u'0', u'6', u'6', u'1', u'5', u'0', u'5', u'1', u'3', u'5', u'0', u'4', u'1', u'5', u'4', u'4', u'3', u'3', u'3', u'1', u'6', u'1', u'6', u'1', u'6', u'1', u'6', u'1', u'1', u'8', u'9', u'0', u'3', u'7', u'6', u'6', u'1', u'5', u'0', u'5', u'1', u'3', u'5', u'0', u'4', u'0', u'3', u'0', u'4', u'0', u'3', u'0', u'4', u'0', u'3', u'3', u'0', u'3', u'0', u'4', u'0', u'0', u'3', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'3', u'0', u'0', u'3', u'0', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'1', u'0', u'1', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'8', u'0', u'2', u'8', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'2', u'0', u'1', u'2', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'0', u'0', u'1', u'0', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'3', u'1', u'1', u'3', u'1', u'1', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'6', u'0', u'2', u'6', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'7', u'1', u'5', u'0', u'7', u'1', u'5', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'8', u'2', u'0', u'1', u'5', u'8', u'2', u'0', u'1', u'5', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'2', u'0', u'2', u'0', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'0', u'1', u'0', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'5', u'0', u'0', u'5', u'0', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'5', u'1', u'6', u'0', u'5', u'1', u'6', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'1', u'1', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'2', u'0', u'1', u'6', u'1', u'0', u'4', u'2', u'0', u'1', u'6', u'1', u'0', u'4', u'2', u'0', u'1', u'6', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'6', u'9', u'1', u'6', u'9', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'0', u'1', u'0', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'4', u'0', u'2', u'4', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'1', u'0', u'1', u'1', u'0', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'3', u'2', u'0', u'3', u'2', u'0', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'1', u'6', u'1', u'1', u'6', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'5', u'3', u'1', u'5', u'3', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'2', u'0', u'1', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'0', u'6', u'0', u'0', u'6', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'2', u'0', u'2', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'9', u'5', u'0', u'9', u'5', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'2', u'0', u'2', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'2', u'0', u'2', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'2', u'0', u'2', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'1', u'1', u'1', u'1', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'2', u'0', u'2', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'2', u'0', u'2', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'2', u'0', u'1', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'4', u'0', u'1', u'8', u'4', u'0', u'1', u'8', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'8', u'0', u'1', u'8', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'3', u'0', u'2', u'3', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'3', u'1', u'1', u'3', u'1', u'3', u'2', u'1', u'6', u'6', u'6', u'0', u'2', u'2', u'2', u'0', u'3', u'3', u'3', u'1', u'9', u'9', u'0', u'2', u'0', u'1', u'6', u'1', u'0', u'1', u'5', u'5', u'9', u'6', u'1', u'9', u'1', u'1', u'1', u'3', u'2', u'2', u'6', u'6', u'3', u'4', u'4', u'0', u'0', u'1', u'1', u'1', u'1', u'1', u'1', u'0', u'0', u'2', u'3', u'4']
>>> # re.findall('[A-Za-z]', text)
>>> ord('Z')
90
>>> ord('a')
97
>>> chr('91')

Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    chr('91')
TypeError: an integer is required
>>> chr(91)
'['
>>> re.findall('[Z-A]', text)

Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    re.findall('[Z-A]', text)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/re.py", line 181, in findall
    return _compile(pattern, flags).findall(string)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/re.py", line 251, in _compile
    raise error, v # invalid expression
error: bad character range
>>> re.findall('[0-9]', text)
[u'1', u'0', u'8', u'3', u'1', u'0', u'3', u'1', u'1', u'3', u'1', u'9', u'9', u'9', u'8', u'4', u'0', u'4', u'0', u'4', u'0', u'4', u'4', u'7', u'0', u'9', u'3', u'1', u'1', u'0', u'1', u'2', u'0', u'3', u'0', u'3', u'3', u'3', u'3', u'4', u'0', u'3', u'4', u'0', u'6', u'6', u'1', u'5', u'0', u'5', u'1', u'3', u'5', u'0', u'4', u'1', u'5', u'4', u'4', u'3', u'3', u'3', u'1', u'6', u'1', u'6', u'1', u'6', u'1', u'6', u'1', u'1', u'8', u'9', u'0', u'3', u'7', u'6', u'6', u'1', u'5', u'0', u'5', u'1', u'3', u'5', u'0', u'4', u'0', u'3', u'0', u'4', u'0', u'3', u'0', u'4', u'0', u'3', u'3', u'0', u'3', u'0', u'4', u'0', u'0', u'3', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'3', u'0', u'0', u'3', u'0', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'1', u'0', u'1', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'8', u'0', u'2', u'8', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'2', u'0', u'1', u'2', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'0', u'0', u'1', u'0', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'3', u'1', u'1', u'3', u'1', u'1', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'6', u'0', u'2', u'6', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'7', u'1', u'5', u'0', u'7', u'1', u'5', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'8', u'2', u'0', u'1', u'5', u'8', u'2', u'0', u'1', u'5', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'2', u'0', u'2', u'0', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'0', u'1', u'0', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'5', u'0', u'0', u'5', u'0', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'5', u'1', u'6', u'0', u'5', u'1', u'6', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'1', u'1', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'2', u'0', u'1', u'6', u'1', u'0', u'4', u'2', u'0', u'1', u'6', u'1', u'0', u'4', u'2', u'0', u'1', u'6', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'6', u'9', u'1', u'6', u'9', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'0', u'1', u'0', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'4', u'0', u'2', u'4', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'1', u'0', u'1', u'1', u'0', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'3', u'2', u'0', u'3', u'2', u'0', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'1', u'6', u'1', u'1', u'6', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'5', u'3', u'1', u'5', u'3', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'2', u'0', u'1', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'0', u'6', u'0', u'0', u'6', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'2', u'0', u'2', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'9', u'5', u'0', u'9', u'5', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'2', u'0', u'2', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'2', u'0', u'2', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'2', u'0', u'2', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'1', u'1', u'1', u'1', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'2', u'0', u'2', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'2', u'0', u'2', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'2', u'0', u'1', u'2', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'4', u'0', u'1', u'8', u'4', u'0', u'1', u'8', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'8', u'0', u'1', u'8', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'1', u'0', u'1', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'0', u'2', u'3', u'0', u'2', u'3', u'2', u'0', u'1', u'6', u'0', u'9', u'2', u'0', u'1', u'3', u'1', u'1', u'3', u'1', u'3', u'2', u'1', u'6', u'6', u'6', u'0', u'2', u'2', u'2', u'0', u'3', u'3', u'3', u'1', u'9', u'9', u'0', u'2', u'0', u'1', u'6', u'1', u'0', u'1', u'5', u'5', u'9', u'6', u'1', u'9', u'1', u'1', u'1', u'3', u'2', u'2', u'6', u'6', u'3', u'4', u'4', u'0', u'0', u'1', u'1', u'1', u'1', u'1', u'1', u'0', u'0', u'2', u'3', u'4']
>>> re.findall('[0-9]+', text)
[u'1', u'0', u'8', u'3', u'1', u'0', u'3', u'1', u'1', u'3', u'1999', u'8', u'40', u'40', u'4', u'04', u'4', u'7', u'09', u'3', u'1', u'1', u'0', u'1', u'2', u'0', u'3', u'0', u'3', u'3', u'3', u'3', u'40', u'3', u'40', u'66150', u'513504', u'15', u'4', u'4', u'3', u'3', u'3', u'16', u'16', u'16', u'16', u'1', u'1', u'89037', u'66150', u'513504', u'0', u'30', u'4', u'0', u'30', u'4', u'0', u'3', u'3', u'0', u'30', u'4', u'0', u'0301', u'2016', u'09', u'20', u'0', u'3', u'0', u'0', u'3', u'0', u'2016', u'09', u'20', u'0', u'1', u'1', u'0', u'1', u'1', u'2016', u'09', u'20', u'0', u'2', u'8', u'0', u'2', u'8', u'2016', u'09', u'20', u'0', u'1', u'0', u'1', u'2016', u'09', u'20', u'2', u'0', u'1', u'2', u'0', u'1', u'2016', u'09', u'20', u'0', u'1', u'0', u'0', u'1', u'0', u'2016', u'09', u'20', u'3', u'1', u'1', u'3', u'1', u'1', u'2', u'2016', u'09', u'20', u'0', u'2', u'6', u'0', u'2', u'6', u'2016', u'09', u'20', u'0', u'7', u'15', u'0', u'7', u'15', u'2016', u'09', u'20', u'8', u'20', u'15', u'8', u'20', u'15', u'2016', u'09', u'20', u'2', u'0', u'2', u'0', u'2016', u'09', u'20', u'0', u'0', u'1', u'0', u'0', u'1', u'2016', u'09', u'20', u'0', u'5', u'0', u'0', u'5', u'0', u'2016', u'09', u'20', u'0', u'5', u'16', u'0', u'5', u'16', u'2016', u'09', u'20', u'1', u'1', u'1', u'1', u'2016', u'09', u'20', u'2016', u'1', u'0', u'4', u'2016', u'1', u'0', u'4', u'2016', u'2016', u'09', u'20', u'1', u'6', u'9', u'1', u'6', u'9', u'2016', u'09', u'20', u'0', u'0', u'1', u'0', u'0', u'1', u'2016', u'09', u'20', u'0', u'2', u'4', u'0', u'2', u'4', u'2016', u'09', u'20', u'1', u'1', u'0', u'1', u'1', u'0', u'2016', u'09', u'20', u'3', u'2', u'0', u'3', u'2', u'0', u'2016', u'09', u'20', u'1', u'1', u'6', u'1', u'1', u'6', u'2016', u'09', u'20', u'0', u'1', u'0', u'1', u'2016', u'09', u'20', u'1', u'5', u'3', u'1', u'5', u'3', u'2016', u'09', u'20', u'0', u'12', u'0', u'12', u'2016', u'09', u'20', u'0', u'0', u'6', u'0', u'0', u'6', u'2016', u'09', u'20', u'0', u'2', u'2', u'0', u'2', u'2', u'2016', u'09', u'20', u'0', u'9', u'5', u'0', u'9', u'5', u'2016', u'09', u'20', u'0', u'2', u'2', u'0', u'2', u'2', u'2016', u'09', u'20', u'0', u'2', u'2', u'0', u'2', u'2', u'2016', u'09', u'20', u'0', u'2', u'2', u'0', u'2', u'2', u'2016', u'09', u'20', u'1', u'1', u'1', u'1', u'1', u'1', u'2016', u'09', u'20', u'0', u'2', u'2', u'0', u'2', u'2', u'2016', u'09', u'20', u'0', u'2', u'2', u'0', u'2', u'2', u'2016', u'09', u'20', u'0', u'1', u'2', u'0', u'1', u'2', u'2016', u'09', u'20', u'4', u'0', u'18', u'4', u'0', u'18', u'2016', u'09', u'20', u'0', u'1', u'8', u'0', u'1', u'8', u'2016', u'09', u'20', u'0', u'1', u'0', u'1', u'2016', u'09', u'20', u'0', u'2', u'3', u'0', u'2', u'3', u'2016', u'09', u'20', u'1', u'3', u'1', u'1', u'3', u'1', u'3', u'2', u'1', u'6', u'6', u'6', u'0', u'2', u'2', u'2', u'0', u'3', u'3', u'3', u'1990', u'2016', u'1', u'0', u'1', u'55961911', u'1', u'3', u'2', u'2', u'66', u'3', u'4', u'4', u'0', u'0', u'1', u'1', u'1', u'1', u'1', u'1', u'0', u'0', u'234']
>>> 
========= RESTART: /Users/mike/teaching/2016-09-19/get_pypi_count.py =========
>>> count
[]
>>> 
========= RESTART: /Users/mike/teaching/2016-09-19/get_pypi_count.py =========
[u'There are currently\n<strong>89041</strong>\npackages here']
>>> 
========= RESTART: /Users/mike/teaching/2016-09-19/get_pypi_count.py =========
[u'1']
>>> 
========= RESTART: /Users/mike/teaching/2016-09-19/get_pypi_count.py =========
[u'89041']
>>> 
========= RESTART: /Users/mike/teaching/2016-09-19/get_pypi_count.py =========
[u'89041']
>>> 
========= RESTART: /Users/mike/teaching/2016-09-19/get_pypi_count.py =========
[u'89041']
>>> 
========= RESTART: /Users/mike/teaching/2016-09-19/get_pypi_count.py =========
[u'89041']
>>> 
========= RESTART: /Users/mike/teaching/2016-09-19/get_pypi_count.py =========
89041
>>> re.findall('eio', 'aeiou')
['eio']
>>> re.findall('^eio', 'aeiou')
[]
>>> re.findall('^aei', 'aeiou')
['aei']
>>> re.findall('.', 'aeiou')
['a', 'e', 'i', 'o', 'u']
>>> re.findall('.*', 'aeiou')
['aeiou', '']
>>> re.findall('.+', 'aeiou')
['aeiou']
>>> re.findall('.^', 'aeiou')
[]
>>> re.findall('.$', 'aeiou')
['u']
>>> re.findall('..$', 'aeiou')
['ou']
>>> re.findall('$.', 'aeiou')
[]
>>> re.findall('[a-q]', 'aeiou')
['a', 'e', 'i', 'o']
>>> re.findall('[a-m]', 'aeiou')
['a', 'e', 'i']
>>> re.findall('[^a-m]', 'aeiou')
['o', 'u']
>>> re.findall('[^a-u]', 'aei-ou')
['-']
>>> re.findall('[a-u]', 'aei-ou')
['a', 'e', 'i', 'o', 'u']
>>> re.findall('[a\-u]', 'aei-ou')
['a', '-', 'u']
>>> re.findall(r'[a\-u]', 'aei-ou')
['a', '-', 'u']
>>> re.findall('\\', 'a literal \\ backslash')

Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    re.findall('\\', 'a literal \\ backslash')
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/re.py", line 181, in findall
    return _compile(pattern, flags).findall(string)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/re.py", line 251, in _compile
    raise error, v # invalid expression
error: bogus escape (end of line)
>>> re.findall('\\\\', 'a literal \\ backslash')
['\\']
>>> re.findall(r'\\', 'a literal \\ backslash')
['\\']
>>> 
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> str.find
<method 'find' of 'str' objects>
>>> help(str.find)
Help on method_descriptor:

find(...)
    S.find(sub [,start [,end]]) -> int
    
    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Return -1 on failure.

>>> i = 'aeiou'.find('z')
>>> 'aeiou'[i] == 'z'
False
>>> 
>>> help(str.index)
Help on method_descriptor:

index(...)
    S.index(sub [,start [,end]]) -> int
    
    Like S.find() but raise ValueError when the substring is not found.

>>> help(re.search)
Help on function search in module re:

search(pattern, string, flags=0)
    Scan through string looking for a match to the pattern, returning
    a match object, or None if no match was found.

>>> try:
	raise RuntimeError
except RuntimeError:
	print 'caught ya'

	
caught ya
>>> 
>>> # lunch until 1:10pm
>>> 
>>> import subprocess
>>> subprocess.call('ls')
0
>>> output = subprocess.check_output('ls')
>>> output
'Blain.Marilyn.png\nBlain.Marilyn.vcf\nDavis.Harold.png\nDavis.Harold.vcf\nGunter.Fritz.png\nGunter.Fritz.vcf\nHettinger.Raymond.png\nHettinger.Raymond.vcf\nJones.David.png\nJones.David.vcf\nMarks.Blair.png\nMarks.Blair.vcf\nMasterson.Martin.png\nMasterson.Martin.vcf\nPichon.Esmerela.png\nPichon.Esmerela.vcf\nSchmidt.Gertrude.png\nSchmidt.Gertrude.vcf\nThomas.Mary.png\nThomas.Mary.vcf\nZapata.Luis.png\nZapata.Luis.vcf\n__pycache__\nbrief.py\ncounting_urls.py\nday1.idle.py\nday1a.idle.py\nday2.idle.py\ndownload.py\nexample.py\nexample.txt\nget_pypi_count.py\nhighlight.py\nhighlight.pyc\nlinks.txt\nlogo.py\nnotes\npublish.py\nvcard.py\nvcard.pyc\n'
>>> command = 'ls -al'.split()
>>> output = subprocess.check_output(command)
>>> command
['ls', '-al']
>>> argv = 'ls -al'.split()
>>> argv
['ls', '-al']
>>> # output = subprocess.check_output('dir', shell=True)
>>> import os
>>> os.listdir
<built-in function listdir>
>>> import shutil
>>> subprocess.Popen
<class 'subprocess.Popen'>
>>> output = subprocess.check_output('ls -al')

Traceback (most recent call last):
  File "<pyshell#254>", line 1, in <module>
    output = subprocess.check_output('ls -al')
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/subprocess.py", line 567, in check_output
    process = Popen(stdout=PIPE, *popenargs, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/subprocess.py", line 711, in __init__
    errread, errwrite)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/subprocess.py", line 1343, in _execute_child
    raise child_exception
OSError: [Errno 2] No such file or directory
>>> 
>>> 
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/example.py ============
hello world!

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/example.py", line 4, in <module>
    print os.argv
AttributeError: 'module' object has no attribute 'argv'
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/example.py ============
hello world!
['/Users/mike/teaching/2016-09-19/example.py']
>>> 
>>> 
>>> import argparse
>>> # use argparse to create a nice CLI quickly
>>> 
>>> 
>>> 
>>> # 4 core collections in Python
>>> list
<type 'list'>
>>> dict, set, tuple
(<type 'dict'>, <type 'set'>, <type 'tuple'>)
>>> 
>>> 
>>> # dict is short for "dictionary"
>>> 
>>> letters = ['a', 'b', 'z']
>>> letters[0]
'a'
>>> letters[1]
'b'
>>> letters[2]
'z'
>>> letters = [None, 'a', 'b', 'z']
>>> letters[1]
'a'
>>> letters[2]
'b'
>>> len(letters)
4
>>> 
>>> letters = {1: 'a', 2: 'b', 26: 'z'}
>>> letters[1]
'a'
>>> letters[2]
'b'
>>> letters[26]
'z'
>>> len(letters)
3
>>> # good data types for dict keys: int or str, or tuples of int/str
>>> 2.51235
2.51235
>>> 2.51234
2.51234
>>> 
>>> {'a': 1, 'b': 2, 'c': 3} # dict is a collection of (key, value) pairs
{'a': 1, 'c': 3, 'b': 2}
>>> 
>>> {'a': 1, 'b': 2, 'c': 3}
{'a': 1, 'c': 3, 'b': 2}
>>> {'a': 1, 'b': 2, 'c': 3}
{'a': 1, 'c': 3, 'b': 2}
>>> {'a': 1, 'b': 2, 'c': 3}
{'a': 1, 'c': 3, 'b': 2}
>>> {'a': 1, 'b': 2, 'c': 3}
{'a': 1, 'c': 3, 'b': 2}
>>> 
>>> {'b': 20, 'c': 35, 'a': 1000}
{'a': 1000, 'c': 35, 'b': 20}
>>> 
>>> 
>>> # if you think of a dict as a real life dictionary, you'll usually be correct
>>> 
>>> # gobsmacked --> stunned into submission, not knowing how to respond
>>> # nonplussed --> stunned into submission, not knowing how to respond
>>> 
>>> # sillystriken --> stunned into submission ...
>>> # sillystriken --> stunned into submission, not knowing how to respond
>>> 
>>> 
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> 
>>> for thing in d:
	print thing

	
a
c
b
>>> for key in d:
	print key

	
a
c
b
>>> 'a' in d
True
>>> d['a']
1
>>> d['w']

Traceback (most recent call last):
  File "<pyshell#318>", line 1, in <module>
    d['w']
KeyError: 'w'
>>> name

Traceback (most recent call last):
  File "<pyshell#319>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> d.attribute

Traceback (most recent call last):
  File "<pyshell#320>", line 1, in <module>
    d.attribute
AttributeError: 'dict' object has no attribute 'attribute'
>>> d
{'a': 1, 'c': 3, 'b': 2}
>>> d.keys()
['a', 'c', 'b']
>>> d.values()
[1, 3, 2]
>>> 
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
>>> 
>>> d.keys()
['a', 'c', 'b']
>>> d.values()
[1, 3, 2]
>>> d.items()
[('a', 1), ('c', 3), ('b', 2)]
>>> d.item()

Traceback (most recent call last):
  File "<pyshell#331>", line 1, in <module>
    d.item()
AttributeError: 'dict' object has no attribute 'item'
>>> 
>>> d
{'a': 1, 'c': 3, 'b': 2}
>>> d['a']
1
>>> d['a'] = 10
>>> d
{'a': 10, 'c': 3, 'b': 2}
>>> del d['a']
>>> d
{'c': 3, 'b': 2}
>>> 
>>> d['a':'b']

Traceback (most recent call last):
  File "<pyshell#340>", line 1, in <module>
    d['a':'b']
TypeError: unhashable type
>>> 
>>> 
>>> words = {}
>>> words['nonplussed'] = 'stunned'
>>> definition = words['nonplussed']
>>> words['sillystricken'] = definition
>>> del words['nonplussed']
>>> 
>>> words
{'sillystricken': 'stunned'}
>>> 
>>> for value in words.values():
	if value == 'stunned':
		print 'found it'

		
found it
>>> 
>>> d['a']

Traceback (most recent call last):
  File "<pyshell#356>", line 1, in <module>
    d['a']
KeyError: 'a'
>>> d
{'c': 3, 'b': 2}
>>> d['b']
2
>>> 'b' in d
True
>>> for key, value in words.items():
	if value == 'stunned':
		print 'found it', key

		
found it sillystricken
>>> 
>>> tuple
<type 'tuple'>
>>> 
>>> 
>>> 
>>> t = (1, 2, 3)
>>> 
>>> t[0]
1
>>> t[:2]
(1, 2)
>>> for element in t:
	print element

	
1
2
3
>>> 
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> t
(1, 2, 3)
>>> t[0]
1
>>> t[0] = 10

Traceback (most recent call last):
  File "<pyshell#379>", line 1, in <module>
    t[0] = 10
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> # typical usage patterns for list vs tuple
>>> 
>>> # lists tend to be used for looping over homogenous data
>>> # also, lists are used as stacks (LIFO) append/pop
>>> 
>>> # tuples tend to be used for individual records, often hetergenous data
>>> person = ('Mike', 'Boston', 33)
>>> people = [('Mike', 'Boston', 33), ('Raymond', 'San Jose', 0x33)]
>>> people
[('Mike', 'Boston', 33), ('Raymond', 'San Jose', 51)]
>>> 
>>> people[0] == person
True
>>> people[0] is person
False
>>> 
>>> d = {}
>>> 
>>> 
>>> a = [0, 1]
>>> b = [0, 1]
>>> 
>>> a == b
True
>>> a is b
False
>>> 
>>> a.append(2)
>>> a
[0, 1, 2]
>>> 
>>> d
{}
>>> d[a]

Traceback (most recent call last):
  File "<pyshell#408>", line 1, in <module>
    d[a]
TypeError: unhashable type: 'list'
>>> d[(0, 1)] = 'tuple works'
>>> d
{(0, 1): 'tuple works'}
>>> people = [('Mike', 'Boston', 33), ('Raymond', 'San Jose', 'male')]
>>> 
>>> 
>>> 
>>> set
<type 'set'>
>>> 
>>> 
>>> 
>>> word = 'abracadabra'
>>> 
>>> uniques = {}
>>> for c in word:
	uniques[c] = None

	
>>> uniques.keys()
['a', 'r', 'b', 'c', 'd']
>>> uniques
{'a': None, 'r': None, 'b': None, 'c': None, 'd': None}
>>> 
>>> set(word)
set(['a', 'r', 'b', 'c', 'd'])
>>> 
>>> 
>>> a = {1, 1, 1, 1}
>>> len(a)
1
>>> a
set([1])
>>> 
>>> {1, 1, 1} == {1}
True
>>> 
>>> a = {1, 2, 3}
>>> b = {3, 4, 5}
>>> 
>>> a.intersection(b)
set([3])
>>> a.union(b)
set([1, 2, 3, 4, 5])
>>> a - b
set([1, 2])
>>> b - a
set([4, 5])
>>> 
>>> allowed = {'testbed', 'devices'}
>>> keys = {'testbed', 'device'}
>>> keys < allowed
False
>>> keys <= allowed
False
>>> keys = {'testbed', 'devices'}
>>> keys <= allowed
True
>>> 
>>> a = {1, 2, 3}
>>> b = {4, 5, 6}
>>> a < b
False
>>> a > b
False
>>> a == b
False
>>> a.isdisjoint(b)
True
>>> 
>>> 
>>> a = {1, 2, 3, 4}
>>> b = {3, 4, 5, 6}
>>> 
>>> # all the people who are friendly AND wealthy
>>> # all the people who are friendly OR wealthy --> more people
>>> 
>>> a | b
set([1, 2, 3, 4, 5, 6])
>>> a & b
set([3, 4])
>>> 
>>> a.intersection(b)
set([3, 4])
>>> a.union(b)
set([1, 2, 3, 4, 5, 6])
>>> 
>>> 
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> 
>>> dir(list) - dir(tuple)

Traceback (most recent call last):
  File "<pyshell#476>", line 1, in <module>
    dir(list) - dir(tuple)
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> 
>>> [0, 1, 2] - ['hello']

Traceback (most recent call last):
  File "<pyshell#478>", line 1, in <module>
    [0, 1, 2] - ['hello']
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> set(dir(list)) - set(dir(tuple))
set(['sort', 'insert', '__reversed__', '__delslice__', 'reverse', 'extend', '__delitem__', '__setslice__', 'remove', '__setitem__', '__iadd__', 'pop', 'append', '__imul__'])
>>> sorted(set(dir(list)) - set(dir(tuple)))
['__delitem__', '__delslice__', '__iadd__', '__imul__', '__reversed__', '__setitem__', '__setslice__', 'append', 'extend', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> list, dict, set, tuple
(<type 'list'>, <type 'dict'>, <type 'set'>, <type 'tuple'>)
>>> 
>>> 
>>> # break until 2:22pm
>>> 
>>> 
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
ppp160.iadfw.net - - [01/Jul/1995:00:18:44 -0400] "GET /htbin/wais.pl HTTP/1.0" 200 308

sagami2.isc.meiji.ac.jp - - [01/Jul/1995:00:33:55 -0400] "GET /shuttle/resources/orbiters/endeavour-logo.gif HTTP/1.0" 200 5052

xyzzy.cts.com - - [01/Jul/1995:00:50:36 -0400] "GET /shuttle/missions/sts-71/images/KSC-95EC-0916.jpg HTTP/1.0" 200 34029

204.244.4.10 - - [01/Jul/1995:01:08:54 -0400] "GET /images/launch-logo.gif HTTP/1.0" 200 1713

freenet.edmonton.ab.ca - - [01/Jul/1995:01:30:09 -0400] "GET /shuttle/countdown/video/livevideo.jpeg HTTP/1.0" 200 45029

>>> line
'freenet.edmonton.ab.ca - - [01/Jul/1995:01:30:09 -0400] "GET /shuttle/countdown/video/livevideo.jpeg HTTP/1.0" 200 45029\n'
>>> line.split()[0]
'freenet.edmonton.ab.ca'
>>> line.split()
['freenet.edmonton.ab.ca', '-', '-', '[01/Jul/1995:01:30:09', '-0400]', '"GET', '/shuttle/countdown/video/livevideo.jpeg', 'HTTP/1.0"', '200', '45029']
>>> line
'freenet.edmonton.ab.ca - - [01/Jul/1995:01:30:09 -0400] "GET /shuttle/countdown/video/livevideo.jpeg HTTP/1.0" 200 45029\n'
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
ppp160.iadfw.net
sagami2.isc.meiji.ac.jp
xyzzy.cts.com
204.244.4.10
freenet.edmonton.ab.ca
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
['.net']
['.jp']
['.com']
[]
['.ca']
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
ppp160.iadfw.net ['.net']
sagami2.isc.meiji.ac.jp ['.jp']
xyzzy.cts.com ['.com']
204.244.4.10 []
freenet.edmonton.ab.ca ['.ca']
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
ppp160.iadfw.net net
sagami2.isc.meiji.ac.jp jp
xyzzy.cts.com com
204.244.4.10 com
freenet.edmonton.ab.ca ca
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/nasa.py", line 19, in <module>
    counts[tld] += 1
KeyError: 'net'
>>> line
'ppp160.iadfw.net - - [01/Jul/1995:00:18:44 -0400] "GET /htbin/wais.pl HTTP/1.0" 200 308\n'
>>> host
'ppp160.iadfw.net'
>>> tld
'net'
>>> counts
{}
>>> counts['net']

Traceback (most recent call last):
  File "<pyshell#496>", line 1, in <module>
    counts['net']
KeyError: 'net'
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/nasa.py", line 19, in <module>
    counts[tld] = counts[tld] + 1
KeyError: 'net'
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
>>> counts
{'com': 1, 'net': 1, 'jp': 1, 'ca': 1}
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
>>> counts
{'fi': 6, 'ch': 6, 'gr': 1, 'ca': 52, 'za': 2, 'cz': 2, 'au': 21, 'at': 3, 'edu': 213, 'cr': 1, 'ie': 3, 'es': 2, 'ru': 2, 'nl': 26, 'mil': 13, 'pt': 2, 'no': 8, 'lv': 1, 'nz': 4, 'net': 173, 'gov': 148, 'pl': 2, 'be': 5, 'fr': 6, 'dk': 1, 'hr': 1, 'de': 22, 'jp': 40, 'it': 8, 'br': 13, 'org': 12, 'sg': 2, 'my': 1, 'us': 8, 'uk': 46, 'com': 580, 'mx': 2, 'se': 11, 'il': 1}
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
>>> counts
{'gw': 1, 'gu': 1, 'ptl': 1, 'sci': 2, 'sandia': 5, 'rennes': 1, 'laitram': 1, 'global': 1, 'sca': 1, 'all': 1, 'ge': 2, 'nlr': 1, 'cfe': 1, 'tonsberg': 1, 'nwm': 3, 'osc': 3, 'osf': 1, 'cadvision': 1, 'umd': 1, 'ts': 1, 'ccnet': 2, 'tn': 1, 'aus': 1, 'aur': 1, 'tk': 1, 'ti': 3, 'tg': 1, 'teknikum': 1, 'tc': 2, 'spokpl': 1, 'vcv': 1, 'fishnet': 2, 'uncc': 1, 'axionet': 1, 'tacom': 1, 'fal': 1, 'worldbank': 1, 'skypoint': 1, 'saurus': 1, 'norfolk': 2, 'upf': 1, 'smc': 1, 'dia': 1, 'magnet': 1, 'p': 1, 'bangor': 1, 'dip': 1, 'caltech': 1, 'picker': 2, 'oche': 1, 'neste': 1, 'htl': 1, 'direct': 1, 'hti': 1, 'd': 2, 'hitachi': 1, 'rrz': 2, 'cesar': 1, 'cfr': 3, 'port': 1, 'znet': 1, 'dial': 4, 'chicago': 1, 'sun': 2, 'multimedia': 1, 'zrz': 1, 'access': 3, 'sprl': 1, 'vcr': 1, 'net': 8, 'termserv': 1, 'era': 1, 'alinc': 1, 'med': 3, 'kpnw': 1, 'vanderbilt': 1, 'leo': 1, 'lerc': 6, 'xnet': 2, 'singnet': 1, 'kersur': 1, 'celsiustech': 1, 'basf': 1, 'cybernet': 1, 'kema': 1, 'cts': 3, 'augustana': 1, 'usps': 2, 'boi': 1, 'cdev': 1, 'ctc': 1, 'drc': 1, 'oulu': 2, 'usafa': 1, 'golden': 1, 'powerup': 1, 'avionics': 3, 'unizh': 1, 'sgs': 1, 'ls': 1, 'omhq': 1, 'sgi': 9, 'austria': 1, 'pixi': 4, 'utrust': 1, 'compuserve': 45, 'buffnet': 1, 'gateway': 1, 'utmb': 1, 'usd': 1, 'usc': 1, 'che': 1, 'vlsi': 2, 'coastalnet': 2, 'cray': 1, 'fei': 1, 'corpcomm': 1, 'dny': 4, 'is': 3, 'mm': 1, 'nbnet': 2, 'olivetti': 1, 'srce': 1, 'demon': 13, 'econ': 1, 'nkn': 1, 'ritsumei': 1, 'cacd': 1, 'wvi': 1, 'dartmouth': 1, 'embratel': 11, 'jhuapl': 3, 'me': 1, 'ma': 2, 'mc': 1, 'azstarnet': 3, 'cas': 1, 'eclipse': 1, 'dev': 1, 'cat': 1, 'ere': 1, 'mv': 1, 'can': 1, 'den': 2, 'umbc': 1, 'flg': 1, 'cad': 4, 'nada': 1, 'nexus': 1, 'sps': 1, 'csustan': 1, 'wilmington': 1, 'niagara': 1, 'slip': 8, 'oswego': 1, 'pond': 1, 'ulaval': 1, 'spd': 1, 'ic': 1, 'csl': 1, 'afn': 1, 'csn': 1, 'rsoc': 1, 'uqac': 1, 'eng': 6, 'csd': 2, 'llnl': 2, 'fastlane': 2, 'isi': 1, 'shasta': 1, 'gate': 6, 'stir': 1, 'synopsys': 1, 'fs': 1, 'teleport': 7, 'max': 1, 'netvision': 1, 'hmpd': 1, 'lab': 1, 'npb': 1, 'internic': 2, 'maf': 1, 'fi': 1, 'arch': 1, 'alphen': 1, 'dorms': 2, 'boeing': 1, 'ripco': 1, 'telepac': 2, 'lawlib': 1, 'su': 1, 'kulnet': 1, 'fluent': 1, 'media': 1, 'wing': 1, 'nyc': 1, 'transarc': 1, 'vassar': 1, 'stpaul': 1, 'itc': 1, 'neta': 1, 'opec': 1, 'pacificrim': 1, 'barclays': 1, 'scott': 1, 'lss': 1, 'ssd': 1, 'itu': 1, 'nimh': 1, 'supernet': 1, 'le': 1, 'gte': 3, 'wis': 1, 'fiu': 2, 'sensemedia': 1, 'prodigy': 47, 'pci': 1, 'lr': 2, 'ipswichcity': 1, 'izmiran': 1, 'nimr': 1, 'tsr': 1, 'lmsc': 2, 'abacom': 1, 'cea': 1, 'cem': 1, 'resnet': 1, 'biomed': 1, 'das': 1, 'magic': 1, 'bas': 1, 'getnet': 1, 'unomaha': 1, 'dialip': 2, 'terraport': 1, 'kootenay': 1, 'dialin': 2, 'dbsoftware': 1, 'mbnet': 1, 'ee': 1, 'ed': 2, 'deepcove': 1, 'ec': 1, 'hlp': 1, 'coil': 2, 'connect': 1, 'ansaldo': 1, 'isltd': 1, 'shannon': 1, 'out': 3, 'rt': 1, 'gol': 2, 'gradient': 2, 'dsu': 2, 'rz': 1, 'research': 1, 'ftc': 1, 'compulink': 1, 'geol': 1, 'cwo': 1, 'rem': 1, 'iprolink': 1, 'unch': 1, 'ftn': 1, 'utcc': 1, 'ece': 2, 'cary': 1, 'ucdavis': 1, 'iaehv': 1, 'strata': 1, 'tntech': 1, 'orl': 11, 'proxy': 45, 'lausd': 1, 'artdes': 1, 'bwi': 2, 'sni': 1, 'tiac': 1, 'koo': 1, 'awod': 1, 'atm': 2, 'ups': 1, 'att': 5, 'phx': 5, 'stentor': 1, 'wln': 1, 'isc': 1, 'austin': 3, 'utdallas': 1, 'crim': 1, 'racsa': 1, 'bham': 3, 'pclink': 1, 'pgh': 2, 'gamewood': 1, 'cybernetics': 2, 'chevron': 2, 'npt': 2, 'onr': 1, 'calvacom': 1, 'open': 1, 'bluecrab': 1, 'cris': 2, 'city': 1, 'brussels': 1, 'bocaraton': 2, 'uky': 1, 'rrzn': 1, 'dfw': 2, 'iaf': 1, 'gpa': 1, 'bellcore': 1, 'dgim': 1, 'fmi': 3, 'pcshs': 1, 'biochem': 1, 'circa': 1, 'fmc': 1, 'ias': 1, 'iar': 1, 'jaxnet': 3, 'magec': 1, 'tec': 1, 'kaiwan': 1, 'et': 1, 'hursley': 3, 'sy': 2, 'cops': 1, 'netgate': 1, 'compserv': 1, 'gpu': 2, 'ncd': 1, 'center': 1, 'std': 1, 'b': 1, 'earthlink': 2, 'solidex': 1, 'stm': 2, 'halcyon': 2, 'nstn': 3, 'werple': 1, 'clemson': 1, 'tamu': 1, 'interactive': 1, 'exide': 1, 'nad': 1, 'algonet': 3, 'prl': 2, 'concordia': 1, 'oqa': 1, 'sas': 1, 'turner': 1, 'st': 4, 'lbl': 1, 'sat': 1, 'chem': 1, 'engin': 2, 'rmii': 1, 'aladdin': 1, 'perftech': 1, 'lit': 2, 'vnet': 1, 'skiles': 1, 'erinet': 1, 'mit': 3, 'intersource': 4, 'jsc': 9, 'bst': 1, 'who': 1, 'uclan': 1, 'sfo': 1, 'dialup': 3, 'sdsmt': 1, 'achilles': 1, 'visi': 1, 'zcu': 1, 'brookdale': 1, 'rogers': 1, 'dom': 1, 'aksi': 1, 'csranet': 1, 'lpl': 3, 'kw': 2, 'mhill': 1, 'lawt': 1, 'connectnet': 1, 'aecl': 2, 'physics': 1, 'microsoft': 2, 'urz': 2, 'pnl': 2, 'rmplc': 1, 'cdc': 1, 'lotus': 1, 'afit': 1, 'jpmorgan': 1, 'rtp': 1, 'ccds': 1, 'nevada': 1, 'atsc': 1, 'sron': 1, 'richmond': 1, 'quiknet': 1, 'fullerton': 1, 'westford': 1, 'polarnet': 1, 'ksc': 55, 'acns': 2, 'hip': 2, 'info': 3, 'irco': 1, 'erenj': 1, 'dc': 2, 'csra': 2, 'watson': 1, 'cpqd': 1, 'dv': 1, 'islandnet': 2, 'dt': 2, 'du': 3, 'chips': 2, 'ssc': 2, 'micronet': 1, 'oanet': 1, 'prima': 1, 'ucop': 1, 'emn': 1, 'metronet': 1, 'sdstate': 1, 'kuhp': 1, 'admins': 1, 'aei': 2, 'vincent': 1, 'crl': 6, 'bart': 1, 'rmt': 1, 'seas': 1, 'computek': 1, 'igeofcu': 1, 'emac': 2, 'arc': 3, 'btco': 1, 'ark': 2, 'sei': 1, 'aros': 1, 'bendnet': 1, 'vpro': 1, 'autometric': 1, 'swipnet': 2, 'torfree': 1, 'r': 1, 'myriad': 1, 'mtn': 1, 'iadfw': 4, 'ramlink': 1, 'kek': 1, 'ju': 1, 'jp': 2, 'inlink': 1, 'magi': 1, 'harvard': 1, 'wr': 1, 'magna': 1, 'bose': 1, 'jf': 2, 'wtk': 1, 'eecom': 1, 'koyote': 1, 'cos': 1, 'cor': 2, 'admin': 1, 's': 1, 'tridom': 1, 'coe': 1, 'iinet': 2, 'uni': 1, 'com': 6, 'visionware': 1, 'jeton': 1, 'ucs': 1, 'cl': 2, 'cc': 7, 'rdyne': 1, 'ca': 2, 'superlink': 1, 'amoco': 1, 'actrix': 1, 'cs': 12, 'li': 1, 'cv': 2, 'pr': 1, 'bbn': 1, 'tuc': 1, 'pt': 1, 'lycos': 1, 'dortmund': 1, 'pc': 1, 'pa': 5, 'pg': 1, 'pe': 1, 'dur': 1, 'pi': 3, 'po': 2, 'pm': 2, 'sanders': 2, 'firn': 1, 'mck': 1, 'netdepot': 1, 'mci': 1, 'nrc': 1, 'schuller': 1, 'telcom': 1, 'netcom': 1, 'gtetel': 1, 'shsu': 2, 'dfrc': 2, 'idirect': 2, 'artisoft': 1, 'atlanta': 1, 'ots': 1, 'ott': 1, 'smartlink': 1, 'aix': 1, 'knoware': 2, 'intr': 1, 'rutgers': 1, 'mordor': 1, 'coco': 1, 'ozemail': 3, 'statcan': 1, 'ix': 64, 'ctron': 1, 'jpl': 6, 'vf': 6, 'bcasd': 1, 'picky': 1, 'iu': 1, 'cpsc': 1, 'lfwc': 1, 'il': 1, 'in': 1, 'engr': 6, 'everyday': 1, 'asucla': 1, 'deagostini': 1, 'inc': 1, 'tksc': 1, 'nmhu': 2, 'estec': 3, 'hypercomp': 1, 'lava': 1, 'slac': 1, 'intercom': 1, 'deltanet': 2, 'mindspring': 2, 'voyager': 1, 'ibase': 1, 'nic': 1, 'ios': 1, 'syr': 1, 'iol': 3, 'ccit': 1, 'phr': 1, 'oit': 1, 'mech': 2, 'lib': 3, 'neural': 1, 'unl': 1, 'wolfe': 1, 'neptune': 1, 'trcinc': 1, 'ccs': 2, 'client': 1, 'sunnyvale': 1, 'pcnet': 1, 'ccd': 1, 'the': 1, 'nesusa': 1, 'ny': 2, 'mclean': 1, 'just': 1, 'mfg': 1, 'edmonton': 3, 'rbdc': 1, 'lds': 1, 'world': 1, 'co': 2, 'sasknet': 1, 'clipper': 2, 'fpl': 4, 'nas': 2, 'bnr': 3, 'xmission': 1, 'bell': 2, 'sky': 1, 'aloha': 1, 'uchc': 1, 'mitre': 2, 'haystack': 1, 'east': 1, 'ncifcrf': 2, 'telstra': 1, 'msfc': 5, 'mayo': 1, 'digital': 11, 'munich': 1, 'mot': 2, 'nando': 4, 'nve': 1, 'psy': 1, 'rns': 1, 'wantree': 1, 'shadow': 3, 'vim': 1, 'adams': 1, 'wellsfargo': 1, 'synoptics': 1, 'arcs': 1, 'nwscc': 1, 'orlando': 1, 'ncsa': 1, 'intex': 2, 'fnal': 1, 'almaden': 1, 'bekkoame': 3, 'onramp': 3, 'nildram': 1, 'leuven': 1, 'cisco': 1, 'hiwaay': 2, 'ascend': 2, 'tvs': 1, 'cyberport': 1, 'globalx': 1, 'lvld': 1, 'ols': 1, 'wwa': 1, 'entertv': 2, 'oikos': 1, 'star': 1, 'lycoming': 1, 'epix': 3, 'cnw': 1, 'cooper': 1, 'cns': 2, 'eel': 1, 'fcw': 1, 'hensa': 1, 'ak': 1, 'larc': 2, 'waikato': 1, 'ucsd': 1, 'esa': 1, 'ucsf': 1, 'ics': 2, 'gsfc': 20, 'tmn': 1, 'vianet': 1, 'hsc': 1, 'nmt': 1, 'compusmart': 1, 'ps': 4, 'seinf': 1, 'rug': 2, 'hsr': 1, 'bu': 1, 'corp': 1, 'async': 1, 'kiets': 1, 'acc': 1, 'on': 2, 'usa': 4, 'pfizer': 1, 'ocala': 1, 'plaza': 1, 'uibk': 1, 'acs': 2, 'infosphere': 1, 'iway': 2, 'magicnet': 2, 'nsi': 1, 'svskt': 1, 'tyrell': 1, 'csuchico': 1, 'marshall': 1, 'nsc': 2, 'cognet': 2, 'cellbio': 1, 'ppp': 4, 'cinenet': 2, 'next': 1, 'wistar': 1, 'van': 1, 'arcade': 1, 'housing': 1, 'innet': 1, 'eglin': 2, 'house': 1, 'wam': 1, 'accessus': 1, 'psychol': 2, 'didac': 1, 'kfunigraz': 1, 'bus': 1, 'eac': 1, 'hq': 1, 'xerox': 1, 'astro': 4, 'niehs': 1, 'kraft': 1, 'memphis': 1, 'wiscnet': 1, 'mtx': 1, 'uta': 1, 'interlink': 1, 'stanford': 5, 'iisc': 1, 'mts': 2, 'us': 1, 'asahi': 2, 'moneng': 1, 'esslink': 1, 'cit': 1, 'udel': 1, 'ug': 1, 'aa': 1, 'infinet': 1, 'ag': 2, 'ai': 1, 'indy': 1, 'lcar': 1, 'pic': 2, 'nnb': 2, 'pix': 1, 'grainger': 1, 'as': 1, 'av': 1, 'idbsu': 1, 'erie': 1, 'ericsson': 1, 'ciesin': 1, 'let': 1, 'nlnet': 1, 'cencom': 1, 'sna': 1, 'bellatlantic': 1, 'nb': 3, 'hoskyns': 1, 'amdahl': 1, 'gre': 1, 'newbridge': 1, 'ultranet': 1, 'ns': 1, 'nu': 1, 'amsinc': 1, 'phys': 2, 'phoenix': 2, 'annex': 3, 'org': 1, 'msus': 1, 'execpc': 4, 'seagate': 1, 'gecm': 1, 'corcom': 1, 'gower': 1, 'pool': 1, 'borland': 1, 'sasw': 1, 'telepost': 2, 'dow': 1, 'neosoft': 1, 'hns': 1, 'lsis': 1, 'u': 3, 'adam': 1, 'dvz': 1, 'whnf': 1, 'aramco': 1}
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
ppp160.iadfw.net net
sagami2.isc.meiji.ac.jp jp
xyzzy.cts.com com
freenet.edmonton.ab.ca ca
slip13.nb2.usu.edu edu
alyssa.prodigy.com com
ip-pdx4-06.teleport.com com
ttyb5.shasta.com com
nbdyn34.dip.csuchico.edu edu
ppp4.nildram.co.uk uk
an1.aros.net net
eve-2a.adam.com.au au
line12.the-spa.com com
pn020.p.chiba-u.ac.jp jp
www-b3.proxy.aol.com com
sopines206.nando.net net
athena.compulink.gr gr
slip183-5.kw.jp.ibm.net net
kentville-ts-16.nstn.ca ca
lrgw514098.lr.tudelft.nl nl
eic73.fiu.edu edu
dd13-026.compuserve.com com
dd01-016.compuserve.com com
murtaugh.crim.ca ca
pcjmk.ag.rl.ac.uk uk
crux.izmiran.rssi.ru ru
dawn14.cs.berkeley.edu edu
www-b6.proxy.aol.com com
sahp315.sandia.gov gov
d133.nnb.interaccess.com com
d133.nnb.interaccess.com com
ix-phx5-09.ix.netcom.com com
al088.du.pipex.com com
ix-orl1-18.ix.netcom.com com
rofpop28.infosphere.com com
port13.alphen.cistron.nl nl
lab8.pc.fsu.edu edu
lub13.onramp.net net
ix-den14-15.ix.netcom.com com
shuttle.gsfc.nasa.gov gov
richarms.demon.co.uk uk
phjpdr.phys.lsu.edu edu
midland-pp2.access.sinet.slb.com com
indy1.indy.net net
chaos.idirect.com com
h98-208.ccnet.com com
ds9.bellcore.com com
www-d3.proxy.aol.com com
redlight.mindspring.com com
ip136.flg.primenet.com com
slip164-136.on.ca.ibm.net net
ad04-041.compuserve.com com
xyplex1-1-19.intersource.com com
dialup513.chicago.mci.net net
ix-roc2-14.ix.netcom.com com
quinns.wvi.com com
isnet.is.wfu.edu edu
slip869.rmii.com com
gk-west.usps.gov gov
dialin33583.slip.nts.uci.edu edu
ip048.phx.primenet.com com
reggae.iinet.net.au au
ip161.phx.primenet.com com
bclyde.xnet.com com
dial9.irco.com com
lkf0178.deltanet.com com
yeti.didac-mip.fr fr
mailbox.rmplc.co.uk uk
lis3_p3.telepac.pt pt
dd11-017.compuserve.com com
ix-dc6-04.ix.netcom.com com
=============================== RESTART: Shell ===============================
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
ppp160.iadfw.net iadfw
sagami2.isc.meiji.ac.jp isc
xyzzy.cts.com cts
freenet.edmonton.ab.ca edmonton
slip13.nb2.usu.edu nb
alyssa.prodigy.com prodigy
ip-pdx4-06.teleport.com teleport
ttyb5.shasta.com shasta
nbdyn34.dip.csuchico.edu dip
ppp4.nildram.co.uk nildram
an1.aros.net aros
eve-2a.adam.com.au adam
line12.the-spa.com the
pn020.p.chiba-u.ac.jp p
www-b3.proxy.aol.com proxy
sopines206.nando.net nando
athena.compulink.gr compulink
slip183-5.kw.jp.ibm.net kw
kentville-ts-16.nstn.ca nstn
lrgw514098.lr.tudelft.nl lr
eic73.fiu.edu fiu
dd13-026.compuserve.com compuserve
dd01-016.compuserve.com compuserve
murtaugh.crim.ca crim

=============================== RESTART: Shell ===============================
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
>>> counts
{'fi': 6, 'ch': 6, 'gr': 1, 'ca': 52, 'za': 2, 'cz': 2, 'au': 21, 'at': 3, 'edu': 213, 'cr': 1, 'ie': 3, 'es': 2, 'ru': 2, 'nl': 26, 'mil': 13, 'pt': 2, 'no': 8, 'lv': 1, 'nz': 4, 'net': 173, 'gov': 148, 'pl': 2, 'be': 5, 'fr': 6, 'dk': 1, 'hr': 1, 'de': 22, 'jp': 40, 'it': 8, 'br': 13, 'org': 12, 'sg': 2, 'my': 1, 'us': 8, 'uk': 46, 'com': 580, 'mx': 2, 'se': 11, 'il': 1}
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 5, 6, 6, 6, 8, 8, 8, 11, 12, 13, 13, 21, 22, 26, 40, 46, 52, 148, 173, 213, 580]
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[1, 1, 1, 1, 1]
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[580, 213, 173, 148, 52]
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('za', 2), ('us', 8), ('uk', 46), ('sg', 2), ('se', 11)]
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('za', 2), ('us', 8), ('uk', 46), ('sg', 2), ('se', 11), ('ru', 2), ('pt', 2), ('pl', 2), ('org', 12), ('nz', 4), ('no', 8), ('nl', 26), ('net', 173), ('my', 1), ('mx', 2), ('mil', 13), ('lv', 1), ('jp', 40), ('it', 8), ('il', 1), ('ie', 3), ('hr', 1), ('gr', 1), ('gov', 148), ('fr', 6), ('fi', 6), ('es', 2), ('edu', 213), ('dk', 1), ('de', 22), ('cz', 2), ('cr', 1), ('com', 580), ('ch', 6), ('ca', 52), ('br', 13), ('be', 5), ('au', 21), ('at', 3)]
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
>>> counts.most_common(5)
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]
>>> 
>>> 
>>> line
'128.159.123.29 - - [28/Jul/1995:13:21:00 -0400] "GET /ksc.html HTTP/1.0" 200 7280\n'
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]
ppp160.iadfw.net - - [01/Jul/1995:00:18:44 -0400] "GET /htbin/wais.pl HTTP/1.0" 200 308

>>> line
'ppp160.iadfw.net - - [01/Jul/1995:00:18:44 -0400] "GET /htbin/wais.pl HTTP/1.0" 200 308\n'
>>> 
>>> 
>>> for i in range(5):
	print i

	
0
1
2
3
4
>>> for i in range(5):
	if i > 2:
		break
	print i

	
0
1
2
>>> for i in range(5):
	print i
	if i > 2:
		break

	
0
1
2
3
>>> for i in range(5):
	if i > 2:
		break
	print i

	
0
1
2
>>> 
>>> for i in range(5):
	if i == 1:
		continue
	if i > 2:
		break
	print i

	
0
2
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]
ppp160.iadfw.net - - [01/Jul/1995:00:18:44 -0400] "GET /htbin/wais.pl HTTP/1.0" 200 308

>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]

=============================== RESTART: Shell ===============================
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]
[]
>>> line
'ppp160.iadfw.net - - [01/Jul/1995:00:18:44 -0400] "GET /htbin/wais.pl HTTP/1.0" 200 308\n'
>>> pattern
'ppp160.iadfw.net - - [01/Jul/1995:00:18:44 -0400] "GET /htbin/wais.pl HTTP/1.0" 200 308'
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]
['ppp160.iadfw.net - - [01/Jul/1995:00:18:44 -0400] "GET /htbin/wais.pl HTTP/1.0" 200 308']
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]
['ppp160.iadfw.net - - [01/Jul/1995:00:18:44 -0400] "GET /htbin/wais.pl HTTP/1.0" 200 308']
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]
[('ppp160.iadfw.net', '01/Jul/1995:00:18:44 -0400', 'GET /htbin/wais.pl HTTP/1.0', '200', '308')]
>>> 
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]
>>> len(records)
1891
>>> records[-1]
('128.159.123.29', '28/Jul/1995:13:21:00 -0400', 'GET /ksc.html HTTP/1.0', '200', '7280')
>>> records[0]
('ppp160.iadfw.net', '01/Jul/1995:00:18:44 -0400', 'GET /htbin/wais.pl HTTP/1.0', '200', '308')
>>> 
>>> print r'C:\path\to\file'
C:\path\to\file
>>> print 'C:\\path\\to\\file'
C:\path\to\file
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]
>>> 
>>> 
>>> import collections
>>> import itertools
>>> 
>>> __builtins__
<module '__builtin__' (built-in)>
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs', 'all', 'any', 'apply', 'basestring', 'bin', 'bool', 'buffer', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'execfile', 'exit', 'file', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'long', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'raw_input', 'reduce', 'reload', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange', 'zip']
>>> 
>>> 
>>> sorted
<built-in function sorted>
>>> 
>>> 
>>> 
KeyboardInterrupt
>>> dasfdsfas (
	asdfsdaf

	adsfsa
KeyboardInterrupt
>>> 
>>> 
>>> 
>>> def foo():
	
SyntaxError: invalid syntax
>>> def foo():
	pass

>>> foo(1, 2)

Traceback (most recent call last):
  File "<pyshell#554>", line 1, in <module>
    foo(1, 2)
TypeError: foo() takes no arguments (2 given)
>>> 
>>> 
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
0
1
2
3
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
0 Luke
1 Leia
2 Han
3 Chewie
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
1 Luke
2 Leia
3 Han
4 Chewie
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
0 Luke
1 Leia
2 Han
3 Chewie
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
1 Luke
2 Leia
3 Han
4 Chewie
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
0 Luke
1 Leia
2 Han
3 Chewie
Luke
Chewie
Han
Leia
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
0 Luke
1 Leia
2 Han
3 Chewie

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/iteration.py", line 33, in <module>
    print names[i]
IndexError: list index out of range
>>> range(5)
[0, 1, 2, 3, 4]
>>> range(2, 5)
[2, 3, 4]
>>> range(5, 50, 10)
[5, 15, 25, 35, 45]
>>> range(50, 5, -10)
[50, 40, 30, 20, 10]
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
0 Luke
1 Leia
2 Han
3 Chewie
Chewie
Han
Leia
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
0 Luke
1 Leia
2 Han
3 Chewie
Chewie
Han
Leia
Luke
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
0 Luke
1 Leia
2 Han
3 Chewie
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
0 Luke
1 Leia
2 Han
3 Chewie
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
>>> 
>>> 
>>> for name in reversed(sorted(names)):
	print name

	
Luke
Leia
Han
Chewie
>>> for name in sorted(names, reversed=True):
	print name

	

Traceback (most recent call last):
  File "<pyshell#567>", line 1, in <module>
    for name in sorted(names, reversed=True):
TypeError: 'reversed' is an invalid keyword argument for this function
>>> for name in sorted(names, reverse=True):
	print name

	
Luke
Leia
Han
Chewie
>>> 
>>> word = 'abracadabra'
>>> set(word)
set(['a', 'r', 'b', 'c', 'd'])
>>> sorted(set(word))
['a', 'b', 'c', 'd', 'r']
>>> 
>>> names
['Luke', 'Leia', 'Han', 'Chewie']
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
0 Luke
1 Leia
2 Han
3 Chewie
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
0 Luke
1 Leia
2 Han
3 Chewie
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
Luke hero
Leia princess
Han pilot
Chewie copilot
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
0 Luke
1 Leia
2 Han
3 Chewie
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
Luke hero
Leia princess
Han pilot
Chewie copilot
Luke hero
Leia princess
Han pilot
Chewie copilot
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
0 Luke
1 Leia
2 Han
3 Chewie
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
Luke hero
Leia princess
Han pilot
Chewie copilot
Luke hero
Leia princess
Han pilot
Chewie copilot
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Darth
Luke
Leia
Han
Chewie
Darth
0 Luke
1 Leia
2 Han
3 Chewie
4 Darth
0 Luke
1 Leia
2 Han
3 Chewie
4 Darth
Darth
Chewie
Han
Leia
Luke
Darth
Chewie
Han
Leia
Luke
Chewie
Darth
Han
Leia
Luke
Luke hero
Leia princess
Han pilot
Chewie copilot
Darth

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/iteration.py", line 50, in <module>
    print names[i], roles[i]
IndexError: list index out of range
>>> 
>>> for name, role in zip(names, roles):
	print name, role

	
Luke hero
Leia princess
Han pilot
Chewie copilot
>>> 
>>> zip(names, roles)
[('Luke', 'hero'), ('Leia', 'princess'), ('Han', 'pilot'), ('Chewie', 'copilot')]
>>> 
>>> dict(zip(names, roles))
{'Luke': 'hero', 'Leia': 'princess', 'Han': 'pilot', 'Chewie': 'copilot'}
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Darth
Luke
Leia
Han
Chewie
Darth
0 Luke
1 Leia
2 Han
3 Chewie
4 Darth
0 Luke
1 Leia
2 Han
3 Chewie
4 Darth
Darth
Chewie
Han
Leia
Luke
Darth
Chewie
Han
Leia
Luke
Chewie
Darth
Han
Leia
Luke
Luke hero
Leia princess
Han pilot
Chewie copilot
Darth

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/iteration.py", line 50, in <module>
    print names[i], roles[i]
IndexError: list index out of range
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
0 Luke
1 Leia
2 Han
3 Chewie
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
Luke hero
Leia princess
Han pilot
Chewie copilot
Luke hero
Leia princess
Han pilot
Chewie copilot

4
4
3
6
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
0 Luke
1 Leia
2 Han
3 Chewie
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
Luke hero
Leia princess
Han pilot
Chewie copilot
Luke hero
Leia princess
Han pilot
Chewie copilot

4
4
3
6

[4, 4, 3, 6]
>>> 
>>> lengths
[4, 4, 3, 6]
>>> 
>>> len
<built-in function len>
>>> 
>>> x = len
>>> x
<built-in function len>
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
0 Luke
1 Leia
2 Han
3 Chewie
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
Luke hero
Leia princess
Han pilot
Chewie copilot
Luke hero
Leia princess
Han pilot
Chewie copilot

4
4
3
6

[4, 4, 3, 6]

>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
Luke
Leia
Han
Chewie
0 Luke
1 Leia
2 Han
3 Chewie
0 Luke
1 Leia
2 Han
3 Chewie
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
Chewie
Han
Leia
Luke
Luke hero
Leia princess
Han pilot
Chewie copilot
Luke hero
Leia princess
Han pilot
Chewie copilot

4
4
3
6

[4, 4, 3, 6]

[4, 4, 3, 6]
>>> 
>>> 
>>> map(len, names)
[4, 4, 3, 6]
>>> zip(names, map(len, names))
[('Luke', 4), ('Leia', 4), ('Han', 3), ('Chewie', 6)]
>>> dict(zip(names, map(len, names)))
{'Luke': 4, 'Leia': 4, 'Han': 3, 'Chewie': 6}
>>> 
>>> 
>>> sorted(names)
['Chewie', 'Han', 'Leia', 'Luke']
>>> 
>>> names = ['chewie', 'leia', 'Luke', 'Han']
>>> sorted(names)
['Han', 'Luke', 'chewie', 'leia']
>>> 
>>> 
>>> # Schwartzian Transform
>>> map(len, names)
[6, 4, 4, 3]
>>> zip(map(len, names), names)
[(6, 'chewie'), (4, 'leia'), (4, 'Luke'), (3, 'Han')]
>>> sorted(zip(map(len, names), names))
[(3, 'Han'), (4, 'Luke'), (4, 'leia'), (6, 'chewie')]
>>> 
>>> 
>>> sorted(names, key=len)
['Han', 'leia', 'Luke', 'chewie']
>>> sorted(names, key=str.lower)
['chewie', 'Han', 'leia', 'Luke']
>>> 
>>> len(names) == len(roles)
True
>>> 
>>> import tkinter

Traceback (most recent call last):
  File "<pyshell#615>", line 1, in <module>
    import tkinter
ImportError: No module named tkinter
>>> import Tkinter
>>> root = Tkinter.Tk()
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> import xml
>>> xml
<module 'xml' from '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/xml/__init__.pyc'>
>>> dir(xml)
['_MINIMUM_XMLPLUS_VERSION', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__']
>>> xml.__file__
'/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/xml/__init__.pyc'
>>> 
>>> import xml.etree
>>> xml
<module 'xml' from '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/xml/__init__.pyc'>
>>> xml.etreee

Traceback (most recent call last):
  File "<pyshell#627>", line 1, in <module>
    xml.etreee
AttributeError: 'module' object has no attribute 'etreee'
>>> xml.etree
<module 'xml.etree' from '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/xml/etree/__init__.pyc'>
>>> 
>>> from xml.etree import ElementTree
>>> ElementTree
<module 'xml.etree.ElementTree' from '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/xml/etree/ElementTree.pyc'>
>>> 
>>> 
>>> 
>>> ElementTree.parse
<function parse at 0x103a7d8c0>
>>> tree = ElementTree.parse('notes/books.xml')
>>> 
>>> tree
<xml.etree.ElementTree.ElementTree object at 0x103a60190>
>>> type(tree)
<class 'xml.etree.ElementTree.ElementTree'>
>>> 
>>> catalog = tree.getroot()
>>> catlog

Traceback (most recent call last):
  File "<pyshell#642>", line 1, in <module>
    catlog
NameError: name 'catlog' is not defined
>>> catalog
<Element 'catalog' at 0x103a80490>
>>> catalog.text
'\n   '
>>> for child in catalog:
	print child

	
<Element 'book' at 0x103a804d0>
<Element 'book' at 0x103a808d0>
<Element 'book' at 0x103a80a90>
<Element 'book' at 0x103a80c50>
<Element 'book' at 0x103a80e10>
<Element 'book' at 0x103a80fd0>
<Element 'book' at 0x103a891d0>
<Element 'book' at 0x103a89390>
<Element 'book' at 0x103a89550>
<Element 'book' at 0x103a89710>
<Element 'book' at 0x103a898d0>
<Element 'book' at 0x103a89a90>
>>> for book in catalog.findall('book'):
	print book

	
<Element 'book' at 0x103a804d0>
<Element 'book' at 0x103a808d0>
<Element 'book' at 0x103a80a90>
<Element 'book' at 0x103a80c50>
<Element 'book' at 0x103a80e10>
<Element 'book' at 0x103a80fd0>
<Element 'book' at 0x103a891d0>
<Element 'book' at 0x103a89390>
<Element 'book' at 0x103a89550>
<Element 'book' at 0x103a89710>
<Element 'book' at 0x103a898d0>
<Element 'book' at 0x103a89a90>
>>> 
>>> 
>>> book
<Element 'book' at 0x103a89a90>
>>> 
>>> 
>>> 
========= RESTART: /Users/mike/teaching/2016-09-19/show_books_xml.py =========
<Element 'book' at 0x103a6cf10>
<Element 'book' at 0x103a733d0>
<Element 'book' at 0x103a73590>
<Element 'book' at 0x103a73750>
<Element 'book' at 0x103a73910>
<Element 'book' at 0x103a73ad0>
<Element 'book' at 0x103a73c90>
<Element 'book' at 0x103a73e50>
<Element 'book' at 0x103a82050>
<Element 'book' at 0x103a82210>
<Element 'book' at 0x103a823d0>
<Element 'book' at 0x103a82590>
>>> 
>>> book
<Element 'book' at 0x103a82590>
>>> book.text
'\n      '
>>> for child in book:
	print child

	
<Element 'author' at 0x103a825d0>
<Element 'title' at 0x103a82610>
<Element 'genre' at 0x103a82650>
<Element 'price' at 0x103a82690>
<Element 'publish_date' at 0x103a826d0>
<Element 'description' at 0x103a82710>
>>> 
>>> book['id']

Traceback (most recent call last):
  File "<pyshell#663>", line 1, in <module>
    book['id']
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/xml/etree/ElementTree.py", line 266, in __getitem__
    return self._children[index]
TypeError: list indices must be integers, not str
>>> book[0]
<Element 'author' at 0x103a825d0>
>>> book.get('id')
'bk112'
>>> 
>>> 
>>> 
========= RESTART: /Users/mike/teaching/2016-09-19/show_books_xml.py =========
Microsoft .NET: The Programming Bible
>>> 
========= RESTART: /Users/mike/teaching/2016-09-19/show_books_xml.py =========
Microsoft .NET: The Programming Bible
>>> 
========= RESTART: /Users/mike/teaching/2016-09-19/show_books_xml.py =========
Microsoft .NET: The Programming Bible
214.4
>>> 
========= RESTART: /Users/mike/teaching/2016-09-19/show_books_xml.py =========
Microsoft .NET: The Programming Bible
214.4
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/brief_xml.py ===========
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/brief_xml.py ===========

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/brief_xml.py", line 9, in <module>
    for row in ins_api.findall('//ROW_interface'):
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/xml/etree/ElementTree.py", line 390, in findall
    return ElementPath.findall(self, path, namespaces)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/xml/etree/ElementPath.py", line 293, in findall
    return list(iterfind(elem, path, namespaces))
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/xml/etree/ElementPath.py", line 257, in iterfind
    raise SyntaxError("cannot use absolute path on element")
SyntaxError: cannot use absolute path on element
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/brief_xml.py ===========
<Element 'ROW_interface' at 0x103a73390>
<Element 'ROW_interface' at 0x103a73510>
<Element 'ROW_interface' at 0x103a73790>
<Element 'ROW_interface' at 0x103a73a10>
<Element 'ROW_interface' at 0x103a73c90>
<Element 'ROW_interface' at 0x103a73f10>
<Element 'ROW_interface' at 0x103a821d0>
<Element 'ROW_interface' at 0x103a82450>
<Element 'ROW_interface' at 0x103a826d0>
<Element 'ROW_interface' at 0x103a82950>
<Element 'ROW_interface' at 0x103a82bd0>
<Element 'ROW_interface' at 0x103a82e50>
<Element 'ROW_interface' at 0x103a8c110>
<Element 'ROW_interface' at 0x103a8c390>
<Element 'ROW_interface' at 0x103a8c610>
<Element 'ROW_interface' at 0x103a8c890>
<Element 'ROW_interface' at 0x103a8cb10>
<Element 'ROW_interface' at 0x103a8cd90>
<Element 'ROW_interface' at 0x103a96050>
<Element 'ROW_interface' at 0x103a962d0>
<Element 'ROW_interface' at 0x103a96550>
<Element 'ROW_interface' at 0x103a967d0>
<Element 'ROW_interface' at 0x103a96a50>
<Element 'ROW_interface' at 0x103a96cd0>
<Element 'ROW_interface' at 0x103a96f50>
<Element 'ROW_interface' at 0x103aa1210>
<Element 'ROW_interface' at 0x103aa1490>
<Element 'ROW_interface' at 0x103aa1710>
<Element 'ROW_interface' at 0x103aa1990>
<Element 'ROW_interface' at 0x103aa1c10>
<Element 'ROW_interface' at 0x103aa1e90>
<Element 'ROW_interface' at 0x103af1150>
<Element 'ROW_interface' at 0x103af13d0>
<Element 'ROW_interface' at 0x103af1650>
<Element 'ROW_interface' at 0x103af18d0>
<Element 'ROW_interface' at 0x103af1b50>
<Element 'ROW_interface' at 0x103af1dd0>
<Element 'ROW_interface' at 0x103afc090>
<Element 'ROW_interface' at 0x103afc310>
<Element 'ROW_interface' at 0x103afc590>
<Element 'ROW_interface' at 0x103afc810>
<Element 'ROW_interface' at 0x103afca90>
<Element 'ROW_interface' at 0x103afcd10>
<Element 'ROW_interface' at 0x103afcf90>
<Element 'ROW_interface' at 0x103b08250>
<Element 'ROW_interface' at 0x103b084d0>
<Element 'ROW_interface' at 0x103b08750>
<Element 'ROW_interface' at 0x103b089d0>
<Element 'ROW_interface' at 0x103b08c50>
<Element 'ROW_interface' at 0x103b08ed0>
<Element 'ROW_interface' at 0x103b13190>
<Element 'ROW_interface' at 0x103b13410>
<Element 'ROW_interface' at 0x103b13690>
<Element 'ROW_interface' at 0x103b13910>
<Element 'ROW_interface' at 0x103b13b90>
<Element 'ROW_interface' at 0x103b13e10>
<Element 'ROW_interface' at 0x103b1e0d0>
<Element 'ROW_interface' at 0x103b1e350>
<Element 'ROW_interface' at 0x103b1e5d0>
<Element 'ROW_interface' at 0x103b1e850>
<Element 'ROW_interface' at 0x103b1ead0>
<Element 'ROW_interface' at 0x103b1ed50>
<Element 'ROW_interface' at 0x103b1efd0>
<Element 'ROW_interface' at 0x103b29290>
<Element 'ROW_interface' at 0x103b29510>
<Element 'ROW_interface' at 0x103b29790>
<Element 'ROW_interface' at 0x103b29a10>
<Element 'ROW_interface' at 0x103b29c90>
<Element 'ROW_interface' at 0x103b29f10>
<Element 'ROW_interface' at 0x103b351d0>
<Element 'ROW_interface' at 0x103b35450>
<Element 'ROW_interface' at 0x103b356d0>
<Element 'ROW_interface' at 0x103b35950>
<Element 'ROW_interface' at 0x103b35bd0>
<Element 'ROW_interface' at 0x103b35e50>
<Element 'ROW_interface' at 0x103b41110>
<Element 'ROW_interface' at 0x103b41390>
<Element 'ROW_interface' at 0x103b41610>
<Element 'ROW_interface' at 0x103b41890>
<Element 'ROW_interface' at 0x103b41b10>
<Element 'ROW_interface' at 0x103b41d90>
<Element 'ROW_interface' at 0x103b4c050>
<Element 'ROW_interface' at 0x103b4c2d0>
<Element 'ROW_interface' at 0x103b4c550>
<Element 'ROW_interface' at 0x103b4c7d0>
<Element 'ROW_interface' at 0x103b4ca50>
<Element 'ROW_interface' at 0x103b4ccd0>
<Element 'ROW_interface' at 0x103b4cf50>
<Element 'ROW_interface' at 0x103b57210>
<Element 'ROW_interface' at 0x103b57490>
<Element 'ROW_interface' at 0x103b57710>
<Element 'ROW_interface' at 0x103b57990>
<Element 'ROW_interface' at 0x103b57c10>
<Element 'ROW_interface' at 0x103b57e90>
<Element 'ROW_interface' at 0x103b62150>
<Element 'ROW_interface' at 0x103b623d0>
<Element 'ROW_interface' at 0x103b62650>
<Element 'ROW_interface' at 0x103b628d0>
<Element 'ROW_interface' at 0x103b62b10>
<Element 'ROW_interface' at 0x103b62d90>
<Element 'ROW_interface' at 0x103b62fd0>
<Element 'ROW_interface' at 0x103b6e250>
<Element 'ROW_interface' at 0x103b6e490>
<Element 'ROW_interface' at 0x103b6e6d0>
<Element 'ROW_interface' at 0x103b6e910>
>>> 
<Element 'ROW_interface' at 0x103b7d450>
<Element 'ROW_interface' at 0x103b7d510>
<Element 'ROW_interface' at 0x103b7d850>
<Element 'ROW_interface' at 0x103b7dad0>
<Element 'ROW_interface' at 0x103b7dd50>
<Element 'ROW_interface' at 0x103b7df90>
<Element 'ROW_interface' at 0x103b8a250>
<Element 'ROW_interface' at 0x103b8a4d0>
<Element 'ROW_interface' at 0x103b8a750>
<Element 'ROW_interface' at 0x103b8a9d0>
<Element 'ROW_interface' at 0x103b8ac50>
<Element 'ROW_interface' at 0x103b8aed0>
<Element 'ROW_interface' at 0x103b95190>
<Element 'ROW_interface' at 0x103b95410>
<Element 'ROW_interface' at 0x103b95690>
<Element 'ROW_interface' at 0x103b95910>
<Element 'ROW_interface' at 0x103b95b90>
<Element 'ROW_interface' at 0x103b95e10>
<Element 'ROW_interface' at 0x103ba00d0>
<Element 'ROW_interface' at 0x103ba0350>
<Element 'ROW_interface' at 0x103ba05d0>
<Element 'ROW_interface' at 0x103ba0850>
<Element 'ROW_interface' at 0x103ba0ad0>
<Element 'ROW_interface' at 0x103ba0d50>
<Element 'ROW_interface' at 0x103ba0fd0>
<Element 'ROW_interface' at 0x103bab290>
<Element 'ROW_interface' at 0x103bab510>
<Element 'ROW_interface' at 0x103bab790>
<Element 'ROW_interface' at 0x103baba10>
<Element 'ROW_interface' at 0x103babc90>
<Element 'ROW_interface' at 0x103babf10>
<Element 'ROW_interface' at 0x103bb51d0>
<Element 'ROW_interface' at 0x103bb5450>
<Element 'ROW_interface' at 0x103bb56d0>
<Element 'ROW_interface' at 0x103bb5950>
<Element 'ROW_interface' at 0x103bb5bd0>
<Element 'ROW_interface' at 0x103bb5e50>
<Element 'ROW_interface' at 0x103bc2110>
<Element 'ROW_interface' at 0x103bc2390>
<Element 'ROW_interface' at 0x103bc2610>
<Element 'ROW_interface' at 0x103bc2890>
<Element 'ROW_interface' at 0x103bc2b10>
<Element 'ROW_interface' at 0x103bc2d90>
<Element 'ROW_interface' at 0x103bcd050>
<Element 'ROW_interface' at 0x103bcd2d0>
<Element 'ROW_interface' at 0x103bcd550>
<Element 'ROW_interface' at 0x103bcd7d0>
<Element 'ROW_interface' at 0x103bcda50>
<Element 'ROW_interface' at 0x103bcdcd0>
<Element 'ROW_interface' at 0x103bcdf50>
<Element 'ROW_interface' at 0x103bd8210>
<Element 'ROW_interface' at 0x103bd8490>
<Element 'ROW_interface' at 0x103bd8710>
<Element 'ROW_interface' at 0x103bd8990>
<Element 'ROW_interface' at 0x103bd8c10>
<Element 'ROW_interface' at 0x103bd8e90>
<Element 'ROW_interface' at 0x103be3150>
<Element 'ROW_interface' at 0x103be33d0>
<Element 'ROW_interface' at 0x103be3650>
<Element 'ROW_interface' at 0x103be38d0>
<Element 'ROW_interface' at 0x103be3b50>
<Element 'ROW_interface' at 0x103be3dd0>
<Element 'ROW_interface' at 0x103bee090>
<Element 'ROW_interface' at 0x103bee310>
<Element 'ROW_interface' at 0x103bee590>
<Element 'ROW_interface' at 0x103bee810>
<Element 'ROW_interface' at 0x103beea90>
<Element 'ROW_interface' at 0x103beed10>
<Element 'ROW_interface' at 0x103beef90>
<Element 'ROW_interface' at 0x103bfa250>
<Element 'ROW_interface' at 0x103bfa4d0>
<Element 'ROW_interface' at 0x103bfa750>
<Element 'ROW_interface' at 0x103bfa9d0>
<Element 'ROW_interface' at 0x103bfac50>
<Element 'ROW_interface' at 0x103bfaed0>
<Element 'ROW_interface' at 0x103c06190>
<Element 'ROW_interface' at 0x103c06410>
<Element 'ROW_interface' at 0x103c06690>
<Element 'ROW_interface' at 0x103c06910>
<Element 'ROW_interface' at 0x103c06b90>
<Element 'ROW_interface' at 0x103c06e10>
<Element 'ROW_interface' at 0x103c110d0>
<Element 'ROW_interface' at 0x103c11350>
<Element 'ROW_interface' at 0x103c115d0>
<Element 'ROW_interface' at 0x103c11850>
<Element 'ROW_interface' at 0x103c11ad0>
<Element 'ROW_interface' at 0x103c11d50>
<Element 'ROW_interface' at 0x103c11fd0>
=============================== RESTART: Shell ===============================
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/brief_xml.py ===========
<Element 'ROW_interface' at 0x103088390>
<Element 'ROW_interface' at 0x103088510>
<Element 'ROW_interface' at 0x103088790>
<Element 'ROW_interface' at 0x103088a10>
<Element 'ROW_interface' at 0x103088c90>
<Element 'ROW_interface' at 0x103088f10>
<Element 'ROW_interface' at 0x1030971d0>
<Element 'ROW_interface' at 0x103097450>
<Element 'ROW_interface' at 0x1030976d0>
<Element 'ROW_interface' at 0x103097950>
<Element 'ROW_interface' at 0x103097bd0>
<Element 'ROW_interface' at 0x103097e50>
<Element 'ROW_interface' at 0x1030a1110>
<Element 'ROW_interface' at 0x1030a1390>
<Element 'ROW_interface' at 0x1030a1610>
<Element 'ROW_interface' at 0x1030a1890>
<Element 'ROW_interface' at 0x1030a1b10>
<Element 'ROW_interface' at 0x1030a1d90>
<Element 'ROW_interface' at 0x1030ab050>
<Element 'ROW_interface' at 0x1030ab2d0>
<Element 'ROW_interface' at 0x1030ab550>
<Element 'ROW_interface' at 0x1030ab7d0>
<Element 'ROW_interface' at 0x1030aba50>
<Element 'ROW_interface' at 0x1030abcd0>
<Element 'ROW_interface' at 0x1030abf50>
<Element 'ROW_interface' at 0x1030b6210>
<Element 'ROW_interface' at 0x1030b6490>
<Element 'ROW_interface' at 0x1030b6710>
<Element 'ROW_interface' at 0x1030b6990>
<Element 'ROW_interface' at 0x1030b6c10>
<Element 'ROW_interface' at 0x1030b6e90>
<Element 'ROW_interface' at 0x1030c0150>
<Element 'ROW_interface' at 0x1030c03d0>
<Element 'ROW_interface' at 0x1030c0650>
<Element 'ROW_interface' at 0x1030c08d0>
<Element 'ROW_interface' at 0x1030c0b50>
<Element 'ROW_interface' at 0x1030c0dd0>
<Element 'ROW_interface' at 0x1030cb090>
<Element 'ROW_interface' at 0x1030cb310>
<Element 'ROW_interface' at 0x1030cb590>
<Element 'ROW_interface' at 0x1030cb810>
<Element 'ROW_interface' at 0x1030cba90>
<Element 'ROW_interface' at 0x1030cbd10>
<Element 'ROW_interface' at 0x1030cbf90>
<Element 'ROW_interface' at 0x1030d7250>
<Element 'ROW_interface' at 0x1030d74d0>
<Element 'ROW_interface' at 0x1030d7750>
<Element 'ROW_interface' at 0x1030d79d0>
<Element 'ROW_interface' at 0x1030d7c50>
<Element 'ROW_interface' at 0x1030d7ed0>
<Element 'ROW_interface' at 0x1030e2190>
<Element 'ROW_interface' at 0x1030e2410>
<Element 'ROW_interface' at 0x1030e2690>
<Element 'ROW_interface' at 0x1030e2910>
<Element 'ROW_interface' at 0x1030e2b90>
<Element 'ROW_interface' at 0x1030e2e10>
<Element 'ROW_interface' at 0x1030ed0d0>
<Element 'ROW_interface' at 0x1030ed350>
<Element 'ROW_interface' at 0x1030ed5d0>
<Element 'ROW_interface' at 0x1030ed850>
<Element 'ROW_interface' at 0x1030edad0>
<Element 'ROW_interface' at 0x1030edd50>
<Element 'ROW_interface' at 0x1030edfd0>
<Element 'ROW_interface' at 0x1030f8290>
<Element 'ROW_interface' at 0x1030f8510>
<Element 'ROW_interface' at 0x1030f8790>
<Element 'ROW_interface' at 0x1030f8a10>
<Element 'ROW_interface' at 0x1030f8c90>
<Element 'ROW_interface' at 0x1030f8f10>
<Element 'ROW_interface' at 0x10334a1d0>
<Element 'ROW_interface' at 0x10334a450>
<Element 'ROW_interface' at 0x10334a6d0>
<Element 'ROW_interface' at 0x10334a950>
<Element 'ROW_interface' at 0x10334abd0>
<Element 'ROW_interface' at 0x10334ae50>
<Element 'ROW_interface' at 0x103356110>
<Element 'ROW_interface' at 0x103356390>
<Element 'ROW_interface' at 0x103356610>
<Element 'ROW_interface' at 0x103356890>
<Element 'ROW_interface' at 0x103356b10>
<Element 'ROW_interface' at 0x103356d90>
<Element 'ROW_interface' at 0x103361050>
<Element 'ROW_interface' at 0x1033612d0>
<Element 'ROW_interface' at 0x103361550>
<Element 'ROW_interface' at 0x1033617d0>
<Element 'ROW_interface' at 0x103361a50>
<Element 'ROW_interface' at 0x103361cd0>
<Element 'ROW_interface' at 0x103361f50>
<Element 'ROW_interface' at 0x10336c210>
<Element 'ROW_interface' at 0x10336c490>
<Element 'ROW_interface' at 0x10336c710>
<Element 'ROW_interface' at 0x10336c990>
<Element 'ROW_interface' at 0x10336cc10>
<Element 'ROW_interface' at 0x10336ce90>
<Element 'ROW_interface' at 0x103377150>
<Element 'ROW_interface' at 0x1033773d0>
<Element 'ROW_interface' at 0x103377650>
<Element 'ROW_interface' at 0x1033778d0>
<Element 'ROW_interface' at 0x103377b10>
<Element 'ROW_interface' at 0x103377d90>
<Element 'ROW_interface' at 0x103377fd0>
<Element 'ROW_interface' at 0x103383250>
<Element 'ROW_interface' at 0x103383490>
<Element 'ROW_interface' at 0x1033836d0>
<Element 'ROW_interface' at 0x103383910>
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/brief_xml.py ===========
mgmt0
>>> 
====== RESTART: /Users/mike/teaching/2016-09-19/xml_with_namespaces.py ======
>>> 
>>> tree
<xml.etree.ElementTree.ElementTree object at 0x103a6c6d0>
>>> 
>>> rpc_reply
<Element '{urn:ietf:params:xml:ns:netconf:base:1.0}rpc-reply' at 0x103a6ced0>
>>> rpc_reply.tag
'{urn:ietf:params:xml:ns:netconf:base:1.0}rpc-reply'
>>> rpc_reply.find('data')
>>> rpc_reply.find('nf:data')

Traceback (most recent call last):
  File "<pyshell#674>", line 1, in <module>
    rpc_reply.find('nf:data')
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/xml/etree/ElementTree.py", line 363, in find
    return ElementPath.find(self, path, namespaces)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/xml/etree/ElementPath.py", line 285, in find
    return iterfind(elem, path, namespaces).next()
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/xml/etree/ElementPath.py", line 259, in iterfind
    token = next()
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/xml/etree/ElementPath.py", line 83, in xpath_tokenizer
    raise SyntaxError("prefix %r not found in prefix map" % prefix)
SyntaxError: prefix 'nf' not found in prefix map
>>> 
====== RESTART: /Users/mike/teaching/2016-09-19/xml_with_namespaces.py ======
>>> 
>>> rpc_reply.find('nf:data', ns)
<Element '{urn:ietf:params:xml:ns:netconf:base:1.0}data' at 0x103a6ef10>
>>> rpc_reply.find('nf:data/x:show', ns)
<Element '{http://www.cisco.com/nxos:1.0:if_manager}show' at 0x103a6ef50>
>>> 
====== RESTART: /Users/mike/teaching/2016-09-19/xml_with_namespaces.py ======

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/xml_with_namespaces.py", line 12, in <module>
    for address in rpc_reply.findall('.//x:eth_hw_addr'):
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/xml/etree/ElementTree.py", line 390, in findall
    return ElementPath.findall(self, path, namespaces)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/xml/etree/ElementPath.py", line 293, in findall
    return list(iterfind(elem, path, namespaces))
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/xml/etree/ElementPath.py", line 263, in iterfind
    selector.append(ops[token[0]](next, token))
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/xml/etree/ElementPath.py", line 119, in prepare_descendant
    token = next()
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/xml/etree/ElementPath.py", line 83, in xpath_tokenizer
    raise SyntaxError("prefix %r not found in prefix map" % prefix)
SyntaxError: prefix 'x' not found in prefix map
>>> 
====== RESTART: /Users/mike/teaching/2016-09-19/xml_with_namespaces.py ======
0050.5691.0032
0000.0000.0005
0000.0000.0005
0000.0000.0005
0000.0000.0005
0000.0000.0005
0000.0000.0005
0000.0000.0005
0000.0000.0005
0000.0000.0005
>>> 
====== RESTART: /Users/mike/teaching/2016-09-19/xml_with_namespaces.py ======
0050.5691.0032
0000.0000.0005
0000.0000.0005
0000.0000.0005
0000.0000.0005
0000.0000.0005
0000.0000.0005
0000.0000.0005
0000.0000.0005
0000.0000.0005
>>> 
======== RESTART: /Users/mike/teaching/2016-09-19/show_books_json.py ========
>>> json.load
<function load at 0x10325d938>
>>> help(json.load)
Help on function load in module json:

load(fp, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
    Deserialize ``fp`` (a ``.read()``-supporting file-like object containing
    a JSON document) to a Python object.
    
    If the contents of ``fp`` is encoded with an ASCII based encoding other
    than utf-8 (e.g. latin-1), then an appropriate ``encoding`` name must
    be specified. Encodings that are not ASCII based (such as UCS-2) are
    not allowed, and should be wrapped with
    ``codecs.getreader(fp)(encoding)``, or simply decoded to a ``unicode``
    object and passed to ``loads()``
    
    ``object_hook`` is an optional function that will be called with the
    result of any object literal decode (a ``dict``). The return value of
    ``object_hook`` will be used instead of the ``dict``. This feature
    can be used to implement custom decoders (e.g. JSON-RPC class hinting).
    
    ``object_pairs_hook`` is an optional function that will be called with the
    result of any object literal decoded with an ordered list of pairs.  The
    return value of ``object_pairs_hook`` will be used instead of the ``dict``.
    This feature can be used to implement custom decoders that rely on the
    order that the key and value pairs are decoded (for example,
    collections.OrderedDict will remember the order of insertion). If
    ``object_hook`` is also defined, the ``object_pairs_hook`` takes priority.
    
    To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``
    kwarg; otherwise ``JSONDecoder`` is used.

>>> 
======== RESTART: /Users/mike/teaching/2016-09-19/show_books_json.py ========
>>> 
>>> type(data)
<type 'dict'>
>>> 
>>> data.keys()
[u'bk103', u'bk102', u'bk101', u'bk107', u'bk106', u'bk105', u'bk104', u'bk109', u'bk108', u'bk110', u'bk111', u'bk112']
>>> 
>>> data['bk102']
{u'description': u'A former architect battles corporate zombies, \n      an evil sorceress, and her own childhood to become queen \n      of the world.', u'author': u'Ralls, Kim', u'price': 5.95, u'title': u'Midnight Rain', u'publish_date': u'2000-12-16', u'genre': u'Fantasy'}
>>> data['bk102']['price']
5.95
>>> type(data['bk102']['price'])
<type 'float'>
>>> 
======== RESTART: /Users/mike/teaching/2016-09-19/show_books_json.py ========
{"a": [10, 20, 30], "b": {"count": 42, "greetings": "hello"}}
>>> 
======== RESTART: /Users/mike/teaching/2016-09-19/show_books_json.py ========
{
  "a": [
    10, 
    20, 
    30
  ], 
  "b": {
    "count": 42, 
    "greetings": "hello"
  }
}
>>> 
======== RESTART: /Users/mike/teaching/2016-09-19/show_books_json.py ========
{
  "a": [
    10, 
    20, 
    30
  ], 
  "b": {
    "count": 42, 
    "greetings": "hello"
  }
}
>>> 
>>> 
>>> data
{u'bk103': {u'description': u'After the collapse of a nanotechnology \n      society in England, the young survivors lay the \n      foundation for a new society.', u'author': u'Corets, Eva', u'price': 5.95, u'title': u'Maeve Ascendant', u'publish_date': u'2000-11-17', u'genre': u'Fantasy'}, u'bk102': {u'description': u'A former architect battles corporate zombies, \n      an evil sorceress, and her own childhood to become queen \n      of the world.', u'author': u'Ralls, Kim', u'price': 5.95, u'title': u'Midnight Rain', u'publish_date': u'2000-12-16', u'genre': u'Fantasy'}, u'bk101': {u'description': u'An in-depth look at creating applications \n      with XML.', u'author': u'Gambardella, Matthew', u'price': 44.95, u'title': u"XML Developer's Guide", u'publish_date': u'2000-10-01', u'genre': u'Computer'}, u'bk107': {u'description': u'A deep sea diver finds true love twenty \n      thousand leagues beneath the sea.', u'author': u'Thurman, Paula', u'price': 4.95, u'title': u'Splish Splash', u'publish_date': u'2000-11-02', u'genre': u'Romance'}, u'bk106': {u'description': u'When Carla meets Paul at an ornithology \n      conference, tempers fly as feathers get ruffled.', u'author': u'Randall, Cynthia', u'price': 4.95, u'title': u'Lover Birds', u'publish_date': u'2000-09-02', u'genre': u'Romance'}, u'bk105': {u'description': u"The two daughters of Maeve, half-sisters, \n      battle one another for control of England. Sequel to \n      Oberon's Legacy.", u'author': u'Corets, Eva', u'price': 5.95, u'title': u'The Sundered Grail', u'publish_date': u'2001-09-10', u'genre': u'Fantasy'}, u'bk104': {u'description': u'In post-apocalypse England, the mysterious \n      agent known only as Oberon helps to create a new life \n      for the inhabitants of London. Sequel to Maeve \n      Ascendant.', u'author': u'Corets, Eva', u'price': 5.95, u'title': u"Oberon's Legacy", u'publish_date': u'2001-03-10', u'genre': u'Fantasy'}, u'bk109': {u'description': u'After an inadvertant trip through a Heisenberg\n      Uncertainty Device, James Salway discovers the problems \n      of being quantum.', u'author': u'Kress, Peter', u'price': 6.95, u'title': u'Paradox Lost', u'publish_date': u'2000-11-02', u'genre': u'Science Fiction'}, u'bk108': {u'description': u'An anthology of horror stories about roaches,\n      centipedes, scorpions  and other insects.', u'author': u'Knorr, Stefan', u'price': 4.95, u'title': u'Creepy Crawlies', u'publish_date': u'2000-12-06', u'genre': u'Horror'}, u'bk110': {u'description': u"Microsoft's .NET initiative is explored in \n      detail in this deep programmer's reference.", u'author': u"O'Brien, Tim", u'price': 36.95, u'title': u'Microsoft .NET: The Programming Bible', u'publish_date': u'2000-12-09', u'genre': u'Computer'}, u'bk111': {u'description': u'The Microsoft MSXML3 parser is covered in \n      detail, with attention to XML DOM interfaces, XSLT processing, \n      SAX and more.', u'author': u"O'Brien, Tim", u'price': 36.95, u'title': u'MSXML3: A Comprehensive Guide', u'publish_date': u'2000-12-01', u'genre': u'Computer'}, u'bk112': {u'description': u'Microsoft Visual Studio 7 is explored in depth,\n      looking at how Visual Basic, Visual C++, C#, and ASP+ are \n      integrated into a comprehensive development \n      environment.', u'author': u'Galos, Mike', u'price': 49.95, u'title': u'Visual Studio 7: A Comprehensive Guide', u'publish_date': u'2001-04-16', u'genre': u'Computer'}}
>>> data.keys()
[u'bk103', u'bk102', u'bk101', u'bk107', u'bk106', u'bk105', u'bk104', u'bk109', u'bk108', u'bk110', u'bk111', u'bk112']
>>> for k in data:
	print k

	
bk103
bk102
bk101
bk107
bk106
bk105
bk104
bk109
bk108
bk110
bk111
bk112
>>> data.values()[:2]
[{u'description': u'After the collapse of a nanotechnology \n      society in England, the young survivors lay the \n      foundation for a new society.', u'author': u'Corets, Eva', u'price': 5.95, u'title': u'Maeve Ascendant', u'publish_date': u'2000-11-17', u'genre': u'Fantasy'}, {u'description': u'A former architect battles corporate zombies, \n      an evil sorceress, and her own childhood to become queen \n      of the world.', u'author': u'Ralls, Kim', u'price': 5.95, u'title': u'Midnight Rain', u'publish_date': u'2000-12-16', u'genre': u'Fantasy'}]
>>> 
>>> data['bk101']['price']
44.95
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> '''
C:


void main() {
	int x = 5;
	x = x + 2;
}
'''
'\nC:\n\n\nvoid main() {\n\tint x = 5;\n\tx = x + 2;\n}\n'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> x = 5
>>> x = x + 2
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> x = 5
>>> def increment(x):
	x = x + 1

	
>>> increment(x)
>>> x
5
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> a = [10, 20]
>>> def foo(y):
	y.append(30)

	
>>> foo(a)
>>> 
>>> 
>>> a
[10, 20, 30]
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> x = 0
>>> 
>>> 
>>> count = 0
>>> def tick():
	count += 1

	
>>> tick()

Traceback (most recent call last):
  File "<pyshell#754>", line 1, in <module>
    tick()
  File "<pyshell#753>", line 2, in tick
    count += 1
UnboundLocalError: local variable 'count' referenced before assignment
>>> def tick():
	count = count + 1

	
>>> tick()

Traceback (most recent call last):
  File "<pyshell#757>", line 1, in <module>
    tick()
  File "<pyshell#756>", line 2, in tick
    count = count + 1
UnboundLocalError: local variable 'count' referenced before assignment
>>> 
>>> 
>>> increment = 2
>>> 
>>> def foo():
	print increment

	
>>> foo()
2
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> count = 0
>>> 
>>> def tick():
	global count
	count += 1

	
>>> tick()
>>> count
1
>>> 
=============================== RESTART: Shell ===============================
>>> 
