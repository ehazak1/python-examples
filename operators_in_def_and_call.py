'''
operators in def and call

= in a ref
    creates a default value
    making an argument optional
    -- allows new features, keeping backwords compatibility

= in a call
    passes arguments by keyword rather than by positioin

* in a call
    unpacks a sequence as positional argumenrs

** in a call
    unpacks a dict as keywork argument

* in a def
    packs positional args into a tuple

    
'''

def power(base): #v1
    return base ** 2

def power(base, exponent=2): # v2
    return base ** exponent

##def power(exponent=2, base=10): #v3
##    return base ** exponent

x = [5,3]
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
