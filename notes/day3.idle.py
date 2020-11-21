Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 26 2016, 12:10:39) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/lookup.py =============
>>> dict()
{}
>>> settings['fg']
'cyan'
>>> defaults['fg']
'green'
>>> settings['bg']

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    settings['bg']
KeyError: 'bg'
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/lookup.py =============
>>> lookup('fg')
'cyan'
>>> lookup('bg')
'black'
>>> lookup('z')

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    lookup('z')
  File "/Users/mike/teaching/2016-09-19/lookup.py", line 11, in lookup
    return defaults[key]
KeyError: 'z'
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/lookup.py =============
>>> lookup('fg')
'cyan'
>>> lookup('bg')
'black'
>>> lookup('z')

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    lookup('z')
  File "/Users/mike/teaching/2016-09-19/lookup.py", line 19, in lookup
    return defaults[key]
KeyError: 'z'
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/lookup.py =============

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/lookup.py", line 24, in <module>
    os.remove('tmp.txt')
OSError: [Errno 2] No such file or directory: 'tmp.txt'
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/lookup.py =============
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/lookup.py =============
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/lookup.py =============

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/lookup.py", line 30, in <module>
    safe_remove('tmp.txt')
  File "/Users/mike/teaching/2016-09-19/lookup.py", line 28, in safe_remove
    os.remove(filename)
OSError: [Errno 2] No such file or directory: 'tmp.txt'
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/lookup.py =============
>>> 
>>> lookup('fg', settings, defaults)
'cyan'
>>> lookup('bg', settings, defaults)
'black'
>>> lookup('z', settings, defaults)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    lookup('z', settings, defaults)
  File "/Users/mike/teaching/2016-09-19/lookup.py", line 13, in lookup
    return fallback[key]
KeyError: 'z'
>>> 
>>> 
>>> def foo():
	x = 'I am local'
	print locals()

	
>>> foo()
{'x': 'I am local'}
>>> 
>>> locals()
{'settings': {'h': 40, 'w': 80, 'fg': 'cyan'}, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/Users/mike/teaching/2016-09-19/lookup.py', '__package__': None, 'lookup': <function lookup at 0x1018012a8>, 'safe_remove': <function safe_remove at 0x1006f7d70>, 'defaults': {'h': 24, 'bg': 'black', 'w': 40, 'fg': 'green'}, 'time': <module 'time' from '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/time.so'>, '__name__': '__main__', 'foo': <function foo at 0x103277050>, 'os': <module 'os' from '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/os.pyc'>, '__doc__': ' lookup.py\n'}
>>> foo()
{'x': 'I am local'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> x = 'I am global'
>>> y = 'I am also global'
>>> 
>>> def foo():
	y = 'I am local'
	print 'GLOBALS', globals()
	print 'LOCALS', locals()

	
>>> foo()
GLOBALS {'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 'I am global', 'y': 'I am also global', '__name__': '__main__', 'foo': <function foo at 0x1012012a8>, '__doc__': None}
LOCALS {'y': 'I am local'}
>>> def foo():
	y = 'I am local'
	print 'GLOBALS', globals()
	print 'LOCALS', locals()
	print y
	print x

	
>>> def foo():
	y = 'I am local'
	print y
	print x

	
>>> foo()
I am local
I am global
>>> x
'I am global'
>>> y
'I am also global'
>>> 
>>> 
>>> def foo():
	y = 'I am local'
	print lookup('y', locals(), globals())
	print lookup('x', locals(), globals())

	
>>> foo()

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    foo()
  File "<pyshell#52>", line 3, in foo
    print lookup('y', locals(), globals())
NameError: global name 'lookup' is not defined
>>> from lookup import lookup
>>> 
>>> 
>>> x = 'I am global'
>>> y = 'I am also global'
>>> 
>>> def foo():
	y = 'I am local'
	print lookup('y', locals(), globals())
	print lookup('x', locals(), globals())

	
>>> foo()
I am local
I am global
>>> 
>>> def foo():
	y = 'I am local'
	print lookup('y', locals(), globals())
	print lookup('x', locals(), globals())
	print lookup('z', locals(), globals())

	
>>> foo()
I am local
I am global

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    foo()
  File "<pyshell#66>", line 5, in foo
    print lookup('z', locals(), globals())
  File "lookup.py", line 13, in lookup
    return fallback[key]
KeyError: 'z'
>>> 
>>> def bar():
	y = 'I am local'
	print y
	print x
	print z

	
>>> bar()
I am local
I am global

Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    bar()
  File "<pyshell#74>", line 5, in bar
    print z
NameError: global name 'z' is not defined
>>> 
>>> 
>>> v

Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    v
NameError: name 'v' is not defined
>>> 
>>> 
>>> class Dog:
	kind = 'canine'
	mood = 'happy
	
SyntaxError: EOL while scanning string literal
>>> 
>>> class Dog:
	kind = 'canine'
	mood = 'happy'

	
>>> a = Dog()
>>> a.name = 'Fido'
>>> 
>>> a.name
'Fido'
>>> a.mood
'happy'
>>> a.kind
'canine'
>>> 
>>> a.__dict__
{'name': 'Fido'}
>>> Dog.__dict__
{'__module__': '__main__', '__doc__': None, 'kind': 'canine', 'mood': 'happy'}
>>> 
>>> lookup('name', a.__dict__, Dog.__dict__)
'Fido'
>>> lookup('mood', a.__dict__, Dog.__dict__)
'happy'
>>> lookup('kind', a.__dict__, Dog.__dict__)
'canine'
>>> lookup('z', a.__dict__, Dog.__dict__)

Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    lookup('z', a.__dict__, Dog.__dict__)
  File "lookup.py", line 13, in lookup
    return fallback[key]
KeyError: 'z'
>>> 
>>> 
>>> class Dog:
	kind = 'canine'
	mood = 'happy'

	
>>> a = Dog()
>>> a.name = 'Fido'
>>> 
>>> a.z

Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    a.z
AttributeError: Dog instance has no attribute 'z'
>>> 
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/lookup.py =============
>>> lookup('fg', settings, defaults)

Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    lookup('fg', settings, defaults)
TypeError: lookup() takes exactly 2 arguments (3 given)
>>> lookup('fg', [settings, defaults])
'cyan'
>>> lookup('fg', [user, settings, defaults])
'magenta'
>>> lookup('bg', [user, settings, defaults])
'black'
>>> lookup('h', [user, settings, defaults])
40
>>> lookup('z', [user, settings, defaults])

Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    lookup('z', [user, settings, defaults])
  File "/Users/mike/teaching/2016-09-19/lookup.py", line 16, in lookup
    raise KeyError(key)
KeyError: 'z'
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/lookup.py =============
>>> 
>>> import math
>>> math
<module 'math' from '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/math.so'>
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/lookup.py =============
>>> 
>>> 
>>> 
>>> class Dog:
	kind = 'canine'
	mood = 'happy'

	
>>> class AngryDog(Dog):
	mood = 'angry'

	
>>> b = AngryDog()
>>> b.name = 'Rex'
>>> 
>>> b.__dict__
{'name': 'Rex'}
>>> AngryDog.__dict__
{'__module__': '__main__', 'mood': 'angry', '__doc__': None}
>>> Dog.__dict__
{'__module__': '__main__', '__doc__': None, 'kind': 'canine', 'mood': 'happy'}
>>> 
>>> b.mood
'angry'
>>> b.kind
'canine'
>>> 
>>> dir(b)
['__doc__', '__module__', 'kind', 'mood', 'name']
>>> b.__class__
<class __main__.AngryDog at 0x103a48530>
>>> b.__class__.__bases__
(<class __main__.Dog at 0x1020942c0>,)
>>> help(b)
Help on instance of AngryDog in module __main__:

class AngryDog(Dog)
 |  Data and other attributes defined here:
 |  
 |  mood = 'angry'
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from Dog:
 |  
 |  kind = 'canine'

>>> 
>>> from collections import Counter
>>> help(Counter)
Help on class Counter in module collections:

class Counter(__builtin__.dict)
 |  Dict subclass for counting hashable items.  Sometimes called a bag
 |  or multiset.  Elements are stored as dictionary keys and their counts
 |  are stored as dictionary values.
 |  
 |  >>> c = Counter('abcdeabcdabcaba')  # count elements from a string
 |  
 |  >>> c.most_common(3)                # three most common elements
 |  [('a', 5), ('b', 4), ('c', 3)]
 |  >>> sorted(c)                       # list all unique elements
 |  ['a', 'b', 'c', 'd', 'e']
 |  >>> ''.join(sorted(c.elements()))   # list elements with repetitions
 |  'aaaaabbbbcccdde'
 |  >>> sum(c.values())                 # total of all counts
 |  15
 |  
 |  >>> c['a']                          # count of letter 'a'
 |  5
 |  >>> for elem in 'shazam':           # update counts from an iterable
 |  ...     c[elem] += 1                # by adding 1 to each element's count
 |  >>> c['a']                          # now there are seven 'a'
 |  7
 |  >>> del c['b']                      # remove all 'b'
 |  >>> c['b']                          # now there are zero 'b'
 |  0
 |  
 |  >>> d = Counter('simsalabim')       # make another counter
 |  >>> c.update(d)                     # add in the second counter
 |  >>> c['a']                          # now there are nine 'a'
 |  9
 |  
 |  >>> c.clear()                       # empty the counter
 |  >>> c
 |  Counter()
 |  
 |  Note:  If a count is set to zero or reduced to zero, it will remain
 |  in the counter until the entry is deleted or the counter is cleared:
 |  
 |  >>> c = Counter('aaabbc')
 |  >>> c['b'] -= 2                     # reduce the count of 'b' by two
 |  >>> c.most_common()                 # 'b' is still in, but its count is zero
 |  [('a', 3), ('c', 1), ('b', 0)]
 |  
 |  Method resolution order:
 |      Counter
 |      __builtin__.dict
 |      __builtin__.object
 |  
 |  Methods defined here:
 |  
 |  __add__(self, other)
 |      Add counts from two counters.
 |      
 |      >>> Counter('abbb') + Counter('bcc')
 |      Counter({'b': 4, 'c': 2, 'a': 1})
 |  
 |  __and__(self, other)
 |      Intersection is the minimum of corresponding counts.
 |      
 |      >>> Counter('abbb') & Counter('bcc')
 |      Counter({'b': 1})
 |  
 |  __delitem__(self, elem)
 |      Like dict.__delitem__() but does not raise KeyError for missing values.
 |  
 |  __init__(*args, **kwds)
 |      Create a new, empty Counter object.  And if given, count elements
 |      from an input iterable.  Or, initialize the count from another mapping
 |      of elements to their counts.
 |      
 |      >>> c = Counter()                           # a new, empty counter
 |      >>> c = Counter('gallahad')                 # a new counter from an iterable
 |      >>> c = Counter({'a': 4, 'b': 2})           # a new counter from a mapping
 |      >>> c = Counter(a=4, b=2)                   # a new counter from keyword args
 |  
 |  __missing__(self, key)
 |      The count of elements not in the Counter is zero.
 |  
 |  __or__(self, other)
 |      Union is the maximum of value in either of the input counters.
 |      
 |      >>> Counter('abbb') | Counter('bcc')
 |      Counter({'b': 3, 'c': 2, 'a': 1})
 |  
 |  __reduce__(self)
 |  
 |  __repr__(self)
 |  
 |  __sub__(self, other)
 |      Subtract count, but keep only results with positive counts.
 |      
 |      >>> Counter('abbbc') - Counter('bccd')
 |      Counter({'b': 2, 'a': 1})
 |  
 |  copy(self)
 |      Return a shallow copy.
 |  
 |  elements(self)
 |      Iterator over elements repeating each as many times as its count.
 |      
 |      >>> c = Counter('ABCABC')
 |      >>> sorted(c.elements())
 |      ['A', 'A', 'B', 'B', 'C', 'C']
 |      
 |      # Knuth's example for prime factors of 1836:  2**2 * 3**3 * 17**1
 |      >>> prime_factors = Counter({2: 2, 3: 3, 17: 1})
 |      >>> product = 1
 |      >>> for factor in prime_factors.elements():     # loop over factors
 |      ...     product *= factor                       # and multiply them
 |      >>> product
 |      1836
 |      
 |      Note, if an element's count has been set to zero or is a negative
 |      number, elements() will ignore it.
 |  
 |  most_common(self, n=None)
 |      List the n most common elements and their counts from the most
 |      common to the least.  If n is None, then list all element counts.
 |      
 |      >>> Counter('abcdeabcdabcaba').most_common(3)
 |      [('a', 5), ('b', 4), ('c', 3)]
 |  
 |  subtract(*args, **kwds)
 |      Like dict.update() but subtracts counts instead of replacing them.
 |      Counts can be reduced below zero.  Both the inputs and outputs are
 |      allowed to contain zero and negative counts.
 |      
 |      Source can be an iterable, a dictionary, or another Counter instance.
 |      
 |      >>> c = Counter('which')
 |      >>> c.subtract('witch')             # subtract elements from another iterable
 |      >>> c.subtract(Counter('watch'))    # subtract elements from another counter
 |      >>> c['h']                          # 2 in which, minus 1 in witch, minus 1 in watch
 |      0
 |      >>> c['w']                          # 1 in which, minus 1 in witch, minus 1 in watch
 |      -1
 |  
 |  update(*args, **kwds)
 |      Like dict.update() but add counts instead of replacing them.
 |      
 |      Source can be an iterable, a dictionary, or another Counter instance.
 |      
 |      >>> c = Counter('which')
 |      >>> c.update('witch')           # add elements from another iterable
 |      >>> d = Counter('watch')
 |      >>> c.update(d)                 # add elements from another counter
 |      >>> c['h']                      # four 'h' in which, witch, and watch
 |      4
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  fromkeys(cls, iterable, v=None) from __builtin__.type
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from __builtin__.dict:
 |  
 |  __cmp__(...)
 |      x.__cmp__(y) <==> cmp(x,y)
 |  
 |  __contains__(...)
 |      D.__contains__(k) -> True if D has a key k, else False
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __setitem__(...)
 |      x.__setitem__(i, y) <==> x[i]=y
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  get(...)
 |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
 |  
 |  has_key(...)
 |      D.has_key(k) -> True if D has a key k, else False
 |  
 |  items(...)
 |      D.items() -> list of D's (key, value) pairs, as 2-tuples
 |  
 |  iteritems(...)
 |      D.iteritems() -> an iterator over the (key, value) items of D
 |  
 |  iterkeys(...)
 |      D.iterkeys() -> an iterator over the keys of D
 |  
 |  itervalues(...)
 |      D.itervalues() -> an iterator over the values of D
 |  
 |  keys(...)
 |      D.keys() -> list of D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |  
 |  setdefault(...)
 |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
 |  
 |  values(...)
 |      D.values() -> list of D's values
 |  
 |  viewitems(...)
 |      D.viewitems() -> a set-like object providing a view on D's items
 |  
 |  viewkeys(...)
 |      D.viewkeys() -> a set-like object providing a view on D's keys
 |  
 |  viewvalues(...)
 |      D.viewvalues() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from __builtin__.dict:
 |  
 |  __hash__ = None
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T

>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
=== RESTART: /Users/mike/teaching/2016-09-19/operators_in_def_and_call.py ===
>>> power(5)
25
>>> power(10)
100
>>> 
=== RESTART: /Users/mike/teaching/2016-09-19/operators_in_def_and_call.py ===
>>> power(5, 3)
125
>>> 
>>> 
>>> power(5)

Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    power(5)
TypeError: power() takes exactly 2 arguments (1 given)
>>> 
=== RESTART: /Users/mike/teaching/2016-09-19/operators_in_def_and_call.py ===
>>> 
>>> 
=== RESTART: /Users/mike/teaching/2016-09-19/operators_in_def_and_call.py ===
>>> 
>>> power(5)
25
>>> power(5, 3)
125
>>> power()

Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    power()
TypeError: power() takes at least 1 argument (0 given)
>>> 
>>> 
=== RESTART: /Users/mike/teaching/2016-09-19/operators_in_def_and_call.py ===
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> power(5, 3) # power(base, exponent)
125
>>> foo(True, False, True, True)

Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    foo(True, False, True, True)
NameError: name 'foo' is not defined
>>> 
>>> power(2, 10)
1024
>>> power(10, 2)
100
>>> 
=== RESTART: /Users/mike/teaching/2016-09-19/operators_in_def_and_call.py ===
>>> 1024
1024
>>> 
>>> 
>>> power(5, 3) # power(base, exponent)
243
>>> power(base=5, exponent=3)
125
>>> 
=== RESTART: /Users/mike/teaching/2016-09-19/operators_in_def_and_call.py ===
>>> power(base=5, exponent=3)

Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    power(base=5, exponent=3)
TypeError: power() got an unexpected keyword argument 'exponent'
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
=== RESTART: /Users/mike/teaching/2016-09-19/operators_in_def_and_call.py ===
>>> 
>>> x = [5, 3]
>>> power(x[0], x[1])
125
>>> power(*x)
125
>>> 
=== RESTART: /Users/mike/teaching/2016-09-19/operators_in_def_and_call.py ===
>>> 
>>> 
>>> y
{'base': 5, 'exponent': 3}
>>> 
>>> 
>>> power(y['base'], y['exponent'])
125
>>> 
>>> power(*y)

Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    power(*y)
  File "/Users/mike/teaching/2016-09-19/operators_in_def_and_call.py", line 19, in power
    return base ** exponent
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
>>> 
>>> for key in y:
	print key

	
base
exponent
>>> 
>>> power(**y)
125
>>> 
=== RESTART: /Users/mike/teaching/2016-09-19/operators_in_def_and_call.py ===
>>> foo(1, 2, 3)
(1, 2, 3)
>>> 
=== RESTART: /Users/mike/teaching/2016-09-19/operators_in_def_and_call.py ===
>>> 
>>> bar(1, 2, 3)

Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    bar(1, 2, 3)
TypeError: bar() takes exactly 0 arguments (3 given)
>>> bar(a=1, b=2)
{'a': 1, 'b': 2}
>>> 
=== RESTART: /Users/mike/teaching/2016-09-19/operators_in_def_and_call.py ===
>>> 
>>> baz(1, 2, 3, a=4, b=5)
(1, 2, 3)
{'a': 4, 'b': 5}
>>> 
>>> 
>>> 
>>> bar(a=2, b=3)
{'a': 2, 'b': 3}
>>> 
>>> def only_keywords(*, **kwargs):
	
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> numbers = [5, 42, 3.7]
>>> numbers = [5, 42, 3.7, 7, 11]
>>> 
>>> 
>>> a, b, c, d, e = numbers
>>> 
>>> first, second, = numbers[:2]
>>> first, second, *rest = numbers
SyntaxError: invalid syntax
>>> 
>>> 
>>> numbers = (1, 2, 3)
>>> 
>>> (a, b, c) = numbers
>>> 
>>> 
>>> 1, 2, 3
(1, 2, 3)
>>> 
>>> 
>>> 1,
(1,)
>>> (1, 2, 3)
(1, 2, 3)
>>> (1, 2)
(1, 2)
>>> (1)
1
>>> (1,)
(1,)
>>> 
>>> (a, b, c) = numbers
>>> 
>>> 
>>> y = {'a': 1, 'b': 2}
>>> 
>>> {'a': w, 'b': z} = y
SyntaxError: can't assign to literal
>>> 
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> a = [10, 20]
>>> 
>>> def push(lst):
	lst.append(30)
	return lst

>>> push(a)
[10, 20, 30]
>>> push(a)
[10, 20, 30, 30]
>>> push(a)
[10, 20, 30, 30, 30]
>>> push(a)
[10, 20, 30, 30, 30, 30]
>>> push(a)
[10, 20, 30, 30, 30, 30, 30]
>>> 
>>> push()

Traceback (most recent call last):
  File "<pyshell#269>", line 1, in <module>
    push()
TypeError: push() takes exactly 1 argument (0 given)
>>> 
>>> 
>>> a = [10, 20]
>>> 
>>> def push(lst=[]):
	lst.append(30)
	return lst

>>> push()
[30]
>>> push()
[30, 30]
>>> dir(push)
['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']
>>> push.__defaults__
([30, 30],)
>>> 
>>> def push(lst=None):
	if lst is None:
		lst = []
	lst.append(30)
	return lst

>>> push()
[30]
>>> push()
[30]
>>> push()
[30]
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/lookup.py =============
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/lookup.py =============
>>> 
>>> 
>>> lookup('bg', [user, settings, defaults])
'black'
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/lookup.py =============
>>> lookup('bg', user, settings, defaults)
'black'
>>> lookup('bg', user)

Traceback (most recent call last):
  File "<pyshell#290>", line 1, in <module>
    lookup('bg', user)
  File "/Users/mike/teaching/2016-09-19/lookup.py", line 26, in lookup
    raise KeyError(key)
KeyError: 'bg'
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/oop.py ==============
>>> 
>>> 
>>> a
<__main__.Dog instance at 0x1039ad440>
>>> 
>>> isinstance(a, Dog)
True
>>> isinstance(b, Dog)
True
>>> isinstance(c, Dog)
False
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/oop.py ==============
Woof! <__main__.Dog instance at 0x1039a9638> is barking
Woof! <__main__.Dog instance at 0x1039a7b00> is barking
Meow. <__main__.Cat instance at 0x1039ae050> is purring
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/oop.py ==============
Woof! Fido is barking
Woof! Clifford is barking
Meow. Socks is purring
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/oop.py ==============
Woof! Fido is barking
Woof! Clifford is barking
Meow. Socks is purring
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/oop.py ==============
Woof! Fido is barking
Woof! Clifford is barking
Meow. Socks is purring
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/oop.py ==============
Woof! Fido is barking
Woof! Clifford is barking
Meow. Socks is purring
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/oop.py ==============
Woof! Fido is barking
Woof! Clifford is barking
Meow. Socks is purring
>>> 
>>> 
>>> c
<__main__.Cat instance at 0x1039ae050>
>>> 
>>> 
>>> c.talk()
Meow. Socks is purring
>>> c.talk(1, 2)

Traceback (most recent call last):
  File "<pyshell#304>", line 1, in <module>
    c.talk(1, 2)
TypeError: talk() takes exactly 1 argument (3 given)
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/oop.py ==============
Woof! Fido is barking
Woof! Clifford is barking
Meow. Socks is purring

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/oop.py", line 35, in <module>
    pet.talk()
AttributeError: 'int' object has no attribute 'talk'
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/oop.py ==============
Woof! Fido is barking
Woof! Clifford is barking
Meow. Socks is purring
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/oop.py ==============
Woof! Fido is barking
Woof! Clifford is barking
Meow. Socks is purring
>>> 
>>> a.foo()

Traceback (most recent call last):
  File "<pyshell#306>", line 1, in <module>
    a.foo()
TypeError: foo() takes no arguments (1 given)
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/oop.py ==============
Woof! Fido is barking
Woof! Clifford is barking
Meow. Socks is purring
>>> a.foo(1, 2)

Traceback (most recent call last):
  File "<pyshell#307>", line 1, in <module>
    a.foo(1, 2)
TypeError: foo() takes exactly 2 arguments (3 given)
>>> a.foo(1)

Traceback (most recent call last):
  File "<pyshell#308>", line 1, in <module>
    a.foo(1)
  File "/Users/mike/teaching/2016-09-19/oop.py", line 25, in foo
    print a + b
TypeError: unsupported operand type(s) for +: 'instance' and 'int'
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/oop.py ==============
Woof! Fido is barking

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/oop.py", line 39, in <module>
    pet.talk()
  File "/Users/mike/teaching/2016-09-19/oop.py", line 22, in talk
    print 'Woof! %s is barking' % self.name
AttributeError: Dog instance has no attribute 'name'
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/oop.py ==============
Woof! Fido is barking
Woof! Clifford is barking
Meow. Socks is purring
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/oop.py ==============

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/oop.py", line 39, in <module>
    dog_initialize(a, 'Fido')
NameError: name 'dog_initialize' is not defined
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/oop.py ==============
Woof! Fido is barking
Woof! Clifford is barking
Meow. Socks is purring

============== RESTART: /Users/mike/teaching/2016-09-19/oop.py ==============

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/oop.py", line 38, in <module>
    c = Cat('Socks')
  File "/Users/mike/teaching/2016-09-19/oop.py", line 31, in __init__
    cat.name = name
NameError: global name 'cat' is not defined
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/oop.py ==============
Woof! Fido is barking
Woof! Clifford is barking
Meow. Socks is purring
>>> 
>>> 
>>> # lunch until 1:10pm
>>> 
>>> 
>>> dir(int)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
>>> abs(-5)
5
>>> class Foo:
	def __abs__(self):
		return 'hello'

	
>>> x = Foo()
>>> abs(x)
'hello'
>>> 
>>> 0 and 5
0
>>> 
>>> 
>>> class Foo:
	def __abs__(self):
		return 'hello'
	def __and__(self, other):
		return 'wahoo'

	
>>> Foo() & 5
'wahoo'
>>> 
>>> 
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
>>> 
>>> 
>>> a = Dog('Fido')
>>> a.bark()
Woof! Fido is barking
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
>>> a
<__main__.Dog instance at 0x1039ad248>
>>> 
>>> 
>>> 
>>> import dog
>>> dog
<module 'dog' from '/Users/mike/teaching/2016-09-19/dog.py'>
>>> dog.a
<dog.Dog instance at 0x1039a7b00>
>>> 
>>> dir()
['Dog', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'a', 'dog']
>>> __name__
'__main__'
>>> 
>>> dir(dog)
['Dog', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'a']
>>> dog.__doc__
'\nDemonstrating a few magic methods.\n'
>>> help(dog)
Help on module dog:

NAME
    dog - Demonstrating a few magic methods.

FILE
    /Users/mike/teaching/2016-09-19/dog.py

CLASSES
    Dog
    
    class Dog
     |  our best friends
     |  
     |  Methods defined here:
     |  
     |  __init__(self, name)
     |  
     |  bark(self)

DATA
    a = <dog.Dog instance>


>>> dog.__name__
'dog'
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
>>> 
>>> import dog
my name is dog
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script/application
>>> 
>>> import dog
my name is dog
imported as a module
>>> dog.__dict__
{'a': <dog.Dog instance at 0x1039ad878>, '__builtins__': {'bytearray': <type 'bytearray'>, 'IndexError': <type 'exceptions.IndexError'>, 'all': <built-in function all>, 'help': Type help() for interactive help, or help(object) for help about object., 'vars': <built-in function vars>, 'SyntaxError': <type 'exceptions.SyntaxError'>, 'unicode': <type 'unicode'>, 'UnicodeDecodeError': <type 'exceptions.UnicodeDecodeError'>, 'memoryview': <type 'memoryview'>, 'isinstance': <built-in function isinstance>, 'copyright': Copyright (c) 2001-2016 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved., 'NameError': <type 'exceptions.NameError'>, 'BytesWarning': <type 'exceptions.BytesWarning'>, 'dict': <type 'dict'>, 'input': <built-in function input>, 'oct': <built-in function oct>, 'bin': <built-in function bin>, 'SystemExit': <type 'exceptions.SystemExit'>, 'StandardError': <type 'exceptions.StandardError'>, 'format': <built-in function format>, 'repr': <built-in function repr>, 'sorted': <built-in function sorted>, 'False': False, 'RuntimeWarning': <type 'exceptions.RuntimeWarning'>, 'list': <type 'list'>, 'iter': <built-in function iter>, 'reload': <built-in function reload>, 'Warning': <type 'exceptions.Warning'>, '__package__': None, 'round': <built-in function round>, 'dir': <built-in function dir>, 'cmp': <built-in function cmp>, 'set': <type 'set'>, 'bytes': <type 'str'>, 'reduce': <built-in function reduce>, 'intern': <built-in function intern>, 'issubclass': <built-in function issubclass>, 'Ellipsis': Ellipsis, 'EOFError': <type 'exceptions.EOFError'>, 'locals': <built-in function locals>, 'BufferError': <type 'exceptions.BufferError'>, 'slice': <type 'slice'>, 'FloatingPointError': <type 'exceptions.FloatingPointError'>, 'sum': <built-in function sum>, 'getattr': <built-in function getattr>, 'abs': <built-in function abs>, 'exit': Use exit() or Ctrl-D (i.e. EOF) to exit, 'print': <built-in function print>, 'True': True, 'FutureWarning': <type 'exceptions.FutureWarning'>, 'ImportWarning': <type 'exceptions.ImportWarning'>, 'None': None, 'hash': <built-in function hash>, 'ReferenceError': <type 'exceptions.ReferenceError'>, 'len': <built-in function len>, 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information., 'frozenset': <type 'frozenset'>, '__name__': '__builtin__', 'ord': <built-in function ord>, 'super': <type 'super'>, '_': None, 'TypeError': <type 'exceptions.TypeError'>, 'license': Type license() to see the full license text, 'KeyboardInterrupt': <type 'exceptions.KeyboardInterrupt'>, 'UserWarning': <type 'exceptions.UserWarning'>, 'filter': <built-in function filter>, 'range': <built-in function range>, 'staticmethod': <type 'staticmethod'>, 'SystemError': <type 'exceptions.SystemError'>, 'BaseException': <type 'exceptions.BaseException'>, 'pow': <built-in function pow>, 'RuntimeError': <type 'exceptions.RuntimeError'>, 'float': <type 'float'>, 'MemoryError': <type 'exceptions.MemoryError'>, 'StopIteration': <type 'exceptions.StopIteration'>, 'globals': <built-in function globals>, 'divmod': <built-in function divmod>, 'enumerate': <type 'enumerate'>, 'apply': <built-in function apply>, 'LookupError': <type 'exceptions.LookupError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-D (i.e. EOF) to exit, 'basestring': <type 'basestring'>, 'UnicodeError': <type 'exceptions.UnicodeError'>, 'zip': <built-in function zip>, 'hex': <built-in function hex>, 'long': <type 'long'>, 'next': <built-in function next>, 'ImportError': <type 'exceptions.ImportError'>, 'chr': <built-in function chr>, 'xrange': <type 'xrange'>, 'type': <type 'type'>, '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", 'Exception': <type 'exceptions.Exception'>, 'tuple': <type 'tuple'>, 'UnicodeTranslateError': <type 'exceptions.UnicodeTranslateError'>, 'reversed': <type 'reversed'>, 'UnicodeEncodeError': <type 'exceptions.UnicodeEncodeError'>, 'IOError': <type 'exceptions.IOError'>, 'hasattr': <built-in function hasattr>, 'delattr': <built-in function delattr>, 'setattr': <built-in function setattr>, 'raw_input': <built-in function raw_input>, 'SyntaxWarning': <type 'exceptions.SyntaxWarning'>, 'compile': <built-in function compile>, 'ArithmeticError': <type 'exceptions.ArithmeticError'>, 'str': <type 'str'>, 'property': <type 'property'>, 'GeneratorExit': <type 'exceptions.GeneratorExit'>, 'int': <type 'int'>, '__import__': <built-in function __import__>, 'KeyError': <type 'exceptions.KeyError'>, 'coerce': <built-in function coerce>, 'PendingDeprecationWarning': <type 'exceptions.PendingDeprecationWarning'>, 'file': <type 'file'>, 'EnvironmentError': <type 'exceptions.EnvironmentError'>, 'unichr': <built-in function unichr>, 'id': <built-in function id>, 'OSError': <type 'exceptions.OSError'>, 'DeprecationWarning': <type 'exceptions.DeprecationWarning'>, 'min': <built-in function min>, 'UnicodeWarning': <type 'exceptions.UnicodeWarning'>, 'execfile': <built-in function execfile>, 'any': <built-in function any>, 'complex': <type 'complex'>, 'bool': <type 'bool'>, 'ValueError': <type 'exceptions.ValueError'>, 'NotImplemented': NotImplemented, 'map': <built-in function map>, 'buffer': <type 'buffer'>, 'max': <built-in function max>, 'object': <type 'object'>, 'TabError': <type 'exceptions.TabError'>, 'callable': <built-in function callable>, 'ZeroDivisionError': <type 'exceptions.ZeroDivisionError'>, 'eval': <built-in function eval>, '__debug__': True, 'IndentationError': <type 'exceptions.IndentationError'>, 'AssertionError': <type 'exceptions.AssertionError'>, 'classmethod': <type 'classmethod'>, 'UnboundLocalError': <type 'exceptions.UnboundLocalError'>, 'NotImplementedError': <type 'exceptions.NotImplementedError'>, 'AttributeError': <type 'exceptions.AttributeError'>, 'OverflowError': <type 'exceptions.OverflowError'>}, '__file__': '/Users/mike/teaching/2016-09-19/dog.py', 'Dog': <class dog.Dog at 0x103a48530>, '__package__': None, '__name__': 'dog', '__doc__': '\nDemonstrating a few magic methods.\n'}
>>> dog.__dict__.keys()
['a', '__builtins__', '__file__', 'Dog', '__package__', '__name__', '__doc__']
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script/application
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
>>> a
<__main__.Dog instance at 0x1039ad248>
>>> 
>>> 
>>> import dog
>>> dog.a

Traceback (most recent call last):
  File "<pyshell#362>", line 1, in <module>
    dog.a
AttributeError: 'module' object has no attribute 'a'
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
>>> dog.__doc__

Traceback (most recent call last):
  File "<pyshell#363>", line 1, in <module>
    dog.__doc__
NameError: name 'dog' is not defined
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
>>> 
>>> __doc__
'\nDemonstrating a few magic methods.\n'
>>> i

Traceback (most recent call last):
  File "<pyshell#366>", line 1, in <module>
    i
NameError: name 'i' is not defined
>>> 
>>> 
>>> import dog
>>> 
>>> help(dog)
Help on module dog:

NAME
    dog - Demonstrating a few magic methods.

FILE
    /Users/mike/teaching/2016-09-19/dog.py

CLASSES
    Dog
    
    class Dog
     |  our best friends
     |  
     |  Methods defined here:
     |  
     |  __init__(self, name)
     |  
     |  bark(self)


>>> dir(dog)
['Dog', '__builtins__', '__doc__', '__file__', '__name__', '__package__']
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> 
>>> 
>>> a
<__main__.Dog instance at 0x1039ad248>
>>> a.bark()
Woof! Fido is barking
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> a
Dog(Fido)
>>> Dog(Fido)

Traceback (most recent call last):
  File "<pyshell#378>", line 1, in <module>
    Dog(Fido)
NameError: name 'Fido' is not defined
>>> 
>>> 
>>> s = 'a \t b'
>>> s
'a \t b'
>>> print s
a 	 b
>>> print str(s)
a 	 b
>>> print repr(s)
'a \t b'
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> a
Dog('Fido')
>>> Dog('Fido')
Dog('Fido')
>>> int
<type 'int'>
>>> <type 'int'>
SyntaxError: invalid syntax
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> 
>>> a + b
Dog('Fido, Jr.')
>>> b + a
Dog('Fluffy, Jr.')
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> 
>>> 
>>> a == b
False
>>> a == a
True
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> a == b
False
>>> a == Dog('Fido')
True
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> a == Dog('Fido')
False
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> a == Dog('Fido')
True
>>> 
>>> 
>>> # == < > <= >= !=
>>> dir(float)
['__abs__', '__add__', '__class__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__int__', '__le__', '__long__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__pos__', '__pow__', '__radd__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__setformat__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
>>> dir(int)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
>>> 
>>> cmp(5, 10)
-1
>>> cmp(10, 5)
1
>>> cmp(10, 10)
0
>>> int()0.5
SyntaxError: invalid syntax
>>> int(0.5)
0
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> 
>>> a < b
True
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> 
>>> a == b
False
>>> a == a
False
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> 
>>> dir(set)
['__and__', '__class__', '__cmp__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> cmp(set(), set())

Traceback (most recent call last):
  File "<pyshell#419>", line 1, in <module>
    cmp(set(), set())
TypeError: cannot compare sets using cmp()
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> 
>>> 
>>> a
Dog('Fido')
>>> b
Dog('Fluffy')
>>> 
>>> 
>>> 'Fido' < 'Fluffy'
True
>>> a < b
True
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> k
<__main__.Kennel instance at 0x1039ae4d0>
>>> k.dogs
[Dog('Fido'), Dog('Fluffy'), Dog('Clifford')]
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> k
Kennel([Dog('Fido'), Dog('Fluffy'), Dog('Clifford')])
>>> Kennel([Dog('Fido'), Dog('Fluffy'), Dog('Clifford')])

Traceback (most recent call last):
  File "<pyshell#431>", line 1, in <module>
    Kennel([Dog('Fido'), Dog('Fluffy'), Dog('Clifford')])
TypeError: __init__() takes exactly 1 argument (2 given)
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/dog.py", line 45, in <module>
    k = Kennel()
TypeError: __init__() takes exactly 2 arguments (1 given)
>>> Kennel([Dog('Fido'), Dog('Fluffy'), Dog('Clifford')])
Kennel([Dog('Fido'), Dog('Fluffy'), Dog('Clifford')])
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> k
Kennel([Dog('Fido'), Dog('Fluffy'), Dog('Clifford')])
>>> Kennel([Dog('Fido'), Dog('Fluffy'), Dog('Clifford')])
Kennel([Dog('Fido'), Dog('Fluffy'), Dog('Clifford')])
>>> 
>>> 
>>> j = Kennel()
>>> j
Kennel([Dog('Fido'), Dog('Fluffy'), Dog('Clifford')])
>>> 
>>> Kennel.__init__
<unbound method Kennel.__init__>
>>> Kennel.__init__.__defaults__
([Dog('Fido'), Dog('Fluffy'), Dog('Clifford')],)
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> 
>>> 
>>> k
Kennel([Dog('Fido'), Dog('Fluffy'), Dog('Clifford')])
>>> 
>>> j = Kennel()
>>> j
Kennel([])
>>> 
>>> k.dogs[0]
Dog('Fido')
>>> 
>>> k[0]

Traceback (most recent call last):
  File "<pyshell#451>", line 1, in <module>
    k[0]
AttributeError: Kennel instance has no attribute '__getitem__'
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> k[0]
Dog('Fido')
>>> k[1]
Dog('Fluffy')
>>> k[2]
Dog('Clifford')
>>> k[3]

Traceback (most recent call last):
  File "<pyshell#455>", line 1, in <module>
    k[3]
  File "/Users/mike/teaching/2016-09-19/dog.py", line 41, in __getitem__
    return self.dogs[index]
IndexError: list index out of range
>>> 
>>> 
>>> k[:2]
[Dog('Fido'), Dog('Fluffy')]
>>> for dog in k:
	print dog

	
Dog('Fido')
Dog('Fluffy')
Dog('Clifford')
>>> 
>>> 
>>> len(k)

Traceback (most recent call last):
  File "<pyshell#464>", line 1, in <module>
    len(k)
AttributeError: Kennel instance has no attribute '__len__'
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> len(k)
3
>>> 
>>> len(k[0].name)
4
>>> 
>>> Kennel
<class __main__.Kennel at 0x103a5d598>
>>> 
>>> 
>>> 
>>> class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def _
KeyboardInterrupt
>>> 
>>> 
>>> origin = (0, 0)
>>> origin
(0, 0)
>>> origin.x

Traceback (most recent call last):
  File "<pyshell#482>", line 1, in <module>
    origin.x
AttributeError: 'tuple' object has no attribute 'x'
>>> origin.y

Traceback (most recent call last):
  File "<pyshell#483>", line 1, in <module>
    origin.y
AttributeError: 'tuple' object has no attribute 'y'
>>> 
>>> 
>>> from collections import namedtuple
>>> 
>>> 
>>> Kennel
<class __main__.Kennel at 0x103a5d598>
>>> 
>>> 
>>> namedtuple('Point', 'x y')
<class '__main__.Point'>
>>> Point = namedtuple('Point', ['x', 'y'])
>>> Point
<class '__main__.Point'>
>>> 
>>> a = Point(3, 5)
>>> a
Point(x=3, y=5)
>>> a.x
3
>>> a.y
5
>>> a == (3, 5)
True
>>> P = namedtuple('Point', 'x y')
>>> P
<class '__main__.Point'>
>>> help(Point)
Help on class Point in module __main__:

class Point(__builtin__.tuple)
 |  Point(x, y)
 |  
 |  Method resolution order:
 |      Point
 |      __builtin__.tuple
 |      __builtin__.object
 |  
 |  Methods defined here:
 |  
 |  __getnewargs__(self)
 |      Return self as a plain tuple.  Used by copy and pickle.
 |  
 |  __getstate__(self)
 |      Exclude the OrderedDict from pickling
 |  
 |  __repr__(self)
 |      Return a nicely formatted representation string
 |  
 |  _asdict(self)
 |      Return a new OrderedDict which maps field names to their values
 |  
 |  _replace(_self, **kwds)
 |      Return a new Point object replacing specified fields with new values
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  _make(cls, iterable, new=<built-in method __new__ of type object>, len=<built-in function len>) from __builtin__.type
 |      Make a new Point object from a sequence or iterable
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(_cls, x, y)
 |      Create new instance of Point(x, y)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      Return a new OrderedDict which maps field names to their values
 |  
 |  x
 |      Alias for field number 0
 |  
 |  y
 |      Alias for field number 1
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  _fields = ('x', 'y')
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from __builtin__.tuple:
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __getslice__(...)
 |      x.__getslice__(i, j) <==> x[i:j]
 |      
 |      Use of negative indices is not supported.
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __hash__(...)
 |      x.__hash__() <==> hash(x)
 |  
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __mul__(...)
 |      x.__mul__(n) <==> x*n
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __rmul__(...)
 |      x.__rmul__(n) <==> n*x
 |  
 |  count(...)
 |      T.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.

>>> a.x = 10

Traceback (most recent call last):
  File "<pyshell#504>", line 1, in <module>
    a.x = 10
AttributeError: can't set attribute
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/oop.py ==============
Woof! Fido is barking
Woof! Clifford is barking
Meow. Socks is purring
>>> 
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> class Animal:
	def __init__(self, name):
		self.name = name
	def speak(self):
		print self.name

		
>>> pika = Animal('Pikachu')
>>> pika.speak()
Pikachu
>>> pika.speak()
Pikachu
>>> pika.speak()
Pikachu
>>> 
>>> class Bird(Animal):
	def fly(self):
		print 'whoosh'

		
>>> class Eagle(Bird):
	'majestic'

	
>>> class Condor(Bird):
	'large'

	
>>> class Penguin(Bird):
	def swim(self):
		print 'splash'

		
>>> p = Penguin('Tux')
>>> p.swim()
splash
>>> p.speak()
Tux
>>> p.fly()
whoosh
>>> class Penguin(Bird):
	def swim(self):
		print 'splash'
	def fly(self):
		raise NotImplementedError('Penguins cannot fly')

	
>>> class Mammal(Animal):
	def live_birth(self):
		print 'and has hair'

		
>>> class Human(Mammal):
	'smart'

	
>>> class Buffalo(Mammal):
	'extinct'

	
>>> class Platypus(Mammal):
	'weird'
	def lays_eggs(self):
		print 'and is poisonous and has webbed feet'

		
>>> class Platypus(Mammal):
	'weird'
	def lays_eggs(self):
		print 'and is poisonous and has webbed feet'
	def live_birth(self):
		raise NotImplementedError('grrr')

	
>>> 
>>> 
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
>>> 
>>> 
>>> 
>>> range(5)
[0, 1, 2, 3, 4]
>>> 
>>> range(5, 10)
[5, 6, 7, 8, 9]
>>> 
>>> range(5, 50, 10)
[5, 15, 25, 35, 45]
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
>>> 5
5
>>> 
>>> 
>>> range(5)
[0, 1, 2, 3, 4]
>>> myrange(5)
[0, 1, 2, 3, 4]
>>> 
>>> range(0)
[]
>>> myrange(0)
[]
>>> range('a')

Traceback (most recent call last):
  File "<pyshell#581>", line 1, in <module>
    range('a')
TypeError: range() integer end argument expected, got str.
>>> myrange('a')

=============================== RESTART: Shell ===============================
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
>>> 
>>> myrange('a')

Traceback (most recent call last):
  File "<pyshell#584>", line 1, in <module>
    myrange('a')
  File "/Users/mike/teaching/2016-09-19/iteration.py", line 43, in myrange
    raise TypeError('expected an int, got %r', stop.__class__.__name__)
TypeError: ('expected an int, got %r', 'str')
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
>>> myrange('a')

Traceback (most recent call last):
  File "<pyshell#585>", line 1, in <module>
    myrange('a')
  File "/Users/mike/teaching/2016-09-19/iteration.py", line 43, in myrange
    raise TypeError('expected an int, got %r' % stop.__class__.__name__)
TypeError: expected an int, got 'str'
>>> range('a')

Traceback (most recent call last):
  File "<pyshell#586>", line 1, in <module>
    range('a')
TypeError: range() integer end argument expected, got str.
>>> 5 < 'a'
True
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
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
>>> range(5)
[0, 1, 2, 3, 4]
>>> range(5, 10)
[5, 6, 7, 8, 9]
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
>>> myrange(5, 10)
[5, 6, 7, 8, 9]
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
>>> myrange(5)
[0, 1, 2, 3, 4]
>>> myrange(5, 10)
[5, 6, 7, 8, 9]
>>> 
>>> myrange(-5, 0)
[]
>>> range(-5, 0)
[-5, -4, -3, -2, -1]
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
>>> range(-5, 0)
[-5, -4, -3, -2, -1]
>>> myrange(-5, 0)
[-5, -4, -3, -2, -1]
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
>>> myrange(1, 1, 2)
[]
>>> range(1, 1, 2)
[]
>>> range(1, 1, 0)

Traceback (most recent call last):
  File "<pyshell#601>", line 1, in <module>
    range(1, 1, 0)
ValueError: range() step argument must not be zero
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
>>> 
>>> 
>>> names
['Luke', 'Leia', 'Han', 'Chewie']
>>> 
>>> map(len, names)
[4, 4, 3, 6]
>>> 
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
>>> 
>>> mymap(len, names)
[4, 4, 3, 6]
>>> 
>>> 
>>> len
<built-in function len>
>>> 
>>> len.__call__
<method-wrapper '__call__' of builtin_function_or_method object at 0x1002c4830>
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/dog.py ==============
my name is __main__
executed as a script
>>> 
>>> 
>>> k[0]
Dog('Fido')
>>> 
>>> for dog in k:
	print dog

	
Dog('Fido')
Dog('Fluffy')
Dog('Clifford')
>>> 
>>> 
>>> 
>>> iter(k)
<iterator object at 0x103a4ad90>
>>> 
>>> k[0]
Dog('Fido')
>>> k[1]
Dog('Fluffy')
>>> k[2]
Dog('Clifford')
>>> k[3]

Traceback (most recent call last):
  File "<pyshell#631>", line 1, in <module>
    k[3]
  File "/Users/mike/teaching/2016-09-19/dog.py", line 53, in __getitem__
    return self.dogs[index]
IndexError: list index out of range
>>> 
>>> 
>>> i = 0
>>> while True:
	dog = k[i]
	print dog

	
Dog('Fido')
Dog('Fido')
Dog('Fido')
Dog('Fido')
Dog('Fido')
Dog('Fido')
Dog('Fido')
Dog('Fido')
Dog('Fido')
Dog('Fido')
Dog('Fido')
Dog('Fido')
Dog('Fido')
Dog('Fido')
Dog('Fido')
Dog('Fido')
Dog('Fido')
Dog('Fido')
Dog('Fido')


Traceback (most recent call last):
  File "<pyshell#638>", line 3, in <module>
    print dog
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/idlelib/PyShell.py", line 1356, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> i = 0
>>> while True:
	dog = k[i]
	print dog
	i += 1

	
Dog('Fido')
Dog('Fluffy')
Dog('Clifford')

Traceback (most recent call last):
  File "<pyshell#642>", line 2, in <module>
    dog = k[i]
  File "/Users/mike/teaching/2016-09-19/dog.py", line 53, in __getitem__
    return self.dogs[index]
IndexError: list index out of range
>>> while True:
	try:
		dog = k[i]
	except IndexError:
		break
	print dog
	i += 1

	
>>> i = 0
>>> while True:
	try:
		dog = k[i]
	except IndexError:
		break
	print dog
	i += 1

	
Dog('Fido')
Dog('Fluffy')
Dog('Clifford')
>>> 
>>> 
>>> iterator = iter(k)
>>> iterator
<iterator object at 0x103a63810>
>>> 
>>> next(iterator)
Dog('Fido')
>>> next(iterator)
Dog('Fluffy')
>>> next(iterator)
Dog('Clifford')
>>> 
>>> 
>>> [1, 2, 3, None, 5]
[1, 2, 3, None, 5]
>>> 
>>> next(iterator)

Traceback (most recent call last):
  File "<pyshell#660>", line 1, in <module>
    next(iterator)
StopIteration
>>> 
>>> 
>>> iterator = iter(k)
>>> 
>>> 
>>> 
>>> 
>>> for dog in k:
	print dog

	
Dog('Fido')
Dog('Fluffy')
Dog('Clifford')
>>> 
>>> 
>>> 
>>> iterator = iter(k)
>>> while True:
	try:
		dog = next(iterator)
	except StopIteration:
		break
	print dog

	
Dog('Fido')
Dog('Fluffy')
Dog('Clifford')
>>> 
>>> iterator
<iterator object at 0x103a63810>
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
>>> 
>>> 
>>> iterable = Iterable()
>>> 
>>> iterable[0]
0
>>> iterable['a']
'a'
>>> 
>>> for thing in iterable:
	print thing

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18


Traceback (most recent call last):
  File "<pyshell#693>", line 2, in <module>
    print thing
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/idlelib/PyShell.py", line 1356, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
>>> for thing in Iterable(10):
	print thing

	
0
1
2
3
4
5
6
7
8
9
>>> 
>>> it = iter(Iterable(10))
>>> next(it)
0
>>> next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> it = iter(Iterable(3))
>>> next(it)
0
>>> next(it)
1
>>> next(it)
2
>>> next(it)

Traceback (most recent call last):
  File "<pyshell#706>", line 1, in <module>
    next(it)
StopIteration
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
>>> 
>>> 
>>> it = Iterator(Iterable(5))
>>> next(it)
0
>>> next(it)
0
>>> next(it)
0
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
>>> 
>>> it = Iterator(Iterable(5))
>>> next(it)
0
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
  File "<pyshell#720>", line 1, in <module>
    next(it)
  File "/Users/mike/teaching/2016-09-19/iteration.py", line 101, in next
    value = self.seq[self.current]
  File "/Users/mike/teaching/2016-09-19/iteration.py", line 89, in __getitem__
    raise IndexError(index)
IndexError: 5
>>> 
>>> 5.5e3
5500.0
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
>>> 
>>> 
>>> iter(Iterable(5))
<iterator object at 0x103a4ad10>
>>> 
=========== RESTART: /Users/mike/teaching/2016-09-19/iteration.py ===========
Luke
Leia
Han
Chewie
>>> iter(Iterable(5))
<__main__.Iterator instance at 0x1039ae050>
>>> 
>>> 
>>> 
>>> import inspect
>>> import dis
>>> 
>>> def foo():
	x = 5
	y = x + 2

	
>>> dis.dis(foo)
  2           0 LOAD_CONST               1 (5)
              3 STORE_FAST               0 (x)

  3           6 LOAD_FAST                0 (x)
              9 LOAD_CONST               2 (2)
             12 BINARY_ADD          
             13 STORE_FAST               1 (y)
             16 LOAD_CONST               0 (None)
             19 RETURN_VALUE        
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/kaprekar.py ============
>>> 
>>> step
<function step at 0x1007012a8>
>>> 
>>> x = 2516
>>> 
>>> sorted(x)

Traceback (most recent call last):
  File "<pyshell#743>", line 1, in <module>
    sorted(x)
TypeError: 'int' object is not iterable
>>> 
>>> list(x)

Traceback (most recent call last):
  File "<pyshell#745>", line 1, in <module>
    list(x)
TypeError: 'int' object is not iterable
>>> 
>>> str(x)
'2516'
>>> sorted(str(x))
['1', '2', '5', '6']
>>> 
>>> 
>>> sorted(str(x), reverse=True)
['6', '5', '2', '1']
>>> sorted(str(x), reverse=True) - sorted(str(x))

Traceback (most recent call last):
  File "<pyshell#752>", line 1, in <module>
    sorted(str(x), reverse=True) - sorted(str(x))
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> 
>>> int(sorted(str(x)))

Traceback (most recent call last):
  File "<pyshell#754>", line 1, in <module>
    int(sorted(str(x)))
TypeError: int() argument must be a string or a number, not 'list'
>>> 
>>> str(sorted(str(x)))
"['1', '2', '5', '6']"
>>> int(str(sorted(str(x))))

Traceback (most recent call last):
  File "<pyshell#757>", line 1, in <module>
    int(str(sorted(str(x))))
ValueError: invalid literal for int() with base 10: "['1', '2', '5', '6']"
>>> 
>>> sorted(str(x))
['1', '2', '5', '6']
>>> 
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(str.join)
Help on method_descriptor:

join(...)
    S.join(iterable) -> string
    
    Return a string which is the concatenation of the strings in the
    iterable.  The separator between elements is S.

>>> 
>>> ['list', 'of', 'strings'].join(',')

Traceback (most recent call last):
  File "<pyshell#764>", line 1, in <module>
    ['list', 'of', 'strings'].join(',')
AttributeError: 'list' object has no attribute 'join'
>>> ','.join(['list', 'of', 'strings'])
'list,of,strings'
>>> 
>>> 
>>> sorted(str(x)).join('')

Traceback (most recent call last):
  File "<pyshell#768>", line 1, in <module>
    sorted(str(x)).join('')
AttributeError: 'list' object has no attribute 'join'
>>> ''.join(sorted(str(x)))
'1256'
>>> x
2516
>>> ''.join(sorted(str(x)))
'1256'
>>> 
>>> 
>>> sorted(x)

Traceback (most recent call last):
  File "<pyshell#774>", line 1, in <module>
    sorted(x)
TypeError: 'int' object is not iterable
>>> str(x)
'2516'
>>> ''.join(sorted(str(x)))
'1256'
>>> int(''.join(sorted(str(x))))
1256
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/kaprekar.py ============
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/kaprekar.py ============
>>> step(2516)
5265
>>> step(5265)
3996
>>> step(3996)
6264
>>> step(6264)
4176
>>> step(4176)
6174
>>> step(6174)
6174
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/kaprekar.py ============
**********************************************************************
File "/Users/mike/teaching/2016-09-19/kaprekar.py", line 17, in __main__.step
Failed example:
    step(6174)
Expected:
    6173
Got:
    6174
**********************************************************************
1 items had failures:
   1 of   3 in __main__.step
***Test Failed*** 1 failures.
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/kaprekar.py ============
>>> 
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/kaprekar.py ============
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/kaprekar.py ============
**********************************************************************
File "/Users/mike/teaching/2016-09-19/kaprekar.py", line 19, in __main__.step
Failed example:
    step(1234)
Expected:
    3087 
Got:
    3087
**********************************************************************
1 items had failures:
   1 of   4 in __main__.step
***Test Failed*** 1 failures.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> graph = {}
>>> for i in range(10000):
	graph[i] = step(i)

	
>>> len(graph)
10000
>>> graph[6174]
6174
>>> graph[2516]
5265
>>> 
>>> 
>>> step(0)
0
>>> step(18)
63
>>> 
>>> 
>>> 
>>> 
>>> # leafs leaves
>>> 
>>> 
>>> len(graph.values())
10000
>>> 
>>> len(set(graph.values()))
73
>>> set(graph.values())
set([0, 2178, 4995, 4356, 7173, 6534, 9351, 7533, 9, 396, 3087, 5265, 18, 7443, 9621, 792, 2997, 27, 3996, 9711, 6174, 8991, 8352, 36, 8262, 2088, 297, 4266, 7083, 6444, 45, 8622, 8712, 693, 54, 5175, 7992, 7353, 9531, 63, 1089, 3267, 6084, 5445, 198, 7623, 72, 9801, 1998, 4176, 81, 594, 9171, 8532, 9261, 5085, 6993, 7263, 9441, 99, 999, 6354, 3177, 5994, 5355, 8172, 8082, 495, 4086, 6264, 9081, 8442, 891])
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/kaprekar.py ============
digraph {
}
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/kaprekar.py ============
digraph {
0 -> 0
2178 -> 7443
4995 -> 5355
4356 -> 3087
7173 -> 6354
6534 -> 3087
9351 -> 8172
7533 -> 4176
9 -> 0
396 -> 594
3087 -> 8352
5265 -> 3996
18 -> 63
7443 -> 3996
9621 -> 8352
792 -> 693
2997 -> 7173
27 -> 45
3996 -> 6264
9711 -> 8532
6174 -> 6174
8991 -> 8082
8352 -> 6174
36 -> 27
8262 -> 6354
2088 -> 8532
297 -> 693
4266 -> 4176
7083 -> 8352
6444 -> 1998
45 -> 9
8622 -> 6354
8712 -> 7443
693 -> 594
54 -> 9
5175 -> 5994
7992 -> 7173
7353 -> 4176
9531 -> 8172
63 -> 27
1089 -> 9621
3267 -> 5265
6084 -> 8172
5445 -> 1089
198 -> 792
7623 -> 5265
72 -> 45
9801 -> 9621
1998 -> 8082
4176 -> 6174
81 -> 63
594 -> 495
9171 -> 8532
8532 -> 6174
9261 -> 8352
5085 -> 7992
6993 -> 6264
7263 -> 5265
9441 -> 7992
99 -> 0
999 -> 0
6354 -> 3087
3177 -> 6354
5994 -> 5355
5355 -> 1998
8172 -> 7443
8082 -> 8532
495 -> 495
4086 -> 8172
6264 -> 4176
9081 -> 9621
8442 -> 5994
891 -> 792
}
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/kaprekar.py ============
digraph {
0 -> 0
9 -> 0
18 -> 63
27 -> 45
36 -> 27
45 -> 9
54 -> 9
63 -> 27
72 -> 45
81 -> 63
99 -> 0
198 -> 792
297 -> 693
396 -> 594
495 -> 495
594 -> 495
693 -> 594
792 -> 693
891 -> 792
999 -> 0
1089 -> 9621
1998 -> 8082
2088 -> 8532
2178 -> 7443
2997 -> 7173
3087 -> 8352
3177 -> 6354
3267 -> 5265
3996 -> 6264
4086 -> 8172
4176 -> 6174
4266 -> 4176
4356 -> 3087
4995 -> 5355
5085 -> 7992
5175 -> 5994
5265 -> 3996
5355 -> 1998
5445 -> 1089
5994 -> 5355
6084 -> 8172
6174 -> 6174
6264 -> 4176
6354 -> 3087
6444 -> 1998
6534 -> 3087
6993 -> 6264
7083 -> 8352
7173 -> 6354
7263 -> 5265
7353 -> 4176
7443 -> 3996
7533 -> 4176
7623 -> 5265
7992 -> 7173
8082 -> 8532
8172 -> 7443
8262 -> 6354
8352 -> 6174
8442 -> 5994
8532 -> 6174
8622 -> 6354
8712 -> 7443
8991 -> 8082
9081 -> 9621
9171 -> 8532
9261 -> 8352
9351 -> 8172
9441 -> 7992
9531 -> 8172
9621 -> 8352
9711 -> 8532
9801 -> 9621
}
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/kaprekar.py ============
digraph {
0000 -> 0000
0999 -> 8991
1089 -> 9621
1998 -> 8082
2088 -> 8532
2178 -> 7443
2997 -> 7173
3087 -> 8352
3177 -> 6354
3267 -> 5265
3996 -> 6264
4086 -> 8172
4176 -> 6174
4266 -> 4176
4356 -> 3087
4995 -> 5355
5085 -> 7992
5175 -> 5994
5265 -> 3996
5355 -> 1998
5445 -> 1089
5994 -> 5355
6084 -> 8172
6174 -> 6174
6264 -> 4176
6354 -> 3087
6444 -> 1998
6534 -> 3087
6993 -> 6264
7083 -> 8352
7173 -> 6354
7263 -> 5265
7353 -> 4176
7443 -> 3996
7533 -> 4176
7623 -> 5265
7992 -> 7173
8082 -> 8532
8172 -> 7443
8262 -> 6354
8352 -> 6174
8442 -> 5994
8532 -> 6174
8622 -> 6354
8712 -> 7443
8991 -> 8082
9081 -> 9621
9171 -> 8532
9261 -> 8352
9351 -> 8172
9441 -> 7992
9531 -> 8172
9621 -> 8352
9711 -> 8532
9801 -> 9621
}
>>> 
>>> 
>>> graph = {}
>>> for i in range(10000):
	graph[i] = step(i)

	
>>> non_leaves = set(graph.values())
>>> 
>>> 
>>> 
>>> set().add(5)
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/kaprekar.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/kaprekar.py", line 58, in <module>
    gen_graph()
  File "/Users/mike/teaching/2016-09-19/kaprekar.py", line 44, in gen_graph
    groups[target].add(leaf)
KeyError: '3996'
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/kaprekar.py ============

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/kaprekar.py", line 60, in <module>
    gen_graph()
  File "/Users/mike/teaching/2016-09-19/kaprekar.py", line 46, in gen_graph
    groups[target].add(leaf)
KeyError: '3996'
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/kaprekar.py ============

        digraph {
        graph [rankdir="LR"];
    
0000 -> 0000
0999 -> 8991
1089 -> 9621
1998 -> 8082
2088 -> 8532
2178 -> 7443
2997 -> 7173
3087 -> 8352
3177 -> 6354
3267 -> 5265
3996 -> 6264
4086 -> 8172
4176 -> 6174
4266 -> 4176
4356 -> 3087
4995 -> 5355
5085 -> 7992
5175 -> 5994
5265 -> 3996
5355 -> 1998
5445 -> 1089
5994 -> 5355
6084 -> 8172
6174 -> 6174
6264 -> 4176
6354 -> 3087
6444 -> 1998
6534 -> 3087
6993 -> 6264
7083 -> 8352
7173 -> 6354
7263 -> 5265
7353 -> 4176
7443 -> 3996
7533 -> 4176
7623 -> 5265
7992 -> 7173
8082 -> 8532
8172 -> 7443
8262 -> 6354
8352 -> 6174
8442 -> 5994
8532 -> 6174
8622 -> 6354
8712 -> 7443
8991 -> 8082
9081 -> 9621
9171 -> 8532
9261 -> 8352
9351 -> 8172
9441 -> 7992
9531 -> 8172
9621 -> 8352
9711 -> 8532
9801 -> 9621
}
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/kaprekar.py ============

        digraph {
        graph [rankdir="LR"];
    
0000 -> 0000;
0999 -> 8991;
1089 -> 9621;
1998 -> 8082;
2088 -> 8532;
2178 -> 7443;
2997 -> 7173;
3087 -> 8352;
3177 -> 6354;
3267 -> 5265;
3996 -> 6264;
4086 -> 8172;
4176 -> 6174;
4266 -> 4176;
4356 -> 3087;
4995 -> 5355;
5085 -> 7992;
5175 -> 5994;
5265 -> 3996;
5355 -> 1998;
5445 -> 1089;
5994 -> 5355;
6084 -> 8172;
6174 -> 6174;
6264 -> 4176;
6354 -> 3087;
6444 -> 1998;
6534 -> 3087;
6993 -> 6264;
7083 -> 8352;
7173 -> 6354;
7263 -> 5265;
7353 -> 4176;
7443 -> 3996;
7533 -> 4176;
7623 -> 5265;
7992 -> 7173;
8082 -> 8532;
8172 -> 7443;
8262 -> 6354;
8352 -> 6174;
8442 -> 5994;
8532 -> 6174;
8622 -> 6354;
8712 -> 7443;
8991 -> 8082;
9081 -> 9621;
9171 -> 8532;
9261 -> 8352;
9351 -> 8172;
9441 -> 7992;
9531 -> 8172;
9621 -> 8352;
9711 -> 8532;
9801 -> 9621;
}
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/kaprekar.py ============

        digraph {
        graph [rankdir="LR"];
    
0000 -> 0000;
0999 -> 8991;
1089 -> 9621;
1998 -> 8082;
2088 -> 8532;
2178 -> 7443;
2997 -> 7173;
3087 -> 8352;
3177 -> 6354;
3267 -> 5265;
3996 -> 6264;
4086 -> 8172;
4176 -> 6174;
4266 -> 4176;
4356 -> 3087;
4995 -> 5355;
5085 -> 7992;
5175 -> 5994;
5265 -> 3996;
5355 -> 1998;
5445 -> 1089;
5994 -> 5355;
6084 -> 8172;
6174 -> 6174;
6264 -> 4176;
6354 -> 3087;
6444 -> 1998;
6534 -> 3087;
6993 -> 6264;
7083 -> 8352;
7173 -> 6354;
7263 -> 5265;
7353 -> 4176;
7443 -> 3996;
7533 -> 4176;
7623 -> 5265;
7992 -> 7173;
8082 -> 8532;
8172 -> 7443;
8262 -> 6354;
8352 -> 6174;
8442 -> 5994;
8532 -> 6174;
8622 -> 6354;
8712 -> 7443;
8991 -> 8082;
9081 -> 9621;
9171 -> 8532;
9261 -> 8352;
9351 -> 8172;
9441 -> 7992;
9531 -> 8172;
9621 -> 8352;
9711 -> 8532;
9801 -> 9621;
0049, 0094, 0159 ... -> 9351 [label=120];
0039, 0093, 0149 ... -> 9261 [label=144];
0027, 0072, 0137 ... -> 7173 [label=358];
0014, 0041, 0104 ... -> 4086 [label=432];
0028, 0082, 0138 ... -> 8172 [label=284];
0078, 0087, 0188 ... -> 8622 [label=48];
0045, 0054, 0155 ... -> 5355 [label=118];
0012, 0021, 0102 ... -> 2088 [label=192];
0034, 0043, 0144 ... -> 4266 [label=144];
0055, 0505, 0550 ... -> 5445 [label=30];
0058, 0085, 0168 ... -> 8442 [label=144];
0016, 0061, 0106 ... -> 6084 [label=480];
0048, 0084, 0158 ... -> 8352 [label=188];
0036, 0063, 0146 ... -> 6264 [label=286];
0025, 0052, 0135 ... -> 5175 [label=360];
0079, 0097, 0189 ... -> 9621 [label=45];
0046, 0064, 0156 ... -> 6354 [label=188];
0037, 0073, 0147 ... -> 7263 [label=288];
0088, 0808, 0880 ... -> 8712 [label=12];
0068, 0086, 0178 ... -> 8532 [label=92];
0038, 0083, 0148 ... -> 8262 [label=240];
0004, 0040, 0114 ... -> 3996 [label=262];
0013, 0031, 0103 ... -> 3087 [label=333];
0001, 0010, 0100 ... -> 0999 [label=72];
0024, 0042, 0134 ... -> 4176 [label=284];
0067, 0076, 0177 ... -> 7533 [label=72];
0069, 0096, 0179 ... -> 9531 [label=72];
1111, 2222, 3333 ... -> 0000 [label=9];
0022, 0202, 0220 ... -> 2178 [label=48];
0057, 0075, 0167 ... -> 7443 [label=141];
0019, 0091, 0109 ... -> 9081 [label=192];
0007, 0070, 0117 ... -> 6993 [label=240];
0006, 0060, 0116 ... -> 5994 [label=270];
0056, 0065, 0166 ... -> 6444 [label=96];
0059, 0095, 0169 ... -> 9441 [label=96];
0033, 0303, 0330 ... -> 3267 [label=42];
0044, 0404, 0440 ... -> 4356 [label=36];
0026, 0062, 0136 ... -> 6174 [label=380];
0011, 0101, 0110 ... -> 1089 [label=53];
0023, 0032, 0133 ... -> 3177 [label=168];
0035, 0053, 0145 ... -> 5265 [label=237];
0018, 0081, 0108 ... -> 8082 [label=334];
0002, 0020, 0112 ... -> 1998 [label=158];
0009, 0090, 0119 ... -> 8991 [label=103];
0029, 0092, 0139 ... -> 9171 [label=168];
0047, 0074, 0157 ... -> 7353 [label=216];
0015, 0051, 0105 ... -> 5085 [label=480];
0003, 0030, 0113 ... -> 2997 [label=224];
0077, 0707, 0770 ... -> 7623 [label=18];
0008, 0080, 0118 ... -> 7992 [label=182];
0005, 0050, 0115 ... -> 4995 [label=280];
0089, 0098, 0199 ... -> 9711 [label=24];
0099, 0909, 0990 ... -> 9801 [label=6];
0066, 0606, 0660 ... -> 6534 [label=24];
0017, 0071, 0107 ... -> 7083 [label=432];
}
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/kaprekar.py ============

        digraph {
        graph [rankdir="LR"];
    
0000 -> 0000;
0999 -> 8991;
1089 -> 9621;
1998 -> 8082;
2088 -> 8532;
2178 -> 7443;
2997 -> 7173;
3087 -> 8352;
3177 -> 6354;
3267 -> 5265;
3996 -> 6264;
4086 -> 8172;
4176 -> 6174;
4266 -> 4176;
4356 -> 3087;
4995 -> 5355;
5085 -> 7992;
5175 -> 5994;
5265 -> 3996;
5355 -> 1998;
5445 -> 1089;
5994 -> 5355;
6084 -> 8172;
6174 -> 6174;
6264 -> 4176;
6354 -> 3087;
6444 -> 1998;
6534 -> 3087;
6993 -> 6264;
7083 -> 8352;
7173 -> 6354;
7263 -> 5265;
7353 -> 4176;
7443 -> 3996;
7533 -> 4176;
7623 -> 5265;
7992 -> 7173;
8082 -> 8532;
8172 -> 7443;
8262 -> 6354;
8352 -> 6174;
8442 -> 5994;
8532 -> 6174;
8622 -> 6354;
8712 -> 7443;
8991 -> 8082;
9081 -> 9621;
9171 -> 8532;
9261 -> 8352;
9351 -> 8172;
9441 -> 7992;
9531 -> 8172;
9621 -> 8352;
9711 -> 8532;
9801 -> 9621;
"0049, 0094, 0159 ..." -> 9351 [label=120];
"0039, 0093, 0149 ..." -> 9261 [label=144];
"0027, 0072, 0137 ..." -> 7173 [label=358];
"0014, 0041, 0104 ..." -> 4086 [label=432];
"0028, 0082, 0138 ..." -> 8172 [label=284];
"0078, 0087, 0188 ..." -> 8622 [label=48];
"0045, 0054, 0155 ..." -> 5355 [label=118];
"0012, 0021, 0102 ..." -> 2088 [label=192];
"0034, 0043, 0144 ..." -> 4266 [label=144];
"0055, 0505, 0550 ..." -> 5445 [label=30];
"0058, 0085, 0168 ..." -> 8442 [label=144];
"0016, 0061, 0106 ..." -> 6084 [label=480];
"0048, 0084, 0158 ..." -> 8352 [label=188];
"0036, 0063, 0146 ..." -> 6264 [label=286];
"0025, 0052, 0135 ..." -> 5175 [label=360];
"0079, 0097, 0189 ..." -> 9621 [label=45];
"0046, 0064, 0156 ..." -> 6354 [label=188];
"0037, 0073, 0147 ..." -> 7263 [label=288];
"0088, 0808, 0880 ..." -> 8712 [label=12];
"0068, 0086, 0178 ..." -> 8532 [label=92];
"0038, 0083, 0148 ..." -> 8262 [label=240];
"0004, 0040, 0114 ..." -> 3996 [label=262];
"0013, 0031, 0103 ..." -> 3087 [label=333];
"0001, 0010, 0100 ..." -> 0999 [label=72];
"0024, 0042, 0134 ..." -> 4176 [label=284];
"0067, 0076, 0177 ..." -> 7533 [label=72];
"0069, 0096, 0179 ..." -> 9531 [label=72];
"1111, 2222, 3333 ..." -> 0000 [label=9];
"0022, 0202, 0220 ..." -> 2178 [label=48];
"0057, 0075, 0167 ..." -> 7443 [label=141];
"0019, 0091, 0109 ..." -> 9081 [label=192];
"0007, 0070, 0117 ..." -> 6993 [label=240];
"0006, 0060, 0116 ..." -> 5994 [label=270];
"0056, 0065, 0166 ..." -> 6444 [label=96];
"0059, 0095, 0169 ..." -> 9441 [label=96];
"0033, 0303, 0330 ..." -> 3267 [label=42];
"0044, 0404, 0440 ..." -> 4356 [label=36];
"0026, 0062, 0136 ..." -> 6174 [label=380];
"0011, 0101, 0110 ..." -> 1089 [label=53];
"0023, 0032, 0133 ..." -> 3177 [label=168];
"0035, 0053, 0145 ..." -> 5265 [label=237];
"0018, 0081, 0108 ..." -> 8082 [label=334];
"0002, 0020, 0112 ..." -> 1998 [label=158];
"0009, 0090, 0119 ..." -> 8991 [label=103];
"0029, 0092, 0139 ..." -> 9171 [label=168];
"0047, 0074, 0157 ..." -> 7353 [label=216];
"0015, 0051, 0105 ..." -> 5085 [label=480];
"0003, 0030, 0113 ..." -> 2997 [label=224];
"0077, 0707, 0770 ..." -> 7623 [label=18];
"0008, 0080, 0118 ..." -> 7992 [label=182];
"0005, 0050, 0115 ..." -> 4995 [label=280];
"0089, 0098, 0199 ..." -> 9711 [label=24];
"0099, 0909, 0990 ..." -> 9801 [label=6];
"0066, 0606, 0660 ..." -> 6534 [label=24];
"0017, 0071, 0107 ..." -> 7083 [label=432];
}
>>> 
