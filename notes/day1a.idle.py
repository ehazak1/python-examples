Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 26 2016, 12:10:39) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> s = u'jalape\u00f1o'
>>> print s
jalapeño
>>> type(s)
<type 'unicode'>
>>> 
>>> 
>>> s
u'jalape\xf1o'
>>> 
>>> message = 'a secret message'
>>> message.encode('rot-13')
'n frperg zrffntr'
>>> transmission_format = message.encode('rot-13')
>>> transmission_format
'n frperg zrffntr'
>>> transmission_format.decode('rot-13')
u'a secret message'
>>> 
>>> 
>>> # audio --[encode:mp3]--> transmission/storage format
>>> # transmission/storage format --[decode:mp3]--> audio
>>> 
>>> message
'a secret message'
>>> message.decode('utf-8')
u'a secret message'
>>> 
>>> 
>>> '\x00\xff'.decode()

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    '\x00\xff'.decode()
UnicodeDecodeError: 'ascii' codec can't decode byte 0xff in position 1: ordinal not in range(128)
>>> print u'\N{snowman}'
☃
>>> print u'\N{snowman}\N{comet}'
☃☄
>>> print u'\N{snowman}\N{comet}\N{umbrella}'
☃☄☂
>>> help(str.decode)
Help on method_descriptor:

decode(...)
    S.decode([encoding[,errors]]) -> object
    
    Decodes S using the codec registered for encoding. encoding defaults
    to the default encoding. errors may be given to set a different error
    handling scheme. Default is 'strict' meaning that encoding errors raise
    a UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
    as well as any other name registered with codecs.register_error that is
    able to handle UnicodeDecodeErrors.

>>> 'hello \x00\xff world'.decode()

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    'hello \x00\xff world'.decode()
UnicodeDecodeError: 'ascii' codec can't decode byte 0xff in position 7: ordinal not in range(128)
>>> 'hello \x00\xff world'.decode('ascii', 'ignore')
u'hello \x00 world'
>>> 'hello \xff world'.decode('ascii', 'ignore')
u'hello  world'
>>> 
>>> 
>>> # useful --[encode]--> transmission/storage
>>> # transmission/storage --[decode]--> useful
>>> 
>>> 
>>> s = 'the tale of two cities'
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> s.upper()
'THE TALE OF TWO CITIES'
>>> s.title()
'The Tale Of Two Cities'
>>> s.split()
['the', 'tale', 'of', 'two', 'cities']
>>> s = 'the tale of two cities'
>>> s.title()
'The Tale Of Two Cities'
>>> type(s.title())
<type 'str'>
>>> 
>>> s.title().swapcase()
'tHE tALE oF tWO cITIES'
>>> 
>>> s.split()
['the', 'tale', 'of', 'two', 'cities']
>>> s.split().upper()

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    s.split().upper()
AttributeError: 'list' object has no attribute 'upper'
>>> 
>>> 
>>> s
'the tale of two cities'
>>> len(s)
22
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> s = 'restart'
>>> s.upper()
'RESTART'
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(s.zfill)
Help on built-in function zfill:

zfill(...)
    S.zfill(width) -> string
    
    Pad a numeric string S with zeros on the left, to fill a field
    of the specified width.  The string S is never truncated.

>>> help(s.join)
Help on built-in function join:

join(...)
    S.join(iterable) -> string
    
    Return a string which is the concatenation of the strings in the
    iterable.  The separator between elements is S.

>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
=============================== RESTART: Shell ===============================
>>> s = 'restart'
>>> s.upper()
'RESTART'
>>> s.ljust
<built-in method ljust of str object at 0x1038455d0>
>>> s.rjust
<built-in method rjust of str object at 0x1038455d0>
>>> help(s.center)
Help on built-in function center:

center(...)
    S.center(width[, fillchar]) -> string
    
    Return S centered in a string of length width. Padding is
    done using the specified fill character (default is a space)

>>> s.upper()
'RESTART'
>>> s.upper().center()

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s.upper().center()
TypeError: center() takes at least 1 argument (0 given)
>>> s.upper().center(50)
'                     RESTART                      '
>>> s.upper().center(50, '=')
'=====================RESTART======================'
>>> s.upper().center(70, '=')
'===============================RESTART================================'
>>> 
=============================== RESTART: Shell ===============================
>>> s = 'restart'
>>> s.upper().center(70, '=')
'===============================RESTART================================'
>>> s.upper().center(9).center(70, '=')
'============================== RESTART ==============================='
>>> s.upper().center(len(s) + 2).center(70, '=')
'============================== RESTART ==============================='
>>> s.center(50)
'                     restart                      '
>>> s.center(50, '=')
'=====================restart======================'
>>> 
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(s.istitle)
Help on built-in function istitle:

istitle(...)
    S.istitle() -> bool
    
    Return True if S is a titlecased string and there is at least one
    character in S, i.e. uppercase characters may only follow uncased
    characters and lowercase characters only cased ones. Return False
    otherwise.

>>> "Don't you forget about me".title()
"Don'T You Forget About Me"
>>> 
>>> s
'restart'
>>> s = 'the tale of two cities'
>>> 
>>> 
>>> 
>>> len(s)
22
>>> s[0]
't'
>>> s[22]

Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    s[22]
IndexError: string index out of range
>>> 
>>> s[1]
'h'
>>> s
'the tale of two cities'
>>> len(s)
22
>>> s[len(s)-1]
's'
>>> s[-1]
's'
>>> s[-10]
't'
>>> s[-22]
't'
>>> s[-23]

Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    s[-23]
IndexError: string index out of range
>>> s
'the tale of two cities'

>>> s[0]
't'
>>> s[-1]
's'
>>> 'a' + 'b'
'ab'
>>> 'hello' + 'world'
'helloworld'
>>> 
>>> 2 + 2 + 2
6
>>> 2 + 2 + 2 + 2 + 2
10
>>> 2 * 5
10
>>> 'a' + 'a' + 'a'
'aaa'
>>> 'a' + 'a' + 'a' + 'a' + 'a'
'aaaaa'
>>> 'a' * 5
'aaaaa'
>>> 'ab' * 5
'ababababab'
>>> 
>>> 'abc' * 1.5

Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    'abc' * 1.5
TypeError: can't multiply sequence by non-int of type 'float'
>>> 
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 'a'.__add__('b')
'ab'
>>> 'a' + 'b'
'ab'
>>> len('a')
1
>>> 'a'.__len__()
1
>>> # underscore underscore name underscore underscore
>>> # underscore underscore name
>>> # under under name
>>> # dunder name
>>> 
>>> 'a'.__eq__('a')
True
>>> 'a' == 'a'
True
>>> 'abc'
'abc'
>>> 'a' in 'abc'
True
>>> 'ab' in 'abc'
True
>>> 'abc'.__contains__('ab')
True
>>> 
>>> help('topics')

Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DEBUGGING           LITERALS            SEQUENCEMETHODS2
ASSIGNMENT          DELETION            LOOPING             SEQUENCES
ATTRIBUTEMETHODS    DICTIONARIES        MAPPINGMETHODS      SHIFTING
ATTRIBUTES          DICTIONARYLITERALS  MAPPINGS            SLICINGS
AUGMENTEDASSIGNMENT DYNAMICFEATURES     METHODS             SPECIALATTRIBUTES
BACKQUOTES          ELLIPSIS            MODULES             SPECIALIDENTIFIERS
BASICMETHODS        EXCEPTIONS          NAMESPACES          SPECIALMETHODS
BINARY              EXECUTION           NONE                STRINGMETHODS
BITWISE             EXPRESSIONS         NUMBERMETHODS       STRINGS
BOOLEAN             FILES               NUMBERS             SUBSCRIPTS
CALLABLEMETHODS     FLOAT               OBJECTS             TRACEBACKS
CALLS               FORMATTING          OPERATORS           TRUTHVALUE
CLASSES             FRAMEOBJECTS        PACKAGES            TUPLELITERALS
CODEOBJECTS         FRAMES              POWER               TUPLES
COERCIONS           FUNCTIONS           PRECEDENCE          TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRINTING            TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS1    

>>> help('SPECIALMETHODS')
Special method names
********************

A class can implement certain operations that are invoked by special
syntax (such as arithmetic operations or subscripting and slicing) by
defining methods with special names. This is Python's approach to
*operator overloading*, allowing classes to define their own behavior
with respect to language operators.  For instance, if a class defines
a method named "__getitem__()", and "x" is an instance of this class,
then "x[i]" is roughly equivalent to "x.__getitem__(i)" for old-style
classes and "type(x).__getitem__(x, i)" for new-style classes.  Except
where mentioned, attempts to execute an operation raise an exception
when no appropriate method is defined (typically "AttributeError" or
"TypeError").

When implementing a class that emulates any built-in type, it is
important that the emulation only be implemented to the degree that it
makes sense for the object being modelled.  For example, some
sequences may work well with retrieval of individual elements, but
extracting a slice may not make sense.  (One example of this is the
"NodeList" interface in the W3C's Document Object Model.)


Basic customization
===================

object.__new__(cls[, ...])

   Called to create a new instance of class *cls*.  "__new__()" is a
   static method (special-cased so you need not declare it as such)
   that takes the class of which an instance was requested as its
   first argument.  The remaining arguments are those passed to the
   object constructor expression (the call to the class).  The return
   value of "__new__()" should be the new object instance (usually an
   instance of *cls*).

   Typical implementations create a new instance of the class by
   invoking the superclass's "__new__()" method using
   "super(currentclass, cls).__new__(cls[, ...])" with appropriate
   arguments and then modifying the newly-created instance as
   necessary before returning it.

   If "__new__()" returns an instance of *cls*, then the new
   instance's "__init__()" method will be invoked like
   "__init__(self[, ...])", where *self* is the new instance and the
   remaining arguments are the same as were passed to "__new__()".

   If "__new__()" does not return an instance of *cls*, then the new
   instance's "__init__()" method will not be invoked.

   "__new__()" is intended mainly to allow subclasses of immutable
   types (like int, str, or tuple) to customize instance creation.  It
   is also commonly overridden in custom metaclasses in order to
   customize class creation.

object.__init__(self[, ...])

   Called after the instance has been created (by "__new__()"), but
   before it is returned to the caller.  The arguments are those
   passed to the class constructor expression.  If a base class has an
   "__init__()" method, the derived class's "__init__()" method, if
   any, must explicitly call it to ensure proper initialization of the
   base class part of the instance; for example:
   "BaseClass.__init__(self, [args...])".

   Because "__new__()" and "__init__()" work together in constructing
   objects ("__new__()" to create it, and "__init__()" to customise
   it), no non-"None" value may be returned by "__init__()"; doing so
   will cause a "TypeError" to be raised at runtime.

object.__del__(self)

   Called when the instance is about to be destroyed.  This is also
   called a destructor.  If a base class has a "__del__()" method, the
   derived class's "__del__()" method, if any, must explicitly call it
   to ensure proper deletion of the base class part of the instance.
   Note that it is possible (though not recommended!) for the
   "__del__()" method to postpone destruction of the instance by
   creating a new reference to it.  It may then be called at a later
   time when this new reference is deleted.  It is not guaranteed that
   "__del__()" methods are called for objects that still exist when
   the interpreter exits.

   Note: "del x" doesn't directly call "x.__del__()" --- the former
     decrements the reference count for "x" by one, and the latter is
     only called when "x"'s reference count reaches zero.  Some common
     situations that may prevent the reference count of an object from
     going to zero include: circular references between objects (e.g.,
     a doubly-linked list or a tree data structure with parent and
     child pointers); a reference to the object on the stack frame of
     a function that caught an exception (the traceback stored in
     "sys.exc_traceback" keeps the stack frame alive); or a reference
     to the object on the stack frame that raised an unhandled
     exception in interactive mode (the traceback stored in
     "sys.last_traceback" keeps the stack frame alive).  The first
     situation can only be remedied by explicitly breaking the cycles;
     the latter two situations can be resolved by storing "None" in
     "sys.exc_traceback" or "sys.last_traceback".  Circular references
     which are garbage are detected when the option cycle detector is
     enabled (it's on by default), but can only be cleaned up if there
     are no Python-level "__del__()" methods involved. Refer to the
     documentation for the "gc" module for more information about how
     "__del__()" methods are handled by the cycle detector,
     particularly the description of the "garbage" value.

   Warning: Due to the precarious circumstances under which
     "__del__()" methods are invoked, exceptions that occur during
     their execution are ignored, and a warning is printed to
     "sys.stderr" instead. Also, when "__del__()" is invoked in
     response to a module being deleted (e.g., when execution of the
     program is done), other globals referenced by the "__del__()"
     method may already have been deleted or in the process of being
     torn down (e.g. the import machinery shutting down).  For this
     reason, "__del__()" methods should do the absolute minimum needed
     to maintain external invariants.  Starting with version 1.5,
     Python guarantees that globals whose name begins with a single
     underscore are deleted from their module before other globals are
     deleted; if no other references to such globals exist, this may
     help in assuring that imported modules are still available at the
     time when the "__del__()" method is called.

   See also the "-R" command-line option.

object.__repr__(self)

   Called by the "repr()" built-in function and by string conversions
   (reverse quotes) to compute the "official" string representation of
   an object.  If at all possible, this should look like a valid
   Python expression that could be used to recreate an object with the
   same value (given an appropriate environment).  If this is not
   possible, a string of the form "<...some useful description...>"
   should be returned.  The return value must be a string object. If a
   class defines "__repr__()" but not "__str__()", then "__repr__()"
   is also used when an "informal" string representation of instances
   of that class is required.

   This is typically used for debugging, so it is important that the
   representation is information-rich and unambiguous.

object.__str__(self)

   Called by the "str()" built-in function and by the "print"
   statement to compute the "informal" string representation of an
   object.  This differs from "__repr__()" in that it does not have to
   be a valid Python expression: a more convenient or concise
   representation may be used instead. The return value must be a
   string object.

object.__lt__(self, other)
object.__le__(self, other)
object.__eq__(self, other)
object.__ne__(self, other)
object.__gt__(self, other)
object.__ge__(self, other)

   New in version 2.1.

   These are the so-called "rich comparison" methods, and are called
   for comparison operators in preference to "__cmp__()" below. The
   correspondence between operator symbols and method names is as
   follows: "x<y" calls "x.__lt__(y)", "x<=y" calls "x.__le__(y)",
   "x==y" calls "x.__eq__(y)", "x!=y" and "x<>y" call "x.__ne__(y)",
   "x>y" calls "x.__gt__(y)", and "x>=y" calls "x.__ge__(y)".

   A rich comparison method may return the singleton "NotImplemented"
   if it does not implement the operation for a given pair of
   arguments. By convention, "False" and "True" are returned for a
   successful comparison. However, these methods can return any value,
   so if the comparison operator is used in a Boolean context (e.g.,
   in the condition of an "if" statement), Python will call "bool()"
   on the value to determine if the result is true or false.

   There are no implied relationships among the comparison operators.
   The truth of "x==y" does not imply that "x!=y" is false.
   Accordingly, when defining "__eq__()", one should also define
   "__ne__()" so that the operators will behave as expected.  See the
   paragraph on "__hash__()" for some important notes on creating
   *hashable* objects which support custom comparison operations and
   are usable as dictionary keys.

   There are no swapped-argument versions of these methods (to be used
   when the left argument does not support the operation but the right
   argument does); rather, "__lt__()" and "__gt__()" are each other's
   reflection, "__le__()" and "__ge__()" are each other's reflection,
   and "__eq__()" and "__ne__()" are their own reflection.

   Arguments to rich comparison methods are never coerced.

   To automatically generate ordering operations from a single root
   operation, see "functools.total_ordering()".

object.__cmp__(self, other)

   Called by comparison operations if rich comparison (see above) is
   not defined.  Should return a negative integer if "self < other",
   zero if "self == other", a positive integer if "self > other".  If
   no "__cmp__()", "__eq__()" or "__ne__()" operation is defined,
   class instances are compared by object identity ("address").  See
   also the description of "__hash__()" for some important notes on
   creating *hashable* objects which support custom comparison
   operations and are usable as dictionary keys. (Note: the
   restriction that exceptions are not propagated by "__cmp__()" has
   been removed since Python 1.5.)

object.__rcmp__(self, other)

   Changed in version 2.1: No longer supported.

object.__hash__(self)

   Called by built-in function "hash()" and for operations on members
   of hashed collections including "set", "frozenset", and "dict".
   "__hash__()" should return an integer.  The only required property
   is that objects which compare equal have the same hash value; it is
   advised to somehow mix together (e.g. using exclusive or) the hash
   values for the components of the object that also play a part in
   comparison of objects.

   If a class does not define a "__cmp__()" or "__eq__()" method it
   should not define a "__hash__()" operation either; if it defines
   "__cmp__()" or "__eq__()" but not "__hash__()", its instances will
   not be usable in hashed collections.  If a class defines mutable
   objects and implements a "__cmp__()" or "__eq__()" method, it
   should not implement "__hash__()", since hashable collection
   implementations require that a object's hash value is immutable (if
   the object's hash value changes, it will be in the wrong hash
   bucket).

   User-defined classes have "__cmp__()" and "__hash__()" methods by
   default; with them, all objects compare unequal (except with
   themselves) and "x.__hash__()" returns a result derived from
   "id(x)".

   Classes which inherit a "__hash__()" method from a parent class but
   change the meaning of "__cmp__()" or "__eq__()" such that the hash
   value returned is no longer appropriate (e.g. by switching to a
   value-based concept of equality instead of the default identity
   based equality) can explicitly flag themselves as being unhashable
   by setting "__hash__ = None" in the class definition. Doing so
   means that not only will instances of the class raise an
   appropriate "TypeError" when a program attempts to retrieve their
   hash value, but they will also be correctly identified as
   unhashable when checking "isinstance(obj, collections.Hashable)"
   (unlike classes which define their own "__hash__()" to explicitly
   raise "TypeError").

   Changed in version 2.5: "__hash__()" may now also return a long
   integer object; the 32-bit integer is then derived from the hash of
   that object.

   Changed in version 2.6: "__hash__" may now be set to "None" to
   explicitly flag instances of a class as unhashable.

object.__nonzero__(self)

   Called to implement truth value testing and the built-in operation
   "bool()"; should return "False" or "True", or their integer
   equivalents "0" or "1".  When this method is not defined,
   "__len__()" is called, if it is defined, and the object is
   considered true if its result is nonzero. If a class defines
   neither "__len__()" nor "__nonzero__()", all its instances are
   considered true.

object.__unicode__(self)

   Called to implement "unicode()" built-in; should return a Unicode
   object. When this method is not defined, string conversion is
   attempted, and the result of string conversion is converted to
   Unicode using the system default encoding.


Customizing attribute access
============================

The following methods can be defined to customize the meaning of
attribute access (use of, assignment to, or deletion of "x.name") for
class instances.

object.__getattr__(self, name)

   Called when an attribute lookup has not found the attribute in the
   usual places (i.e. it is not an instance attribute nor is it found
   in the class tree for "self").  "name" is the attribute name. This
   method should return the (computed) attribute value or raise an
   "AttributeError" exception.

   Note that if the attribute is found through the normal mechanism,
   "__getattr__()" is not called.  (This is an intentional asymmetry
   between "__getattr__()" and "__setattr__()".) This is done both for
   efficiency reasons and because otherwise "__getattr__()" would have
   no way to access other attributes of the instance.  Note that at
   least for instance variables, you can fake total control by not
   inserting any values in the instance attribute dictionary (but
   instead inserting them in another object).  See the
   "__getattribute__()" method below for a way to actually get total
   control in new-style classes.

object.__setattr__(self, name, value)

   Called when an attribute assignment is attempted.  This is called
   instead of the normal mechanism (i.e. store the value in the
   instance dictionary).  *name* is the attribute name, *value* is the
   value to be assigned to it.

   If "__setattr__()" wants to assign to an instance attribute, it
   should not simply execute "self.name = value" --- this would cause
   a recursive call to itself.  Instead, it should insert the value in
   the dictionary of instance attributes, e.g., "self.__dict__[name] =
   value".  For new-style classes, rather than accessing the instance
   dictionary, it should call the base class method with the same
   name, for example, "object.__setattr__(self, name, value)".

object.__delattr__(self, name)

   Like "__setattr__()" but for attribute deletion instead of
   assignment.  This should only be implemented if "del obj.name" is
   meaningful for the object.


More attribute access for new-style classes
-------------------------------------------

The following methods only apply to new-style classes.

object.__getattribute__(self, name)

   Called unconditionally to implement attribute accesses for
   instances of the class. If the class also defines "__getattr__()",
   the latter will not be called unless "__getattribute__()" either
   calls it explicitly or raises an "AttributeError". This method
   should return the (computed) attribute value or raise an
   "AttributeError" exception. In order to avoid infinite recursion in
   this method, its implementation should always call the base class
   method with the same name to access any attributes it needs, for
   example, "object.__getattribute__(self, name)".

   Note: This method may still be bypassed when looking up special
     methods as the result of implicit invocation via language syntax
     or built-in functions. See Special method lookup for new-style
     classes.


Implementing Descriptors
------------------------

The following methods only apply when an instance of the class
containing the method (a so-called *descriptor* class) appears in an
*owner* class (the descriptor must be in either the owner's class
dictionary or in the class dictionary for one of its parents).  In the
examples below, "the attribute" refers to the attribute whose name is
the key of the property in the owner class' "__dict__".

object.__get__(self, instance, owner)

   Called to get the attribute of the owner class (class attribute
   access) or of an instance of that class (instance attribute
   access). *owner* is always the owner class, while *instance* is the
   instance that the attribute was accessed through, or "None" when
   the attribute is accessed through the *owner*.  This method should
   return the (computed) attribute value or raise an "AttributeError"
   exception.

object.__set__(self, instance, value)

   Called to set the attribute on an instance *instance* of the owner
   class to a new value, *value*.

object.__delete__(self, instance)

   Called to delete the attribute on an instance *instance* of the
   owner class.


Invoking Descriptors
--------------------

In general, a descriptor is an object attribute with "binding
behavior", one whose attribute access has been overridden by methods
in the descriptor protocol:  "__get__()", "__set__()", and
"__delete__()". If any of those methods are defined for an object, it
is said to be a descriptor.

The default behavior for attribute access is to get, set, or delete
the attribute from an object's dictionary. For instance, "a.x" has a
lookup chain starting with "a.__dict__['x']", then
"type(a).__dict__['x']", and continuing through the base classes of
"type(a)" excluding metaclasses.

However, if the looked-up value is an object defining one of the
descriptor methods, then Python may override the default behavior and
invoke the descriptor method instead.  Where this occurs in the
precedence chain depends on which descriptor methods were defined and
how they were called.  Note that descriptors are only invoked for new
style objects or classes (ones that subclass "object()" or "type()").

The starting point for descriptor invocation is a binding, "a.x". How
the arguments are assembled depends on "a":

Direct Call
   The simplest and least common call is when user code directly
   invokes a descriptor method:    "x.__get__(a)".

Instance Binding
   If binding to a new-style object instance, "a.x" is transformed
   into the call: "type(a).__dict__['x'].__get__(a, type(a))".

Class Binding
   If binding to a new-style class, "A.x" is transformed into the
   call: "A.__dict__['x'].__get__(None, A)".

Super Binding
   If "a" is an instance of "super", then the binding "super(B,
   obj).m()" searches "obj.__class__.__mro__" for the base class "A"
   immediately preceding "B" and then invokes the descriptor with the
   call: "A.__dict__['m'].__get__(obj, obj.__class__)".

For instance bindings, the precedence of descriptor invocation depends
on the which descriptor methods are defined.  A descriptor can define
any combination of "__get__()", "__set__()" and "__delete__()".  If it
does not define "__get__()", then accessing the attribute will return
the descriptor object itself unless there is a value in the object's
instance dictionary.  If the descriptor defines "__set__()" and/or
"__delete__()", it is a data descriptor; if it defines neither, it is
a non-data descriptor.  Normally, data descriptors define both
"__get__()" and "__set__()", while non-data descriptors have just the
"__get__()" method.  Data descriptors with "__set__()" and "__get__()"
defined always override a redefinition in an instance dictionary.  In
contrast, non-data descriptors can be overridden by instances.

Python methods (including "staticmethod()" and "classmethod()") are
implemented as non-data descriptors.  Accordingly, instances can
redefine and override methods.  This allows individual instances to
acquire behaviors that differ from other instances of the same class.

The "property()" function is implemented as a data descriptor.
Accordingly, instances cannot override the behavior of a property.


__slots__
---------

By default, instances of both old and new-style classes have a
dictionary for attribute storage.  This wastes space for objects
having very few instance variables.  The space consumption can become
acute when creating large numbers of instances.

The default can be overridden by defining *__slots__* in a new-style
class definition.  The *__slots__* declaration takes a sequence of
instance variables and reserves just enough space in each instance to
hold a value for each variable.  Space is saved because *__dict__* is
not created for each instance.

__slots__

   This class variable can be assigned a string, iterable, or sequence
   of strings with variable names used by instances.  If defined in a
   new-style class, *__slots__* reserves space for the declared
   variables and prevents the automatic creation of *__dict__* and
   *__weakref__* for each instance.

   New in version 2.2.

Notes on using *__slots__*

* When inheriting from a class without *__slots__*, the *__dict__*
  attribute of that class will always be accessible, so a *__slots__*
  definition in the subclass is meaningless.

* Without a *__dict__* variable, instances cannot be assigned new
  variables not listed in the *__slots__* definition.  Attempts to
  assign to an unlisted variable name raises "AttributeError". If
  dynamic assignment of new variables is desired, then add
  "'__dict__'" to the sequence of strings in the *__slots__*
  declaration.

  Changed in version 2.3: Previously, adding "'__dict__'" to the
  *__slots__* declaration would not enable the assignment of new
  attributes not specifically listed in the sequence of instance
  variable names.

* Without a *__weakref__* variable for each instance, classes
  defining *__slots__* do not support weak references to its
  instances. If weak reference support is needed, then add
  "'__weakref__'" to the sequence of strings in the *__slots__*
  declaration.

  Changed in version 2.3: Previously, adding "'__weakref__'" to the
  *__slots__* declaration would not enable support for weak
  references.

* *__slots__* are implemented at the class level by creating
  descriptors (Implementing Descriptors) for each variable name.  As a
  result, class attributes cannot be used to set default values for
  instance variables defined by *__slots__*; otherwise, the class
  attribute would overwrite the descriptor assignment.

* The action of a *__slots__* declaration is limited to the class
  where it is defined.  As a result, subclasses will have a *__dict__*
  unless they also define *__slots__* (which must only contain names
  of any *additional* slots).

* If a class defines a slot also defined in a base class, the
  instance variable defined by the base class slot is inaccessible
  (except by retrieving its descriptor directly from the base class).
  This renders the meaning of the program undefined.  In the future, a
  check may be added to prevent this.

* Nonempty *__slots__* does not work for classes derived from
  "variable-length" built-in types such as "long", "str" and "tuple".

* Any non-string iterable may be assigned to *__slots__*. Mappings
  may also be used; however, in the future, special meaning may be
  assigned to the values corresponding to each key.

* *__class__* assignment works only if both classes have the same
  *__slots__*.

  Changed in version 2.6: Previously, *__class__* assignment raised an
  error if either new or old class had *__slots__*.


Customizing class creation
==========================

By default, new-style classes are constructed using "type()". A class
definition is read into a separate namespace and the value of class
name is bound to the result of "type(name, bases, dict)".

When the class definition is read, if *__metaclass__* is defined then
the callable assigned to it will be called instead of "type()". This
allows classes or functions to be written which monitor or alter the
class creation process:

* Modifying the class dictionary prior to the class being created.

* Returning an instance of another class -- essentially performing
  the role of a factory function.

These steps will have to be performed in the metaclass's "__new__()"
method -- "type.__new__()" can then be called from this method to
create a class with different properties.  This example adds a new
element to the class dictionary before creating the class:

   class metacls(type):
       def __new__(mcs, name, bases, dict):
           dict['foo'] = 'metacls was here'
           return type.__new__(mcs, name, bases, dict)

You can of course also override other class methods (or add new
methods); for example defining a custom "__call__()" method in the
metaclass allows custom behavior when the class is called, e.g. not
always creating a new instance.

__metaclass__

   This variable can be any callable accepting arguments for "name",
   "bases", and "dict".  Upon class creation, the callable is used
   instead of the built-in "type()".

   New in version 2.2.

The appropriate metaclass is determined by the following precedence
rules:

* If "dict['__metaclass__']" exists, it is used.

* Otherwise, if there is at least one base class, its metaclass is
  used (this looks for a *__class__* attribute first and if not found,
  uses its type).

* Otherwise, if a global variable named __metaclass__ exists, it is
  used.

* Otherwise, the old-style, classic metaclass (types.ClassType) is
  used.

The potential uses for metaclasses are boundless. Some ideas that have
been explored including logging, interface checking, automatic
delegation, automatic property creation, proxies, frameworks, and
automatic resource locking/synchronization.


Customizing instance and subclass checks
========================================

New in version 2.6.

The following methods are used to override the default behavior of the
"isinstance()" and "issubclass()" built-in functions.

In particular, the metaclass "abc.ABCMeta" implements these methods in
order to allow the addition of Abstract Base Classes (ABCs) as
"virtual base classes" to any class or type (including built-in
types), including other ABCs.

class.__instancecheck__(self, instance)

   Return true if *instance* should be considered a (direct or
   indirect) instance of *class*. If defined, called to implement
   "isinstance(instance, class)".

class.__subclasscheck__(self, subclass)

   Return true if *subclass* should be considered a (direct or
   indirect) subclass of *class*.  If defined, called to implement
   "issubclass(subclass, class)".

Note that these methods are looked up on the type (metaclass) of a
class.  They cannot be defined as class methods in the actual class.
This is consistent with the lookup of special methods that are called
on instances, only in this case the instance is itself a class.

See also:

  **PEP 3119** - Introducing Abstract Base Classes
     Includes the specification for customizing "isinstance()" and
     "issubclass()" behavior through "__instancecheck__()" and
     "__subclasscheck__()", with motivation for this functionality in
     the context of adding Abstract Base Classes (see the "abc"
     module) to the language.


Emulating callable objects
==========================

object.__call__(self[, args...])

   Called when the instance is "called" as a function; if this method
   is defined, "x(arg1, arg2, ...)" is a shorthand for
   "x.__call__(arg1, arg2, ...)".


Emulating container types
=========================

The following methods can be defined to implement container objects.
Containers usually are sequences (such as lists or tuples) or mappings
(like dictionaries), but can represent other containers as well.  The
first set of methods is used either to emulate a sequence or to
emulate a mapping; the difference is that for a sequence, the
allowable keys should be the integers *k* for which "0 <= k < N" where
*N* is the length of the sequence, or slice objects, which define a
range of items. (For backwards compatibility, the method
"__getslice__()" (see below) can also be defined to handle simple, but
not extended slices.) It is also recommended that mappings provide the
methods "keys()", "values()", "items()", "has_key()", "get()",
"clear()", "setdefault()", "iterkeys()", "itervalues()",
"iteritems()", "pop()", "popitem()", "copy()", and "update()" behaving
similar to those for Python's standard dictionary objects.  The
"UserDict" module provides a "DictMixin" class to help create those
methods from a base set of "__getitem__()", "__setitem__()",
"__delitem__()", and "keys()". Mutable sequences should provide
methods "append()", "count()", "index()", "extend()", "insert()",
"pop()", "remove()", "reverse()" and "sort()", like Python standard
list objects.  Finally, sequence types should implement addition
(meaning concatenation) and multiplication (meaning repetition) by
defining the methods "__add__()", "__radd__()", "__iadd__()",
"__mul__()", "__rmul__()" and "__imul__()" described below; they
should not define "__coerce__()" or other numerical operators.  It is
recommended that both mappings and sequences implement the
"__contains__()" method to allow efficient use of the "in" operator;
for mappings, "in" should be equivalent of "has_key()"; for sequences,
it should search through the values.  It is further recommended that
both mappings and sequences implement the "__iter__()" method to allow
efficient iteration through the container; for mappings, "__iter__()"
should be the same as "iterkeys()"; for sequences, it should iterate
through the values.

object.__len__(self)

   Called to implement the built-in function "len()".  Should return
   the length of the object, an integer ">=" 0.  Also, an object that
   doesn't define a "__nonzero__()" method and whose "__len__()"
   method returns zero is considered to be false in a Boolean context.

object.__getitem__(self, key)

   Called to implement evaluation of "self[key]". For sequence types,
   the accepted keys should be integers and slice objects.  Note that
   the special interpretation of negative indexes (if the class wishes
   to emulate a sequence type) is up to the "__getitem__()" method. If
   *key* is of an inappropriate type, "TypeError" may be raised; if of
   a value outside the set of indexes for the sequence (after any
   special interpretation of negative values), "IndexError" should be
   raised. For mapping types, if *key* is missing (not in the
   container), "KeyError" should be raised.

   Note: "for" loops expect that an "IndexError" will be raised for
     illegal indexes to allow proper detection of the end of the
     sequence.

object.__missing__(self, key)

   Called by "dict"."__getitem__()" to implement "self[key]" for dict
   subclasses when key is not in the dictionary.

object.__setitem__(self, key, value)

   Called to implement assignment to "self[key]".  Same note as for
   "__getitem__()".  This should only be implemented for mappings if
   the objects support changes to the values for keys, or if new keys
   can be added, or for sequences if elements can be replaced.  The
   same exceptions should be raised for improper *key* values as for
   the "__getitem__()" method.

object.__delitem__(self, key)

   Called to implement deletion of "self[key]".  Same note as for
   "__getitem__()".  This should only be implemented for mappings if
   the objects support removal of keys, or for sequences if elements
   can be removed from the sequence.  The same exceptions should be
   raised for improper *key* values as for the "__getitem__()" method.

object.__iter__(self)

   This method is called when an iterator is required for a container.
   This method should return a new iterator object that can iterate
   over all the objects in the container.  For mappings, it should
   iterate over the keys of the container, and should also be made
   available as the method "iterkeys()".

   Iterator objects also need to implement this method; they are
   required to return themselves.  For more information on iterator
   objects, see Iterator Types.

object.__reversed__(self)

   Called (if present) by the "reversed()" built-in to implement
   reverse iteration.  It should return a new iterator object that
   iterates over all the objects in the container in reverse order.

   If the "__reversed__()" method is not provided, the "reversed()"
   built-in will fall back to using the sequence protocol ("__len__()"
   and "__getitem__()").  Objects that support the sequence protocol
   should only provide "__reversed__()" if they can provide an
   implementation that is more efficient than the one provided by
   "reversed()".

   New in version 2.6.

The membership test operators ("in" and "not in") are normally
implemented as an iteration through a sequence.  However, container
objects can supply the following special method with a more efficient
implementation, which also does not require the object be a sequence.

object.__contains__(self, item)

   Called to implement membership test operators.  Should return true
   if *item* is in *self*, false otherwise.  For mapping objects, this
   should consider the keys of the mapping rather than the values or
   the key-item pairs.

   For objects that don't define "__contains__()", the membership test
   first tries iteration via "__iter__()", then the old sequence
   iteration protocol via "__getitem__()", see this section in the
   language reference.


Additional methods for emulation of sequence types
==================================================

The following optional methods can be defined to further emulate
sequence objects.  Immutable sequences methods should at most only
define "__getslice__()"; mutable sequences might define all three
methods.

object.__getslice__(self, i, j)

   Deprecated since version 2.0: Support slice objects as parameters
   to the "__getitem__()" method. (However, built-in types in CPython
   currently still implement "__getslice__()".  Therefore, you have to
   override it in derived classes when implementing slicing.)

   Called to implement evaluation of "self[i:j]". The returned object
   should be of the same type as *self*.  Note that missing *i* or *j*
   in the slice expression are replaced by zero or "sys.maxsize",
   respectively.  If negative indexes are used in the slice, the
   length of the sequence is added to that index. If the instance does
   not implement the "__len__()" method, an "AttributeError" is
   raised. No guarantee is made that indexes adjusted this way are not
   still negative.  Indexes which are greater than the length of the
   sequence are not modified. If no "__getslice__()" is found, a slice
   object is created instead, and passed to "__getitem__()" instead.

object.__setslice__(self, i, j, sequence)

   Called to implement assignment to "self[i:j]". Same notes for *i*
   and *j* as for "__getslice__()".

   This method is deprecated. If no "__setslice__()" is found, or for
   extended slicing of the form "self[i:j:k]", a slice object is
   created, and passed to "__setitem__()", instead of "__setslice__()"
   being called.

object.__delslice__(self, i, j)

   Called to implement deletion of "self[i:j]". Same notes for *i* and
   *j* as for "__getslice__()". This method is deprecated. If no
   "__delslice__()" is found, or for extended slicing of the form
   "self[i:j:k]", a slice object is created, and passed to
   "__delitem__()", instead of "__delslice__()" being called.

Notice that these methods are only invoked when a single slice with a
single colon is used, and the slice method is available.  For slice
operations involving extended slice notation, or in absence of the
slice methods, "__getitem__()", "__setitem__()" or "__delitem__()" is
called with a slice object as argument.

The following example demonstrate how to make your program or module
compatible with earlier versions of Python (assuming that methods
"__getitem__()", "__setitem__()" and "__delitem__()" support slice
objects as arguments):

   class MyClass:
       ...
       def __getitem__(self, index):
           ...
       def __setitem__(self, index, value):
           ...
       def __delitem__(self, index):
           ...

       if sys.version_info < (2, 0):
           # They won't be defined if version is at least 2.0 final

           def __getslice__(self, i, j):
               return self[max(0, i):max(0, j):]
           def __setslice__(self, i, j, seq):
               self[max(0, i):max(0, j):] = seq
           def __delslice__(self, i, j):
               del self[max(0, i):max(0, j):]
       ...

Note the calls to "max()"; these are necessary because of the handling
of negative indices before the "__*slice__()" methods are called.
When negative indexes are used, the "__*item__()" methods receive them
as provided, but the "__*slice__()" methods get a "cooked" form of the
index values.  For each negative index value, the length of the
sequence is added to the index before calling the method (which may
still result in a negative index); this is the customary handling of
negative indexes by the built-in sequence types, and the "__*item__()"
methods are expected to do this as well.  However, since they should
already be doing that, negative indexes cannot be passed in; they must
be constrained to the bounds of the sequence before being passed to
the "__*item__()" methods. Calling "max(0, i)" conveniently returns
the proper value.


Emulating numeric types
=======================

The following methods can be defined to emulate numeric objects.
Methods corresponding to operations that are not supported by the
particular kind of number implemented (e.g., bitwise operations for
non-integral numbers) should be left undefined.

object.__add__(self, other)
object.__sub__(self, other)
object.__mul__(self, other)
object.__floordiv__(self, other)
object.__mod__(self, other)
object.__divmod__(self, other)
object.__pow__(self, other[, modulo])
object.__lshift__(self, other)
object.__rshift__(self, other)
object.__and__(self, other)
object.__xor__(self, other)
object.__or__(self, other)

   These methods are called to implement the binary arithmetic
   operations ("+", "-", "*", "//", "%", "divmod()", "pow()", "**",
   "<<", ">>", "&", "^", "|").  For instance, to evaluate the
   expression "x + y", where *x* is an instance of a class that has an
   "__add__()" method, "x.__add__(y)" is called.  The "__divmod__()"
   method should be the equivalent to using "__floordiv__()" and
   "__mod__()"; it should not be related to "__truediv__()" (described
   below).  Note that "__pow__()" should be defined to accept an
   optional third argument if the ternary version of the built-in
   "pow()" function is to be supported.

   If one of those methods does not support the operation with the
   supplied arguments, it should return "NotImplemented".

object.__div__(self, other)
object.__truediv__(self, other)

   The division operator ("/") is implemented by these methods.  The
   "__truediv__()" method is used when "__future__.division" is in
   effect, otherwise "__div__()" is used.  If only one of these two
   methods is defined, the object will not support division in the
   alternate context; "TypeError" will be raised instead.

object.__radd__(self, other)
object.__rsub__(self, other)
object.__rmul__(self, other)
object.__rdiv__(self, other)
object.__rtruediv__(self, other)
object.__rfloordiv__(self, other)
object.__rmod__(self, other)
object.__rdivmod__(self, other)
object.__rpow__(self, other)
object.__rlshift__(self, other)
object.__rrshift__(self, other)
object.__rand__(self, other)
object.__rxor__(self, other)
object.__ror__(self, other)

   These methods are called to implement the binary arithmetic
   operations ("+", "-", "*", "/", "%", "divmod()", "pow()", "**",
   "<<", ">>", "&", "^", "|") with reflected (swapped) operands.
   These functions are only called if the left operand does not
   support the corresponding operation and the operands are of
   different types. [2] For instance, to evaluate the expression "x -
   y", where *y* is an instance of a class that has an "__rsub__()"
   method, "y.__rsub__(x)" is called if "x.__sub__(y)" returns
   *NotImplemented*.

   Note that ternary "pow()" will not try calling "__rpow__()" (the
   coercion rules would become too complicated).

   Note: If the right operand's type is a subclass of the left
     operand's type and that subclass provides the reflected method
     for the operation, this method will be called before the left
     operand's non-reflected method.  This behavior allows subclasses
     to override their ancestors' operations.

object.__iadd__(self, other)
object.__isub__(self, other)
object.__imul__(self, other)
object.__idiv__(self, other)
object.__itruediv__(self, other)
object.__ifloordiv__(self, other)
object.__imod__(self, other)
object.__ipow__(self, other[, modulo])
object.__ilshift__(self, other)
object.__irshift__(self, other)
object.__iand__(self, other)
object.__ixor__(self, other)
object.__ior__(self, other)

   These methods are called to implement the augmented arithmetic
   assignments ("+=", "-=", "*=", "/=", "//=", "%=", "**=", "<<=",
   ">>=", "&=", "^=", "|=").  These methods should attempt to do the
   operation in-place (modifying *self*) and return the result (which
   could be, but does not have to be, *self*).  If a specific method
   is not defined, the augmented assignment falls back to the normal
   methods.  For instance, to execute the statement "x += y", where
   *x* is an instance of a class that has an "__iadd__()" method,
   "x.__iadd__(y)" is called.  If *x* is an instance of a class that
   does not define a "__iadd__()" method, "x.__add__(y)" and
   "y.__radd__(x)" are considered, as with the evaluation of "x + y".

object.__neg__(self)
object.__pos__(self)
object.__abs__(self)
object.__invert__(self)

   Called to implement the unary arithmetic operations ("-", "+",
   "abs()" and "~").

object.__complex__(self)
object.__int__(self)
object.__long__(self)
object.__float__(self)

   Called to implement the built-in functions "complex()", "int()",
   "long()", and "float()".  Should return a value of the appropriate
   type.

object.__oct__(self)
object.__hex__(self)

   Called to implement the built-in functions "oct()" and "hex()".
   Should return a string value.

object.__index__(self)

   Called to implement "operator.index()".  Also called whenever
   Python needs an integer object (such as in slicing).  Must return
   an integer (int or long).

   New in version 2.5.

object.__coerce__(self, other)

   Called to implement "mixed-mode" numeric arithmetic.  Should either
   return a 2-tuple containing *self* and *other* converted to a
   common numeric type, or "None" if conversion is impossible.  When
   the common type would be the type of "other", it is sufficient to
   return "None", since the interpreter will also ask the other object
   to attempt a coercion (but sometimes, if the implementation of the
   other type cannot be changed, it is useful to do the conversion to
   the other type here).  A return value of "NotImplemented" is
   equivalent to returning "None".


Coercion rules
==============

This section used to document the rules for coercion.  As the language
has evolved, the coercion rules have become hard to document
precisely; documenting what one version of one particular
implementation does is undesirable.  Instead, here are some informal
guidelines regarding coercion.  In Python 3, coercion will not be
supported.

* If the left operand of a % operator is a string or Unicode object,
  no coercion takes place and the string formatting operation is
  invoked instead.

* It is no longer recommended to define a coercion operation. Mixed-
  mode operations on types that don't define coercion pass the
  original arguments to the operation.

* New-style classes (those derived from "object") never invoke the
  "__coerce__()" method in response to a binary operator; the only
  time "__coerce__()" is invoked is when the built-in function
  "coerce()" is called.

* For most intents and purposes, an operator that returns
  "NotImplemented" is treated the same as one that is not implemented
  at all.

* Below, "__op__()" and "__rop__()" are used to signify the generic
  method names corresponding to an operator; "__iop__()" is used for
  the corresponding in-place operator.  For example, for the operator
  '"+"', "__add__()" and "__radd__()" are used for the left and right
  variant of the binary operator, and "__iadd__()" for the in-place
  variant.

* For objects *x* and *y*, first "x.__op__(y)" is tried.  If this is
  not implemented or returns "NotImplemented", "y.__rop__(x)" is
  tried.  If this is also not implemented or returns "NotImplemented",
  a "TypeError" exception is raised.  But see the following exception:

* Exception to the previous item: if the left operand is an instance
  of a built-in type or a new-style class, and the right operand is an
  instance of a proper subclass of that type or class and overrides
  the base's "__rop__()" method, the right operand's "__rop__()"
  method is tried *before* the left operand's "__op__()" method.

  This is done so that a subclass can completely override binary
  operators. Otherwise, the left operand's "__op__()" method would
  always accept the right operand: when an instance of a given class
  is expected, an instance of a subclass of that class is always
  acceptable.

* When either operand type defines a coercion, this coercion is
  called before that type's "__op__()" or "__rop__()" method is
  called, but no sooner.  If the coercion returns an object of a
  different type for the operand whose coercion is invoked, part of
  the process is redone using the new object.

* When an in-place operator (like '"+="') is used, if the left
  operand implements "__iop__()", it is invoked without any coercion.
  When the operation falls back to "__op__()" and/or "__rop__()", the
  normal coercion rules apply.

* In "x + y", if *x* is a sequence that implements sequence
  concatenation, sequence concatenation is invoked.

* In "x * y", if one operand is a sequence that implements sequence
  repetition, and the other is an integer ("int" or "long"), sequence
  repetition is invoked.

* Rich comparisons (implemented by methods "__eq__()" and so on)
  never use coercion.  Three-way comparison (implemented by
  "__cmp__()") does use coercion under the same conditions as other
  binary operations use it.

* In the current implementation, the built-in numeric types "int",
  "long", "float", and "complex" do not use coercion. All these types
  implement a "__coerce__()" method, for use by the built-in
  "coerce()" function.

  Changed in version 2.7: The complex type no longer makes implicit
  calls to the "__coerce__()" method for mixed-type binary arithmetic
  operations.


With Statement Context Managers
===============================

New in version 2.5.

A *context manager* is an object that defines the runtime context to
be established when executing a "with" statement. The context manager
handles the entry into, and the exit from, the desired runtime context
for the execution of the block of code.  Context managers are normally
invoked using the "with" statement (described in section The with
statement), but can also be used by directly invoking their methods.

Typical uses of context managers include saving and restoring various
kinds of global state, locking and unlocking resources, closing opened
files, etc.

For more information on context managers, see Context Manager Types.

object.__enter__(self)

   Enter the runtime context related to this object. The "with"
   statement will bind this method's return value to the target(s)
   specified in the "as" clause of the statement, if any.

object.__exit__(self, exc_type, exc_value, traceback)

   Exit the runtime context related to this object. The parameters
   describe the exception that caused the context to be exited. If the
   context was exited without an exception, all three arguments will
   be "None".

   If an exception is supplied, and the method wishes to suppress the
   exception (i.e., prevent it from being propagated), it should
   return a true value. Otherwise, the exception will be processed
   normally upon exit from this method.

   Note that "__exit__()" methods should not reraise the passed-in
   exception; this is the caller's responsibility.

See also:

  **PEP 343** - The "with" statement
     The specification, background, and examples for the Python "with"
     statement.


Special method lookup for old-style classes
===========================================

For old-style classes, special methods are always looked up in exactly
the same way as any other method or attribute. This is the case
regardless of whether the method is being looked up explicitly as in
"x.__getitem__(i)" or implicitly as in "x[i]".

This behaviour means that special methods may exhibit different
behaviour for different instances of a single old-style class if the
appropriate special attributes are set differently:

   >>> class C:
   ...     pass
   ...
   >>> c1 = C()
   >>> c2 = C()
   >>> c1.__len__ = lambda: 5
   >>> c2.__len__ = lambda: 9
   >>> len(c1)
   5
   >>> len(c2)
   9


Special method lookup for new-style classes
===========================================

For new-style classes, implicit invocations of special methods are
only guaranteed to work correctly if defined on an object's type, not
in the object's instance dictionary.  That behaviour is the reason why
the following code raises an exception (unlike the equivalent example
with old-style classes):

   >>> class C(object):
   ...     pass
   ...
   >>> c = C()
   >>> c.__len__ = lambda: 5
   >>> len(c)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: object of type 'C' has no len()

The rationale behind this behaviour lies with a number of special
methods such as "__hash__()" and "__repr__()" that are implemented by
all objects, including type objects. If the implicit lookup of these
methods used the conventional lookup process, they would fail when
invoked on the type object itself:

   >>> 1 .__hash__() == hash(1)
   True
   >>> int.__hash__() == hash(int)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: descriptor '__hash__' of 'int' object needs an argument

Incorrectly attempting to invoke an unbound method of a class in this
way is sometimes referred to as 'metaclass confusion', and is avoided
by bypassing the instance when looking up special methods:

   >>> type(1).__hash__(1) == hash(1)
   True
   >>> type(int).__hash__(int) == hash(int)
   True

In addition to bypassing any instance attributes in the interest of
correctness, implicit special method lookup generally also bypasses
the "__getattribute__()" method even of the object's metaclass:

   >>> class Meta(type):
   ...    def __getattribute__(*args):
   ...       print "Metaclass getattribute invoked"
   ...       return type.__getattribute__(*args)
   ...
   >>> class C(object):
   ...     __metaclass__ = Meta
   ...     def __len__(self):
   ...         return 10
   ...     def __getattribute__(*args):
   ...         print "Class getattribute invoked"
   ...         return object.__getattribute__(*args)
   ...
   >>> c = C()
   >>> c.__len__()                 # Explicit lookup via instance
   Class getattribute invoked
   10
   >>> type(c).__len__(c)          # Explicit lookup via type
   Metaclass getattribute invoked
   10
   >>> len(c)                      # Implicit lookup
   10

Bypassing the "__getattribute__()" machinery in this fashion provides
significant scope for speed optimisations within the interpreter, at
the cost of some flexibility in the handling of special methods (the
special method *must* be set on the class object itself in order to be
consistently invoked by the interpreter).

-[ Footnotes ]-

[1] It *is* possible in some cases to change an object's type,
    under certain controlled conditions. It generally isn't a good
    idea though, since it can lead to some very strange behaviour if
    it is handled incorrectly.

[2] For operands of the same type, it is assumed that if the non-
    reflected method (such as "__add__()") fails the operation is not
    supported, which is why the reflected method is not called.

Related help topics: BASICMETHODS, ATTRIBUTEMETHODS, CALLABLEMETHODS,
SEQUENCEMETHODS1, MAPPINGMETHODS, SEQUENCEMETHODS2, NUMBERMETHODS,
CLASSES

>>> 
>>> 
>>> class Dog:
	def __init__(self, name):
		self.name = name
	def bark(self):
		print 'Woof!', name, 'is barking!'

		
>>> a = Dog('Fido')
>>> a.bark()
Woof!

Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    a.bark()
  File "<pyshell#142>", line 5, in bark
    print 'Woof!', name, 'is barking!'
NameError: global name 'name' is not defined
>>> class Dog:
	def __init__(self, name):
		self.name = name
	def bark(self):
		print 'Woof!', self.name, 'is barking!'

		
>>> a = Dog('Fido')
>>> a.bark()
Woof! Fido is barking!
>>> 
>>> len(a)

Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    len(a)
AttributeError: Dog instance has no attribute '__len__'
>>> 
>>> 
>>> dir('hello')
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> 
>>> s = 'the tale of two cities'
>>> s
'the tale of two cities'
>>> # gather the first 3 characters of string `s` in a new string
>>> s[0] + s[1] + s[2]
'the'
>>> s[0:3] # from 0, up to but not including 3
'the'
>>> s[0:3] # slicing uses a half-open interval, from start, up to but excluding stop
'the'
>>> range(5)
[0, 1, 2, 3, 4]
>>> range(1, 5)
[1, 2, 3, 4]
>>> s[1:6]
'he ta'
>>> s
'the tale of two cities'
>>> 'index.html'
'index.html'
>>> 'index.html'.split('.')
['index', 'html']
>>> 'index.html'[0:-1]
'index.htm'
>>> 'index.html'[0:-5]
'index'
>>> 'index.html'[:-5]
'index'
>>> 'index.html'[-5:]
'.html'
>>> 
>>> # Pythonic
>>> s = 'the tale of two cities'
>>> s[0:len(s)]
'the tale of two cities'
>>> s[:]
'the tale of two cities'
>>> s[::2]
'tetl ftocte'
>>> s[::-1]
'seitic owt fo elat eht'
>>> s[-5:-10:-1]
'ic ow'
>>> len(s)
22
>>> s[50]

Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    s[50]
IndexError: string index out of range
>>> s[0:50]
'the tale of two cities'
>>> s[0:1]
't'
>>> 
>>> for c in 'abc':
	print c

	
a
b
c
>>> c
'c'
>>> str
<type 'str'>
>>> 
>>> str = 'a'
>>> 
>>> 
>>> del str
>>> str
<type 'str'>
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> x = 5
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'x']
>>> del x
>>> 
>>> 
>>> x

Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> int = 5
>>> int
5
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'int']
>>> del int
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> del int

Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    del int
NameError: name 'int' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 
>>> int
<type 'int'>
>>> float
<type 'float'>
>>> str
<type 'str'>
>>> 
>>> # Philosophers want to know, what is True?
>>> 
>>> 
>>> bool
<type 'bool'>
>>> 
>>> True
True
>>> False
False
>>> 
>>> 'a' == 5
False
>>> false

Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    false
NameError: name 'false' is not defined
>>> 
>>> None
>>> 
>>> if 5:
	print 'yes'
else:
	print 'no'

	
yes
>>> bool(5)
True
>>> bool(6)
True
>>> bool(-1)
True
>>> bool(0)
False
>>> bool(0.0)
False
>>> # Everything in Python is True
>>> # Unless it is False
>>> 
>>> # There are 3 ways to be False
>>> 
>>> # 1. be zero
>>> 
>>> bool('')
False
>>> bool('dslfjsdlfjsd')
True
>>> bool([])
False
>>> bool([1, 2, 3])
True
>>> bool([False, False])
True
>>> # 2. be empty ... len(obj) == 0
>>> bool(None)
False
>>> # 3. be None
>>> 
>>> x = [1, 2, 3]
>>> if x:
	print 'a non-empty list'
else:
	print 'either an empty list or None'

	
a non-empty list
>>> 
>>> if x is not None:
	print 'a non-empty list'
else:
	print 'either an empty list or None'

	
a non-empty list
>>> if x is not None:
	print 'is not None
else:
	print 'is None'
	
SyntaxError: EOL while scanning string literal
>>> 
>>> if x is not None:
	print 'is not None'
else:
	print 'is None'

	
is not None
>>> x is None
False
>>> None
>>> 
>>> # == < > <= >= !=
>>> 'a' != 'b'
True
>>> 'a' <> 'b'
True
>>> 
>>> 
>>> 'a' <> 'b' # don't use <>, that's there for backwards-compatibility only
True
>>> 
>>> 
>>> # in is or and not
>>> 
>>> 
>>> x = 2
>>> 
>>> x < 10 or x > 30
True
>>> x < 10 and x % 2 == 0
True
>>> 
>>> 
>>> True or False
True
>>> False or True
True
>>> 0 or True
True
>>> 0 or 0
0
>>> 0 or 5
5
>>> 5 or 0
5
>>> [] or 0
0
>>> 0 or []
[]
>>> def foo():
	print 'foo'

	
>>> def bar():
	print 'bar'
	return True

>>> bar() or foo()
bar
True
>>> foo() or bar()
foo
bar
True
>>> x = None
>>> 
>>> if x is not None and x[0] == 5
SyntaxError: invalid syntax
>>> if x is not None and x[0] == 5:
	pass

>>> 
>>> 
>>> 
>>> 
>>> def is_even(x):
	if x % 2 == 0:
		return True
	else:
		return False

	
>>> def is_even(x):
	return x % 2 == 0

>>> 
>>> 
>>> # == < > <= >= !=
>>> 
>>> x = 5
>>> 0 < x and x < 10
True
>>> 0 < x < 10
True
>>> 5.0 == 5 == x
True
>>> 
>>> 
>>> # in is or and not
>>> 
>>> not 5
False
>>> # is
>>> 
>>> 
>>> 
>>> 
>>> a = [0, 1]
>>> b = [0, 1]
>>> 
>>> 
>>> a == b
True
>>> a is b
False
>>> 
>>> bool(5)
True
>>> 
>>> a = [0, 1]
>>> b = a
>>> 
>>> a == b
True
>>> a is b
True
>>> a.append(2)
>>> a
[0, 1, 2]
>>> b
[0, 1, 2]
>>> 
>>> a.extend([3, 4])
>>> a
[0, 1, 2, 3, 4]
>>> 
>>> # 4 basic types (scalars)
>>> int, float, str, bool
(<type 'int'>, <type 'float'>, <type 'str'>, <type 'bool'>)
>>> # 4 basic collections
>>> 
>>> list, dict, set, tuple
(<type 'list'>, <type 'dict'>, <type 'set'>, <type 'tuple'>)
>>> 
>>> 
>>> 
>>> a = [0, 1]
>>> # a list is a sequence
>>> a[0]
0
>>> a[1]
1
>>> 
>>> a = [10, 20]
>>> a[0]
10
>>> a[1]
20
>>> a.append(30)
>>> a
[10, 20, 30]
>>> for x in a:
	print x

	
10
20
30
>>> a[:2]
[10, 20]
>>> len(a)
3
>>> 
>>> 
>>> a[0] = -a[0]
>>> a
[-10, 20, 30]
>>> 
>>> 
>>> del a[1]
>>> len(a)
2
>>> a[2]

Traceback (most recent call last):
  File "<pyshell#397>", line 1, in <module>
    a[2]
IndexError: list index out of range
>>> a
[-10, 30]
>>> [None, None]
[None, None]
>>> [None, 5, 'a']
[None, 5, 'a']
>>> 
>>> 
>>> a = [10, 20, 30]
>>> a.append(40)
>>> a.pop()
40
>>> a
[10, 20, 30]
>>> a.pop(0)
10
>>> a
[20, 30]
>>> 
>>> 
>>> x = 2
>>> if x == 0:
	print 'a'
else:
	if x == 1:
		print 'b'
	else:
		pass

	
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
>>> if x == 0:
	print 'a'
elif x == 1:
	print 'b'
elif x == 2:
	print 'c'
else:
	print 'd'

	
c
>>> 
>>> 
>>> range(5)
[0, 1, 2, 3, 4]
>>> for i in range(5):
	print i

	
0
1
2
3
4
>>> 
>>> 
>>> 
>>> '''
C:

for (int i=0; i<5; i++) {
    printf("%d", i);
    i = 2;
}
'''
'\nC:\n\nfor (int i=0; i<5; i++) {\n    printf("%d", i);\n    i = 2;\n}\n'
>>> 
>>> for i in range(5):
	print i
	i = 2

	
0
1
2
3
4
>>> '''
for i in [0, 1, 2, 3, 4, 5]:
	                 ^-- i = next(iterator)
    print i
    i = 2
'''
'\nfor i in [0, 1, 2, 3, 4, 5]:\n\t                 ^-- i = next(iterator)\n    print i\n    i = 2\n'
>>> 
>>> 
>>> 
>>> 
>>> a = [10, 20, 30, 40, 50]
>>> for element in a:
	print element
	print a
	print a.pop()

	
10
[10, 20, 30, 40, 50]
50
20
[10, 20, 30, 40]
40
30
[10, 20, 30]
30
>>> 
>>> a = [10, 20, 30, 40, 50]
>>> squares = []
>>> for x in a:
	squares.append(x ** 2)

	
>>> x
50
>>> squares
[100, 400, 900, 1600, 2500]
>>> 
>>> 
>>> 
>>> x = 5
>>> x++
SyntaxError: invalid syntax
>>> ++x
5
>>> 
>>> -x
-5
>>> -(-x)
5
>>> --x
5
>>> +x
5
>>> ++x
5
>>> +++x
5
>>> 
>>> x += 1
>>> x
6
>>> x = x + 1
>>> 
>>> 
>>> 
>>> 
>>> def square(x):
	return x ** 2

>>> def square(x):
	return x * x

>>> square
<function square at 0x1031621b8>
>>> square(4)
16
>>> 
>>> class Dog:
	kind = 'canine'
	mood = 'happy'

	
>>> a = Dog()
>>> a.name = 'Fido'
>>> 
>>> 
>>> 
>>> a.name
'Fido'
>>> 
>>> a.mood
'happy'
>>> 
>>> Dog.mood
'happy'
>>> Dog.name

Traceback (most recent call last):
  File "<pyshell#521>", line 1, in <module>
    Dog.name
AttributeError: class Dog has no attribute 'name'
>>> 
>>> 
>>> 
>>> # break until 3:40pm
>>> 
>>> 
>>> 
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/download.py ============
======= Source: https://dl.dropboxusercontent.com/u/54337323/2016-06-13/links.txt ========
                      Starting download at Mon Sep 19 16:03:12 2016                       
https://dl.dropboxusercontent.com/u/54337323/2016-06-13/links.txt
200* OK           https://dl.dropboxusercontent.com/u/54337323/data/symlinks.txt
                  --> notes/symlinks.txt        (updated)
200* OK           https://dl.dropboxusercontent.com/u/3967849/shared/ipv4_int_bri.txt
                  --> notes/ipv4_int_bri.txt    (updated)
200* OK           https://dl.dropboxusercontent.com/u/54337323/data/show_int_brief.json
                  --> notes/show_int_brief.json (updated)
200* OK           https://dl.dropboxusercontent.com/u/3967849/shared/interfaces.xml
                  --> notes/interfaces.xml      (updated)
200* OK           https://dl.dropboxusercontent.com/u/3967849/shared/books.xml
                  --> notes/books.xml           (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/brief_v4.py
                  --> notes/brief_v4.py         (updated)
200  OK           https://dl.dropboxusercontent.com/u/3967849/shared/telnet_demo.py
                  --> notes/telnet_demo.py      (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/books_json.py
                  --> notes/books_json.py       (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/brief.py
                  --> notes/brief.py            (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/brief_v3.py
                  --> notes/brief_v3.py         (updated)
200  OK           https://dl.dropboxusercontent.com/u/3967849/shared/__init__.py
                  --> notes/__init__.py         (updated)
200* OK           https://dl.dropboxusercontent.com/u/54337323/data/show_int_brief.xml
                  --> notes/show_int_brief.xml  (updated)
200* OK           https://dl.dropboxusercontent.com/u/3967849/shared/books.json
                  --> notes/books.json          (updated)
200* OK           https://dl.dropboxusercontent.com/u/54337323/data/alltimegross.html
                  --> notes/alltimegross.html   (updated)
200  OK           https://dl.dropboxusercontent.com/u/3967849/shared/raisin_team.csv
                  --> notes/raisin_team.csv     (updated)
200  OK           https://dl.dropboxusercontent.com/u/3967849/shared/pexpect.py
                  --> notes/pexpect.py          (updated)
200* OK           https://dl.dropboxusercontent.com/u/54337323/data/enron.lay-k.inbox.sample
                  --> notes/enron.lay-k.inbox.sample (updated)
200  OK           https://dl.dropboxusercontent.com/u/3967849/shared/PythonAwesome.pdf
                  --> notes/PythonAwesome.pdf   (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/brief_v2.py
                  --> notes/brief_v2.py         (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/brief_v6.py
                  --> notes/brief_v6.py         (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/brief_xml.py
                  --> notes/brief_xml.py        (updated)
200  OK           https://dl.dropboxusercontent.com/u/3967849/shared/BeautifulSoup.py
                  --> notes/BeautifulSoup.py    (updated)
200* OK           https://dl.dropboxusercontent.com/u/54337323/data/nasa.log.sample
                  --> notes/nasa.log.sample     (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/highlight.py
                  --> notes/highlight.py        (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/download.py
                  --> notes/download.py         (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/http_client.py
                  --> notes/http_client.py      (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/example.py
                  --> notes/example.py          (updated)
200  OK           https://dl.dropboxusercontent.com/u/3967849/shared/islands.pdf
                  --> notes/islands.pdf         (updated)
200  OK           https://dl.dropboxusercontent.com/u/3967849/shared/raisin_team_update.csv
                  --> notes/raisin_team_update.csv (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/iteration.py
                  --> notes/iteration.py        (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/dog.py
                  --> notes/dog.py              (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/day2.idle.py
                  --> notes/day2.idle.py        (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/day1.idle.py
                  --> notes/day1.idle.py        (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/kaprekar.py
                  --> notes/kaprekar.py         (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/day4.idle.py
                  --> notes/day4.idle.py        (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/pets.py
                  --> notes/pets.py             (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/nasa.py
                  --> notes/nasa.py             (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/brief_v5.py
                  --> notes/brief_v5.py         (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/racing.py
                  --> notes/racing.py           (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/show_pypi_count.py
                  --> notes/show_pypi_count.py  (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/tcp_server.py
                  --> notes/tcp_server.py       (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/tcp_server_multiprocessing.py
                  --> notes/tcp_server_multiprocessing.py (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/udp_server.py
                  --> notes/udp_server.py       (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/vcard.py
                  --> notes/vcard.py            (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/xml_with_namespaces.py
                  --> notes/xml_with_namespaces.py (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/lookup.py
                  --> notes/lookup.py           (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/tcp_server_threaded.py
                  --> notes/tcp_server_threaded.py (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/movies.py
                  --> notes/movies.py           (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/day3.idle.py
                  --> notes/day3.idle.py        (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/publish.py
                  --> notes/publish.py          (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/books_xml.py
                  --> notes/books_xml.py        (updated)
200  OK           https://dl.dropboxusercontent.com/u/3967849/shared/IntroPython.pdf
                  --> notes/IntroPython.pdf     (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/tcp_client.py
                  --> notes/tcp_client.py       (updated)
200  OK           https://dl.dropboxusercontent.com/u/54337323/2016-06-13/udp_client.py
                  --> notes/udp_client.py       (updated)
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/download.py ============
======= Source: https://dl.dropboxusercontent.com/u/54337323/2016-09-19/links.txt ========
                      Starting download at Mon Sep 19 16:04:33 2016                       
https://dl.dropboxusercontent.com/u/54337323/2016-09-19/links.txt
200  OK           https://dl.dropboxusercontent.com/u/3967849/shared/raisin_team.csv
                  --> notes/raisin_team.csv     (updated)
200  OK           https://dl.dropboxusercontent.com/u/3967849/shared/PythonAwesome.pdf
                  --> notes/PythonAwesome.pdf   (updated)
>>> download

Traceback (most recent call last):
  File "<pyshell#529>", line 1, in <module>
    download
NameError: name 'download' is not defined
>>> download.py

Traceback (most recent call last):
  File "<pyshell#530>", line 1, in <module>
    download.py
NameError: name 'download' is not defined
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/download.py ============
======= Source: https://dl.dropboxusercontent.com/u/54337323/2016-09-19/links.txt ========
                      Starting download at Mon Sep 19 16:07:23 2016                       
https://dl.dropboxusercontent.com/u/54337323/2016-09-19/links.txt
304  NOT MODIFIED https://dl.dropboxusercontent.com/u/3967849/shared/PythonAwesome.pdf
304  NOT MODIFIED https://dl.dropboxusercontent.com/u/3967849/shared/raisin_team.csv
>>> 
============ RESTART: /Users/mike/teaching/2016-09-19/download.py ============
======= Source: https://dl.dropboxusercontent.com/u/54337323/2016-09-19/links.txt ========
                      Starting download at Mon Sep 19 16:07:48 2016                       
https://dl.dropboxusercontent.com/u/54337323/2016-09-19/links.txt
304  NOT MODIFIED https://dl.dropboxusercontent.com/u/3967849/shared/raisin_team.csv
304  NOT MODIFIED https://dl.dropboxusercontent.com/u/3967849/shared/PythonAwesome.pdf
>>> 
>>> 
>>> '''
PyObject *x;
'''
'\nPyObject *x;\n'
>>> '''
PyObject *x = PyInt();
'''
'\nPyObject *x = PyInt();\n'
>>> x = 5
>>> x = int()
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
>>> f
<open file 'notes/raisin_team.csv', mode 'r' at 0x101738660>
>>> 
>>> 
>>> open('notes/raisin_team.csv')
<open file 'notes/raisin_team.csv', mode 'r' at 0x1030aec90>
>>> type(open('notes/raisin_team.csv'))
<type 'file'>
>>> 
>>> 
>>> file
<type 'file'>
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
>>> file
<open file 'notes/raisin_team.csv', mode 'r' at 0x103838660>
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
>>> dir()
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'f']
>>> f
<open file 'notes/raisin_team.csv', mode 'r' at 0x101f37660>
>>> 
>>> 
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212

Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300

Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318

Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348

Jones,David,Grape Ager,david@example.com,559-555-2379

Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301

Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2333

Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397

Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-6565

Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513

Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700

>>> line
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700\n'
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212

Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300

Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318

Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348

Jones,David,Grape Ager,david@example.com,559-555-2379

Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301

Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2333

Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397

Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-6565

Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513

Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700

>>> line
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700\n'
>>> print line
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700

>>> print line,
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
>>> print line.strip()
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
>>> print line.rstrip()
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300
Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318
Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348
Jones,David,Grape Ager,david@example.com,559-555-2379
Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301
Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2333
Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397
Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-6565
Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
>>> f
<open file 'notes/raisin_team.csv', mode 'r' at 0x103838660>
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300
Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318
Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348
Jones,David,Grape Ager,david@example.com,559-555-2379
Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301
Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2333
Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397
Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-6565
Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/vcard.py", line 8, in <module>
    raise RuntimeError('oops')
RuntimeError: oops
>>> f
<open file 'notes/raisin_team.csv', mode 'r' at 0x103838660>
>>> line
'Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212\n'
>>> f.tell()
717
>>> len(f)

Traceback (most recent call last):
  File "<pyshell#566>", line 1, in <module>
    len(f)
TypeError: object of type 'file' has no len()
>>> len(line)
70
>>> f
<open file 'notes/raisin_team.csv', mode 'r' at 0x103838660>
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300
Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318
Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348
Jones,David,Grape Ager,david@example.com,559-555-2379
Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301
Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2333
Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397
Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-6565
Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
>>> f
<closed file 'notes/raisin_team.csv', mode 'r' at 0x103038660>
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300
Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318
Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348
Jones,David,Grape Ager,david@example.com,559-555-2379
Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301
Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2333
Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397
Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-6565
Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
>>> f
<closed file 'notes/raisin_team.csv', mode 'r' at 0x103838660>
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300
Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318
Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348
Jones,David,Grape Ager,david@example.com,559-555-2379
Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301
Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2333
Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397
Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-6565
Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
>>> f
<closed file 'notes/raisin_team.csv', mode 'r' at 0x101737660>
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/vcard.py", line 8, in <module>
    raise RuntimeError('oops, I did it again')
RuntimeError: oops, I did it again
>>> f
<closed file 'notes/raisin_team.csv', mode 'r' at 0x103838660>
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300
Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318
Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348
Jones,David,Grape Ager,david@example.com,559-555-2379
Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301
Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2333
Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397
Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-6565
Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
>>> line
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700\n'
>>> line.split()
['Schmidt,Gertrude,VP', 'Business', 'Development,gertrude@example.com,559-555-6700']
>>> len(line.split())
3
>>> line.split(',')
['Schmidt', 'Gertrude', 'VP Business Development', 'gertrude@example.com', '559-555-6700\n']
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
['Hettinger', 'Raymond', 'VP Raisin Smushing', 'raymond@example.com', '559-555-1212']
['Thomas', 'Mary', 'Sr. Associate Raisin Design', 'mary@example.com', '559-555-2300']
['Davis', 'Harold', 'Chief Raisin Picker', 'harold@example.com', '559-555-2318']
['Masterson', 'Martin', 'Asst Raisin Smusher', 'martin@example.com', '559-555-2348']
['Jones', 'David', 'Grape Ager', 'david@example.com', '559-555-2379']
['Zapata', 'Luis', 'VP Grape Sales', 'luis@example.com', '559-555-2301']
['Gunter', 'Fritz', 'Grape Smusher', 'fritz@example.com', '559-555-2333']
['Pichon', 'Esmerela', 'Head Raisin Counter', 'esmerelda@example.com', '559-555-2397']
['Blain', 'Marilyn', 'Raisin Packager', 'marilyn@example.com', '559-555-6565']
['Marks', 'Blair', 'VP Investor Relations', 'blair@example.com', '559-555-6513']
['Schmidt', 'Gertrude', 'VP Business Development', 'gertrude@example.com', '559-555-6700']
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
>>> fields
['Schmidt', 'Gertrude', 'VP Business Development', 'gertrude@example.com', '559-555-6700']
>>> line
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700\n'
>>> fields[0]
'Schmidt'
>>> fields[1]
'Gertrude'
>>> fields[2]
'VP Business Development'
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
>>> 
>>> last
'Schmidt'
>>> first
'Gertrude'
>>> title
'VP Business Development'
>>> email
'gertrude@example.com'
>>> phone
'559-555-6700'
>>> line
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700\n'
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
>>> last
'Schmidt'
>>> line
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700\n'
>>> phone
'559-555-6700'
>>> 
>>> 
>>> 
>>> # interpolation
>>> # formatting
>>> 
>>> 
>>> 
>>> 'hello %s world'
'hello %s world'
>>> 'hello %s world' % 'happy'
'hello happy world'
>>> 'hello %s world' % 5
'hello 5 world'
>>> 
>>> 'hello ' + str(5) + ' world'
'hello 5 world'
>>> 'hello %s world' % 5
'hello 5 world'
>>> 'hello %s %s' % 1, 2

Traceback (most recent call last):
  File "<pyshell#606>", line 1, in <module>
    'hello %s %s' % 1, 2
TypeError: not enough arguments for format string
>>> 'hello %s %s' % (1, 2)
'hello 1 2'
>>> 'hello {}'.format(1)
'hello 1'
>>> 'hello %s %s' % ('a', 'b')
'hello a b'
>>> 'hello %s %s' % (a, b)

Traceback (most recent call last):
  File "<pyshell#610>", line 1, in <module>
    'hello %s %s' % (a, b)
NameError: name 'a' is not defined
>>> 'hello {} {}'.format(1, 2)
'hello 1 2'
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
>>> 
>>> template
'BEGIN:VCARD\nVERSION:2.1\nN:%s;%s\nFN:%s\nORG:California Raisin Co.\nTITLE:%s\nTEL;WORK;VOICE:%s\nADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America\nEMAIL:%s\nEND:VCARD\n'
>>> print template
BEGIN:VCARD
VERSION:2.1
N:%s;%s
FN:%s
ORG:California Raisin Co.
TITLE:%s
TEL;WORK;VOICE:%s
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:%s
END:VCARD

>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============

Traceback (most recent call last):
  File "/Users/mike/teaching/2016-09-19/vcard.py", line 21, in <module>
    print template % last, first, first + ' ' + last, title, phone, email
TypeError: not enough arguments for format string
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
BEGIN:VCARD
VERSION:2.1
N:Hettinger;Raymond
FN:Raymond Hettinger
ORG:California Raisin Co.
TITLE:VP Raisin Smushing
TEL;WORK;VOICE:559-555-1212
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:raymond@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Thomas;Mary
FN:Mary Thomas
ORG:California Raisin Co.
TITLE:Sr. Associate Raisin Design
TEL;WORK;VOICE:559-555-2300
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:mary@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:California Raisin Co.
TITLE:Chief Raisin Picker
TEL;WORK;VOICE:559-555-2318
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:harold@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Masterson;Martin
FN:Martin Masterson
ORG:California Raisin Co.
TITLE:Asst Raisin Smusher
TEL;WORK;VOICE:559-555-2348
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:martin@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:California Raisin Co.
TITLE:Grape Ager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:david@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Zapata;Luis
FN:Luis Zapata
ORG:California Raisin Co.
TITLE:VP Grape Sales
TEL;WORK;VOICE:559-555-2301
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:luis@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Gunter;Fritz
FN:Fritz Gunter
ORG:California Raisin Co.
TITLE:Grape Smusher
TEL;WORK;VOICE:559-555-2333
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:fritz@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Pichon;Esmerela
FN:Esmerela Pichon
ORG:California Raisin Co.
TITLE:Head Raisin Counter
TEL;WORK;VOICE:559-555-2397
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:esmerelda@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Blain;Marilyn
FN:Marilyn Blain
ORG:California Raisin Co.
TITLE:Raisin Packager
TEL;WORK;VOICE:559-555-6565
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:marilyn@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Marks;Blair
FN:Blair Marks
ORG:California Raisin Co.
TITLE:VP Investor Relations
TEL;WORK;VOICE:559-555-6513
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:blair@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:California Raisin Co.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:gertrude@example.com
END:VCARD

>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
BEGIN:VCARD
VERSION:2.1
N:Hettinger;Raymond
FN:Raymond Hettinger
ORG:California Raisin Co.
TITLE:VP Raisin Smushing
TEL;WORK;VOICE:559-555-1212
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:raymond@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Thomas;Mary
FN:Mary Thomas
ORG:California Raisin Co.
TITLE:Sr. Associate Raisin Design
TEL;WORK;VOICE:559-555-2300
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:mary@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:California Raisin Co.
TITLE:Chief Raisin Picker
TEL;WORK;VOICE:559-555-2318
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:harold@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Masterson;Martin
FN:Martin Masterson
ORG:California Raisin Co.
TITLE:Asst Raisin Smusher
TEL;WORK;VOICE:559-555-2348
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:martin@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:California Raisin Co.
TITLE:Grape Ager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:david@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Zapata;Luis
FN:Luis Zapata
ORG:California Raisin Co.
TITLE:VP Grape Sales
TEL;WORK;VOICE:559-555-2301
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:luis@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Gunter;Fritz
FN:Fritz Gunter
ORG:California Raisin Co.
TITLE:Grape Smusher
TEL;WORK;VOICE:559-555-2333
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:fritz@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Pichon;Esmerela
FN:Esmerela Pichon
ORG:California Raisin Co.
TITLE:Head Raisin Counter
TEL;WORK;VOICE:559-555-2397
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:esmerelda@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Blain;Marilyn
FN:Marilyn Blain
ORG:California Raisin Co.
TITLE:Raisin Packager
TEL;WORK;VOICE:559-555-6565
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:marilyn@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Marks;Blair
FN:Blair Marks
ORG:California Raisin Co.
TITLE:VP Investor Relations
TEL;WORK;VOICE:559-555-6513
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:blair@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:California Raisin Co.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL:gertrude@example.com
END:VCARD

>>> f
<closed file 'notes/raisin_team.csv', mode 'r' at 0x101f31660>
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
>>> 
>>> 
>>> f = open('example.txt', 'w')
>>> f.write('hello\n')
>>> f.close()
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
>>> 
============= RESTART: /Users/mike/teaching/2016-09-19/vcard.py =============
>>> import math
>>> math.sqrt(4)
2.0
>>> math.tan(3)
-0.1425465430742778
>>> 
>>> 
>>> import gzip
>>> gzip.open
<function open at 0x103964848>
>>> 
>>> import json
>>> json.load
<function load at 0x10397db18>
>>> 
>>> 
>>> import socket
>>> 
>>> import antigravity
>>> 
>>> 
>>> import qrcode

Traceback (most recent call last):
  File "<pyshell#638>", line 1, in <module>
    import qrcode
ImportError: No module named qrcode
>>> import qr

Traceback (most recent call last):
  File "<pyshell#639>", line 1, in <module>
    import qr
ImportError: No module named qr
>>> import qr_code

Traceback (most recent call last):
  File "<pyshell#640>", line 1, in <module>
    import qr_code
ImportError: No module named qr_code
>>> 
>>> # Criteria for the standard library
>>> # 1. no bugs
>>> # 1. no bugs, lots of users
>>> # 2. stable
>>> # 2. stable, lots of users, no complaints
>>> # 3. general purpose
>>> 
>>> # Guido is BDFL
>>> # NumPy, he says is not general purpose
>>> 
>>> 
============== RESTART: /Users/mike/teaching/2016-09-19/logo.py ==============
>>> turtle.forward(100)
>>> 
>>> 
>>> 
>>> dir(turtle)
['Canvas', 'Pen', 'RawPen', 'RawTurtle', 'Screen', 'ScrolledCanvas', 'Shape', 'TK', 'TNavigator', 'TPen', 'Tbuffer', 'Terminator', 'Turtle', 'TurtleGraphicsError', 'TurtleScreen', 'TurtleScreenBase', 'Vec2D', '_CFG', '_LANGUAGE', '_Root', '_Screen', '_TurtleImage', '__all__', '__builtins__', '__doc__', '__file__', '__forwardmethods', '__func_body', '__methodDict', '__methods', '__name__', '__package__', '__stringBody', '_alias_list', '_make_global_funcs', '_math_functions', '_screen_docrevise', '_tg_classes', '_tg_screen_functions', '_tg_turtle_functions', '_tg_utilities', '_turtle_docrevise', '_ver', 'acos', 'acosh', 'addshape', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'back', 'backward', 'begin_fill', 'begin_poly', 'bgcolor', 'bgpic', 'bk', 'bye', 'ceil', 'circle', 'clear', 'clearscreen', 'clearstamp', 'clearstamps', 'clone', 'color', 'colormode', 'config_dict', 'copysign', 'cos', 'cosh', 'deepcopy', 'degrees', 'delay', 'distance', 'done', 'dot', 'down', 'e', 'end_fill', 'end_poly', 'erf', 'erfc', 'exitonclick', 'exp', 'expm1', 'fabs', 'factorial', 'fd', 'fill', 'fillcolor', 'floor', 'fmod', 'forward', 'frexp', 'fsum', 'gamma', 'get_poly', 'getcanvas', 'getmethparlist', 'getpen', 'getscreen', 'getshapes', 'getturtle', 'goto', 'heading', 'hideturtle', 'home', 'ht', 'hypot', 'isdown', 'isfile', 'isinf', 'isnan', 'isvisible', 'join', 'ldexp', 'left', 'lgamma', 'listen', 'log', 'log10', 'log1p', 'lt', 'mainloop', 'math', 'mode', 'modf', 'onclick', 'ondrag', 'onkey', 'onrelease', 'onscreenclick', 'ontimer', 'os', 'pd', 'pen', 'pencolor', 'pendown', 'pensize', 'penup', 'pi', 'pos', 'position', 'pow', 'pu', 'radians', 'read_docstrings', 'readconfig', 'register_shape', 'reset', 'resetscreen', 'resizemode', 'right', 'rt', 'screensize', 'seth', 'setheading', 'setpos', 'setposition', 'settiltangle', 'setundobuffer', 'setup', 'setworldcoordinates', 'setx', 'sety', 'shape', 'shapesize', 'showturtle', 'sin', 'sinh', 'speed', 'split', 'sqrt', 'st', 'stamp', 'tan', 'tanh', 'tilt', 'tiltangle', 'time', 'title', 'towards', 'tracer', 'trunc', 'turtles', 'turtlesize', 'types', 'undo', 'undobufferentries', 'up', 'update', 'width', 'window_height', 'window_width', 'write', 'write_docstringdict', 'xcor', 'ycor']
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> from turtle import *
>>> dir()
['Pen', 'RawPen', 'RawTurtle', 'Screen', 'ScrolledCanvas', 'Shape', 'Terminator', 'Turtle', 'TurtleScreen', 'Vec2D', '__builtins__', '__doc__', '__name__', '__package__', 'acos', 'addshape', 'asin', 'atan', 'atan2', 'back', 'backward', 'begin_fill', 'begin_poly', 'bgcolor', 'bgpic', 'bk', 'bye', 'ceil', 'circle', 'clear', 'clearscreen', 'clearstamp', 'clearstamps', 'clone', 'color', 'colormode', 'cos', 'cosh', 'degrees', 'delay', 'distance', 'done', 'dot', 'down', 'e', 'end_fill', 'end_poly', 'exitonclick', 'exp', 'fabs', 'fd', 'fill', 'fillcolor', 'floor', 'fmod', 'forward', 'frexp', 'get_poly', 'getcanvas', 'getpen', 'getscreen', 'getshapes', 'getturtle', 'goto', 'heading', 'hideturtle', 'home', 'ht', 'hypot', 'isdown', 'isvisible', 'ldexp', 'left', 'listen', 'log', 'log10', 'lt', 'mainloop', 'mode', 'modf', 'onclick', 'ondrag', 'onkey', 'onrelease', 'onscreenclick', 'ontimer', 'pd', 'pen', 'pencolor', 'pendown', 'pensize', 'penup', 'pi', 'pos', 'position', 'pow', 'pu', 'radians', 'register_shape', 'reset', 'resetscreen', 'resizemode', 'right', 'rt', 'screensize', 'seth', 'setheading', 'setpos', 'setposition', 'settiltangle', 'setundobuffer', 'setup', 'setworldcoordinates', 'setx', 'sety', 'shape', 'shapesize', 'showturtle', 'sin', 'sinh', 'speed', 'sqrt', 'st', 'stamp', 'tan', 'tanh', 'tilt', 'tiltangle', 'title', 'towards', 'tracer', 'turtles', 'turtlesize', 'undo', 'undobufferentries', 'up', 'update', 'width', 'window_height', 'window_width', 'write', 'write_docstringdict', 'xcor', 'ycor']
>>> 
>>> forward(100)
>>> right(45)
>>> forward(50)
>>> 
>>> def el():
	forward(100)
	right(90)

	
>>> clearscreen()
>>> el()
>>> el()
>>> el()
>>> el()
>>> 
>>> def box():
	el()
	el()
	el()
	el()

	
>>> clearscreen()
>>> box()
>>> 
>>> clearsceen()

Traceback (most recent call last):
  File "<pyshell#684>", line 1, in <module>
    clearsceen()
NameError: name 'clearsceen' is not defined
>>> clearscreen()
>>> for i in range(4):
	box()
	right(10)

	
>>> 
>>> def el():
	forward(100)
	right(90)

	
>>> def box():
	el()
	el()
	el()
	el()

	
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> def star():
	angle = 60
	for i in range(360/angle):
		box()
		right(angle)

		
>>> star()

Traceback (most recent call last):
  File "<pyshell#701>", line 1, in <module>
    star()
  File "<pyshell#700>", line 4, in star
    box()
NameError: global name 'box' is not defined
>>> from turtle import *
>>> def el():
	forward(100)
	right(90)

	
>>> def box():
	el()
	el()
	el()
	el()

	
>>> def star():
	angle = 60
	for i in range(360/angle):
		box()
		right(angle)

		
>>> star()
>>> 
>>> def star(angle):
	for i in range(360/angle):
		box()
		right(angle)

		
>>> star(50)
>>> 
>>> clearscreen()
>>> begin_fill()
>>> color('red')
>>> fillcolor('purple')
>>> star(60)
>>> end_fill()
>>> 
