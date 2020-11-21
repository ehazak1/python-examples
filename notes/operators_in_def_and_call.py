'''
operators in def and call

= in a def
    create a default value, making an argument optional
    allows new features, keeping backwards compatibility

= in a call
    pass arguments by keyword, rather than by position

* in a call
    unpacks a sequence as positional arguments

** in a call
    unpacks a dict as keyword arguments

* in a def
    packs positional args into a tuple

** in a def
    packs keyword args into a dict



=====================================================================
operator    in def              in call
=====================================================================
=           default value       keyword arg
*           pack into a tuple   unpack a sequence as positional args
**          pack into a dict    unpack a dict as keyword args
=====================================================================
'''

def power(base): # v1
    return base ** 2

def power(base, exponent=2): # v2
    return base ** exponent

## def power(exp=2, base=10): # v3
##     return base ** exponent

x = [5, 3]
power(*x)

y = {'base': 5, 'exponent': 3}
power(**y)

def foo(*args):
    print args

def bar(**kwargs):
    print kwargs

def baz(*args, **kwargs):
    print args
    print kwargs

