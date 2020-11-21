Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 26 2016, 12:10:39) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> # Python has a distinction between a statement and an expression
>>> # an expression can evaluate to a value
>>> # a statement cannot be evaluated
>>> 
>>> import math
>>> x = 5
>>> x
5
>>> if x = 5:
	
SyntaxError: invalid syntax
>>> if import math
SyntaxError: invalid syntax
>>> 
>>> 
>>> names = ['John', 'Paul', 'George', 'Ringo']
>>> for name in names:
	print name

	
John
Paul
George
Ringo
>>> for i, name in enumerate(names):
	print i, name

	
0 John
1 Paul
2 George
3 Ringo
>>> for name in reversed(names):
	print name

	
Ringo
George
Paul
John
>>> for name in sorted(names):
	print name

	
George
John
Paul
Ringo
>>> roles = ['guitar', 'bass', 'guitar', 'drums']
>>> for name, role in zip(names, roles):
	print name, role

	
John guitar
Paul bass
George guitar
Ringo drums
>>> 
>>> for size in map(len, names):
	print size

	
4
4
6
5
>>> for name in map(str.upper, names):
	print name

	
JOHN
PAUL
GEORGE
RINGO
>>> 
>>> names
['John', 'Paul', 'George', 'Ringo']
>>> 
>>> def last_character(s):
	return s[-1]

>>> names[0]
'John'
>>> last_character(names[0])
'n'
>>> for c in map(last_character, names):
	print c

	
n
l
e
o
>>> 
>>> characters = []
>>> for name in names:
	characters.append(name[-1])

	
>>> del last_character
>>> 
>>> def transform(x):
	return 3 * x + 1

>>> 
>>> # `def` does 3 things:
>>> # 1. creates a function object
>>> # 2. attaches metadata to the object: __name__, __doc__
>>> # 3. assign the object to a variable matching its __name__
>>> transform
<function transform at 0x1018012a8>
>>> transform.__name__
'transform'
>>> 
>>> # `lambda` means "make a function"
>>> # 1. create a function object
>>> 
>>> lambda s: s[-1]
<function <lambda> at 0x1006f7d70>
>>> 
>>> map(lambda s: s[-1], names)
['n', 'l', 'e', 'o']
>>> 
>>> sorted(names, key=lambda s: s[-1])
['George', 'Paul', 'John', 'Ringo']
>>> 
>>> max(names)
'Ringo'
>>> max(names, key=lambda s: len(s) * 3 + 1)
'George'
>>> min(names, key=len)
'John'
>>> min(names, key=lambda s: s[-1])
'George'
>>> 
>>> names
['John', 'Paul', 'George', 'Ringo']
>>> 
>>> numbers = range(10)
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> 10
10
>>> lambda :
	
SyntaxError: invalid syntax
>>> lambda : None
<function <lambda> at 0x1006f7de8>
>>> 
>>> lambda x, y: x + y
<function <lambda> at 0x1006f7d70>
>>> lambda : import math
SyntaxError: invalid syntax
>>> 
>>> add = lambda x, y: x + y
>>> add
<function <lambda> at 0x1006f7de8>
>>> add(5, 10)
15
>>> 
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> map(lambda x: x ** 2, numbers)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
>>> filter(lambda x: x % 2 == 0, numbers)
[0, 2, 4, 6, 8]
>>> filter(lambda x: x % 2, numbers)
[1, 3, 5, 7, 9]
>>> filter(lambda x: x % 2 == 0, numbers)
[0, 2, 4, 6, 8]
>>> map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
[0, 4, 16, 36, 64]
>>> 
>>> []
[]
>>> [x ** 2 for x in numbers]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [x ** 2 for x in numbers if x % 2 == 0]
[0, 4, 16, 36, 64]
>>> 
>>> [x ** 2 for x in numbers if x % 2 == 0]
[0, 4, 16, 36, 64]

>>> 
>>> names
['John', 'Paul', 'George', 'Ringo']
>>> 
>>> map(len, names)
[4, 4, 6, 5]
>>> 
>>> [len(name) for name in names]
[4, 4, 6, 5]
>>> 
>>> [name[-1] for name in names]
['n', 'l', 'e', 'o']
>>> 
>>> {name[-1] for name in names}
set(['e', 'l', 'o', 'n'])
>>> {len(name) for name in names}
set([4, 5, 6])
>>> {name: len(name) for name in names}
{'Ringo': 5, 'Paul': 4, 'John': 4, 'George': 6}
>>> 
>>> (len(name) for name in names)
<generator object <genexpr> at 0x103a31460>
>>> tuple(len(name) for name in names)
(4, 4, 6, 5)
>>> 
>>> 
>>> [x ** 2 for x in range(10) if x % 2 == 0]
[0, 4, 16, 36, 64]
>>> 
>>> 
>>> results = []
>>> for x in range(10):
	if x % 2 == 0:
		results.append(x ** 2)

		
>>> 
>>> 
>>> def count_to_three():
	print 1
	print 2
	print 3

	
>>> count_to_three()
1
2
3
>>> 
>>> def count_to_three():
	yield 1
	yield 2
	yield 3

	
>>> count_to_three()
<generator object count_to_three at 0x103a31460>
>>> g = count_to_three()
>>> g
<generator object count_to_three at 0x1038432d0>
>>> next(g)
1
>>> next(g)
2
>>> next(g)
3
>>> next(g)

Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    next(g)
StopIteration
>>> 
>>> for i in [1, 2, 3]:
	print i

	
1
2
3
>>> def count_to_three():
	yield 1
	yield 2
	yield 3

	
>>> for i in count_to_three():
	print i

	
1
2
3
>>> g = count_to_three()
>>> import dis
>>> dis.dis(g)

Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    dis.dis(g)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/dis.py", line 49, in dis
    type(x).__name__
TypeError: don't know how to disassemble generator objects
>>> dis.dis(count_to_three)
  2           0 LOAD_CONST               1 (1)
              3 YIELD_VALUE         
              4 POP_TOP             

  3           5 LOAD_CONST               2 (2)
              8 YIELD_VALUE         
              9 POP_TOP             

  4          10 LOAD_CONST               3 (3)
             13 YIELD_VALUE         
             14 POP_TOP             
             15 LOAD_CONST               0 (None)
             18 RETURN_VALUE        
>>> 
>>> def count_to_three():
	print 'a'
	yield 1
	print 'b'
	yield 2
	print 'c'
	yield 3
	print 'd'

	
>>> g = count_to_three()
>>> g
<generator object count_to_three at 0x103a5ecd0>
>>> 
>>> iterator = iter(g)
>>> g
<generator object count_to_three at 0x103a5ecd0>
>>> iterator
<generator object count_to_three at 0x103a5ecd0>
>>> 
>>> next(iterator)
a
1
>>> next(iterator)
b
2
>>> next(iterator)
c
3
>>> next(iterator)
d

Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    next(iterator)
StopIteration
>>> next(iterator)

Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    next(iterator)
StopIteration
>>> next(iterator)

Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    next(iterator)
StopIteration
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
>>> 
>>> 
>>> 
>>> it = Iterator([1, 2, 3, 4])
>>> next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
4
>>> next(it)

Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    next(it)
StopIteration
>>> next(it)

Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    next(it)
StopIteration
>>> g = Iterator([1, 2, 3, 4])
>>> for i in g:
	print i

	
1
2
3
4
>>> g
<__main__.Iterator instance at 0x1039ae8c0>
>>> next(g)

Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    next(g)
StopIteration
>>> for i in g:
	print i

	
>>> 
>>> 
>>> [x ** 2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [x ** 2 for x in xrange(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
>>> 
>>> [x ** 2 for x in xrange(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
>>> 
>>> (x ** 2 for x in xrange(10))
<generator object <genexpr> at 0x103a31460>
>>> 
>>> print 5
5
>>> from __future__ import print_function
>>> print(5)
5
>>> 
>>> g = (x ** 2 for x in xrange(10))
>>> for i in g:
	print g
	
SyntaxError: invalid syntax
>>> for i in g:
	print(i)

	
0
1
4
9
16
25
36
49
64
81
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
>>> 
>>> 
>>> sum([1, 2, 3])
6
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/nasa.py", line 68, in <module>
    counts = Counter(hours)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/collections.py", line 477, in __init__
    self.update(*args, **kwds)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/collections.py", line 566, in update
    for elem in iterable:
  File "/Users/mike/teaching/2016-09-19/nasa.py", line 67, in <genexpr>
    hours = (log.timestamp.hour for log in logs)
  File "/Users/mike/teaching/2016-09-19/nasa.py", line 61, in parselines
    timestamp = datetime.strptime(timestamp[:-6], '%Y-%m-%d:%H:%M:%S')
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/_strptime.py", line 332, in _strptime
    (data_string, format))
ValueError: time data '01/Jul/1995:00:18:44' does not match format '%Y-%m-%d:%H:%M:%S'
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]
0 63
1 54
2 47
3 33
4 35
5 31
6 36
7 54
8 85
9 97
10 107
11 115
12 121
13 122
14 121
15 121
16 119
17 98
18 80
19 73
20 68
21 71
22 70
23 70
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]
0 63
1 54
2 47
3 33
4 35
5 31
6 36
7 54
8 85
9 97
10 107
11 115
12 121
13 122
14 121
15 121
16 119
17 98
18 80
19 73
20 68
21 71
22 70
23 70
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]
0 ###############################################################
1 ######################################################
2 ###############################################
3 #################################
4 ###################################
5 ###############################
6 ####################################
7 ######################################################
8 #####################################################################################
9 #################################################################################################
10 ###########################################################################################################
11 ###################################################################################################################
12 #########################################################################################################################
13 ##########################################################################################################################
14 #########################################################################################################################
15 #########################################################################################################################
16 #######################################################################################################################
17 ##################################################################################################
18 ################################################################################
19 #########################################################################
20 ####################################################################
21 #######################################################################
22 ######################################################################
23 ######################################################################
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]
0

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/nasa.py", line 71, in <module>
    print hour, '#' * count // 2
TypeError: unsupported operand type(s) for //: 'str' and 'int'
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]
0 ###############################
1 ###########################
2 #######################
3 ################
4 #################
5 ###############
6 ##################
7 ###########################
8 ##########################################
9 ################################################
10 #####################################################
11 #########################################################
12 ############################################################
13 #############################################################
14 ############################################################
15 ############################################################
16 ###########################################################
17 #################################################
18 ########################################
19 ####################################
20 ##################################
21 ###################################
22 ###################################
23 ###################################
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/nasa.py", line 71, in <module>
    print hour.ljust(3), count // 2 * '#'
AttributeError: 'int' object has no attribute 'ljust'
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/nasa.py ==============
[('com', 580), ('edu', 213), ('net', 173), ('gov', 148), ('ca', 52)]
0   ###############################
1   ###########################
2   #######################
3   ################
4   #################
5   ###############
6   ##################
7   ###########################
8   ##########################################
9   ################################################
10  #####################################################
11  #########################################################
12  ############################################################
13  #############################################################
14  ############################################################
15  ############################################################
16  ###########################################################
17  #################################################
18  ########################################
19  ####################################
20  ##################################
21  ###################################
22  ###################################
23  ###################################
>>> 
>>> 
>>> # Read Eval Print Loop
>>> 
>>> eval
<built-in function eval>
>>> 
>>> 
>>> input # eval(raw_input())
<built-in function input>
>>> 
>>> source = raw_input('<<< ')
<<< 2 + 2
>>> source
'2 + 2'
>>> type(source)
<type 'str'>
>>> 
>>> eval(source)
4
>>> def repl():
	'read eval print loop'
	while True:
		source = raw_input('py> ')
		result = eval(source)
		print repr(result)

		
>>> repl()
py> 2 + 2
4
py> 'a' * 20
'aaaaaaaaaaaaaaaaaaaa'
py> lambda : 'hello world'
<function <lambda> at 0x103164ed8>
py> import math

Traceback (most recent call last):
  File "<pyshell#246>", line 1, in <module>
    repl()
  File "<pyshell#245>", line 5, in repl
    result = eval(source)
  File "<string>", line 1
    import math
         ^
SyntaxError: invalid syntax
>>> exec 'import math'
>>> def repl():
	'read eval print loop'
	while True:
		source = raw_input('py> ')
		try:
			result = eval(source)
			print repr(result)
		except SyntaxError:
			exec source

>>> repl()
py> import math
py> x = 5
py> math.sqrt(5)
2.23606797749979
py> import subprocess
py> subprocess.check_output('ls')
'Blain.Marilyn.vcf\nDavis.Harold.vcf\nGunter.Fritz.vcf\nHettinger.Raymond.vcf\nJones.David.vcf\nMarks.Blair.vcf\nMasterson.Martin.vcf\nPichon.Esmerela.vcf\nSchmidt.Gertrude.vcf\nThomas.Mary.vcf\nZapata.Luis.vcf\n__pycache__\nbrief.py\nbrief_xml.py\ncounting_urls.py\nday1.idle.py\nday1a.idle.py\nday2.idle.py\nday3.idle.py\nday4.idle.py\ndog.py\ndog.pyc\ndownload.py\nexample.py\nexample.txt\nget_pypi_count.py\nhighlight.py\nhighlight.pyc\niteration.py\nkaprekar.py\nkaprekar.svg\nlinks.txt\nlogo.py\nlookup.py\nlookup.pyc\nnasa.py\nnotes\noop.py\noperators_in_def_and_call.py\npublish.py\nshow_books_json.py\nshow_books_xml.py\nvcard.py\nvcard.pyc\nxml_with_namespaces.py\n'
py> 
py> subprocess.call('rm -rf /

Traceback (most recent call last):
  File "<pyshell#249>", line 1, in <module>
    repl()
  File "<pyshell#248>", line 4, in repl
    source = raw_input('py> ')
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/idlelib/PyShell.py", line 1398, in readline
    line = self._line_buffer or self.shell.readline()
KeyboardInterrupt
>>> repl()
py> 

Traceback (most recent call last):
  File "<pyshell#250>", line 1, in <module>
    repl()
  File "<pyshell#248>", line 4, in repl
    source = raw_input('py> ')
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/idlelib/PyShell.py", line 1398, in readline
    line = self._line_buffer or self.shell.readline()
KeyboardInterrupt
>>> 
=============================== RESTART: Shell ===============================
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/udp_client.py ===========
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/udp_client.py ===========
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/udp_client.py ===========
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/udp_client.py ===========
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/udp_client.py ===========
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/udp_client.py ===========
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/udp_client.py ===========
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/udp_client.py ===========
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/udp_client.py ===========
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/udp_client.py ===========
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/udp_client.py ===========
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/udp_client.py ===========
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========
Hello!
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/tcp_client.py", line 8, in <module>
    s.connect(address)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.py", line 228, in meth
    return getattr(self._sock,name)(*args)
error: [Errno 61] Connection refused
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========
Hello!
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========
Hello!
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========
Hello!
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========
Hello!
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========
He
ll
o!
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========
Hello!
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========
Hello!
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========
Hello!
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========
Hello!
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========
Hello!
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========
Thu Sep 22 13:49:30 2016
Thu Sep 22 13:49:31 2016
Thu Sep 22 13:49:32 2016
Thu Sep 22 13:49:33 2016
Thu Sep 22 13:49:34 2016
Thu Sep 22 13:49:35 2016
Thu Sep 22 13:49:36 2016
Thu Sep 22 13:49:37 2016
Thu Sep 22 13:49:38 2016
Thu Sep 22 13:49:39 2016
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/tcp_client.py", line 11, in <module>
    data = s.recv(4096)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.py", line 174, in _dummy
    raise error(EBADF, 'Bad file descriptor')
error: [Errno 9] Bad file descriptor
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========
Hello!
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========
Hello!
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========
Thu Sep 22 13:58:00 2016
Thu Sep 22 13:58:01 2016
Thu Sep 22 13:58:02 2016
Thu Sep 22 13:58:03 2016
Thu Sep 22 13:58:04 2016
Thu Sep 22 13:58:05 2016
Thu Sep 22 13:58:06 2016
Thu Sep 22 13:58:07 2016
Thu Sep 22 13:58:08 2016
Thu Sep 22 13:58:09 2016
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/tcp_client.py ===========
Thu Sep 22 13:59:30 2016
Thu Sep 22 13:59:31 2016
Thu Sep 22 13:59:32 2016
Thu Sep 22 13:59:33 2016
Thu Sep 22 13:59:34 2016
Thu Sep 22 13:59:35 2016
Thu Sep 22 13:59:36 2016
Thu Sep 22 13:59:37 2016
Thu Sep 22 13:59:38 2016
Thu Sep 22 13:59:39 2016
>>> 

>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
========== RESTART: /Users/mike/teaching/2016-09-19/http_client.py ==========

=============================== RESTART: Shell ===============================
>>> 
========== RESTART: /Users/mike/teaching/2016-09-19/http_client.py ==========
>>> len(response)
74138
>>> response[:1000]
'HTTP/1.1 200 OK\r\nDate: Thu, 22 Sep 2016 19:21:52 GMT\r\nServer: Apache\r\nSet-Cookie: ObSSOCookie=rxHMNrnNuIbID6eLb8Rmj3PeuCfWOZpQLkzXC1JhN3JKOjIogI%2Bf2Udkdcyv4klH1%2F9Xub2tyDQdNvb7JnCbi4hd%2Bgf6V7968EWnE8ujvNvA1vXglL6ePA487XOfgGW2Dy755G%2Bq1DBweoSfk6T6Q6wax8SdeTFj%2BZHBlyRXS7cKQPsx46SgHuYykRpAZHOvkGxSV5%2FufWlvAAOesDfQCnuIDI9kcr9RCPvtxuIluYwNnV%2F3nUw1dlRYwc%2F8zVTJmCXw%2FmyM59pLvJsLJ4ogphzz29gNNxg4cdOXXpdt8dBLPS6tc5hyQOuPf6ss6KimpY831A95q9C3AeLOdp4BrETVqgXeu8bunrXsxxsh1slrLNxDHP8XBdIirPzlRgRk; path=/; domain=.cisco.com\r\nCache-Control: private\r\nPragma: private\r\nSet-Cookie: CP_GUTC=173.37.145.92.1474572112961604; path=/; expires=Tue, 21-Sep-21 19:21:52 GMT; domain=.cisco.com\r\nETag: "11e3e-53d1ac3cb8e1c"\r\nAccept-Ranges: bytes\r\nContent-Length: 73278\r\nCDCHOST: wemxweb-publish-prod2-01\r\nVary: Accept-Encoding\r\nConnection: close\r\nContent-Type: text/html\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n<!DOCTYPE html>\r\n<!--[if IEMobile 7 ]><html class="no-js no-touch iem7" lang="en"> <![en'
>>> 
========== RESTART: /Users/mike/teaching/2016-09-19/http_client.py ==========
>>> len(response)
15180
>>> response[:1000]
'HTTP/1.1 200 OK\r\nDate: Thu, 22 Sep 2016 19:26:23 GMT\r\nServer: Apache\r\nSet-Cookie: ObSSOCookie=hyzINaG2cf19AqBDC7bPjxFQgxI5M1pD%2F8EQOy%2Flhp5M2v%2BuUaxenGSgN%2Bv4oKizfXWMc6LG0EUVUmrswbqqvbh%2B5k6uyzjoFmzon3TiLTeEMGQxclOA9ic9mvJX%2BOJjGpRnoG1swWjehxlg9eUADivfOzFZbvAJVu%2F%2BoMybCayeWOpwuQrNoddjQH252oX8pAb%2BCf0tpcfi%2FgUKfXk4oqXRStxz0ebs6oj02aFD9G4ou%2BPAAsrmJnQLo9FSxl08sgAPdoPrJ6LC1REOS%2B99JuyARco5LaCTgSazB6Bsfe4l6ySvW78ytAl60XQP34qgYaQWlIQjU%2FtADgqaz%2FQckGGLFP1NO%2BHLej15Ad%2BPjUU9fm7ukxGDVC2LICOBHU8n; path=/; domain=.cisco.com\r\nCache-Control: private\r\nPragma: private\r\nSet-Cookie: CP_GUTC=173.37.145.92.1474572383671801; path=/; expires=Tue, 21-Sep-21 19:26:23 GMT; domain=.cisco.com\r\nETag: "11e3e-53d1ac3cb8e1c"\r\nAccept-Ranges: bytes\r\nContent-Encoding: gzip\r\nCDCHOST: wemxweb-publish-prod2-03\r\nVary: Accept-Encoding\r\nContent-Length: 14282\r\nConnection: close\r\nContent-Type: text/html\r\n\r\n\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03\xed}\xedv\xdb6\xb6\xe8\xefz\xad\xbe\x03\xaa\xce\xc4\xf6\xd8\x94l\xc5\xf9rl\xf5\xda\xb2\x93z&\x8e]\xdbiO\xa7+K\x8b"!\x896E\xb0\x04)G\xe9\xe4\xac\xf3\x10\xf7\xcf\xfdw\x9f\xe5>\xcay\x92\xbb7\x00\x92\xe0\x87D\x89v\xdctN\xdd\x99H\x02\xc1\r`cc\x7fac\xe3\xeb\x95\xaf\x97'
>>> 
========== RESTART: /Users/mike/teaching/2016-09-19/http_client.py ==========
>>> len(content)
14282
>>> print header
HTTP/1.1 200 OK
Date: Thu, 22 Sep 2016 19:28:32 GMT
Server: Apache
Set-Cookie: ObSSOCookie=pSA7ZGLd8AFsENcFi1NZZD61ynrDAFHxG8m0SgRq1TdO4q94I95uN2OGquG9nrzIYFHTlhFVwsyTbMe6g1TG6jdgilKe9e0eArIGvxYrV0mdP0YJh%2Fi3fnu3%2BjcxzFae%2BanxXjOO381rWaqYIYP4lQ5Z9sXhDv8qYcFXwPYb4494SyjFv7fXEIYczTS1fAg89oZ8ZwB25Ra%2FIvCFupEPcavl1nnqlWFb%2B4yvguAjcl7s11wEgegp3SUvoM2Bdm0VM0dAJqqWkQA2NGlMKDbBxdeW9HypaBmLAJu39Is54qNrItPChBg%2FDCcTptAolS4HbdqiEMfsFynPb3aa9M7S2DtWXP4VGV1E2oYwHF6vvIbI%2FdFjy5O%2BzNq%2FriXufo38; path=/; domain=.cisco.com
Cache-Control: private
Pragma: private
Set-Cookie: CP_GUTC=173.37.145.92.1474572512804004; path=/; expires=Tue, 21-Sep-21 19:28:32 GMT; domain=.cisco.com
ETag: "11e3e-53d1ac3cb8e1c"
Accept-Ranges: bytes
Content-Encoding: gzip
CDCHOST: wemxweb-publish-prod2-04
Vary: Accept-Encoding
Content-Length: 14282
Connection: close
Content-Type: text/html
>>> '0.0%' in '18 packets sent, 9 packets received, 50.0% packet loss'
True
>>> 'connected' in 'interface eth0 disconnected'
True
>>> 'connected' in 'interface eth0 disconnected'.split()
False
>>> '0.0%' in '18 packets sent, 9 packets received, 50.0% packet loss'.split()
False
>>> 
========== RESTART: /Users/mike/teaching/2016-09-19/http_client.py ==========

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/http_client.py", line 36, in <module>
    fakefile = StringIO(content)
TypeError: initial_value must be unicode or None, not str
>>> import io
>>> dir(io)
['BlockingIOError', 'BufferedIOBase', 'BufferedRWPair', 'BufferedRandom', 'BufferedReader', 'BufferedWriter', 'BytesIO', 'DEFAULT_BUFFER_SIZE', 'FileIO', 'IOBase', 'IncrementalNewlineDecoder', 'OpenWrapper', 'RawIOBase', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'StringIO', 'TextIOBase', 'TextIOWrapper', 'UnsupportedOperation', '__all__', '__author__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_io', 'abc', 'open']
>>> from StringIO import StringIO
>>> 
========== RESTART: /Users/mike/teaching/2016-09-19/http_client.py ==========
>>> len(content)
73278
>>> len(response)
15178
>>> print header
HTTP/1.1 200 OK
Date: Thu, 22 Sep 2016 19:37:56 GMT
Server: Apache
Set-Cookie: ObSSOCookie=IgI%2Fn%2FjZeWcp%2BmGtI%2FZtC4X1diYDQd5GKYt%2FrccpBWdkyuDrWac0E2nwgoYrkeEIrZduAUnRrbyxnUeA79FB%2BDVy3AFXiqzucZOATFSybxhp9maPyuS6UizAojLJK1UCxYtXhrSQ44g889CtE%2B1YMPSLetLoBHoiMNX7Psz0LVY38qolrs9nqdvS1%2Fe3u3Ou51uFh9RuQ8P8kaQ876f%2BxFnnPfYofvfWkuuIOtt8qdXEHC2%2BO6HGfnAJ%2BErG9Q%2BND%2B1WntQvLPVRtk7tZX5LuR9C5soBmAn9O0FBr09updxLO4jq0JCcWKW%2BHbaI8PgRBVUvQRDQLVnsKeQjKScbrFqXLt5LmSUq9EYcqc7gtSL1OJ%2BdAy2O7rJt01xcGlW6; path=/; domain=.cisco.com
Cache-Control: private
Pragma: private
Set-Cookie: CP_GUTC=173.37.145.92.1474573076152544; path=/; expires=Tue, 21-Sep-21 19:37:56 GMT; domain=.cisco.com
ETag: "11e3e-53d1ac3cb8e1c"
Accept-Ranges: bytes
Content-Encoding: gzip
CDCHOST: wemxweb-publish-prod2-03
Vary: Accept-Encoding
Content-Length: 14282
Connection: close
Content-Type: text/html
>>> type(5)
<type 'int'>
>>> type(type(5))
<type 'type'>
>>> 
