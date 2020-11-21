'''
How to loop like a Pythonista.


==============================================
Traditional-style           Generator-style
builds a list               builds an iterator
==============================================
range                       xrange
                            enumerate
                            reversed
zip                         itertools.izip
map                         itertools.imap
filter                      itertools.ifilter
sorted
==============================================


'''

names = ['Luke', 'Leia', 'Han', 'Chewie']

'''
# The bad way...

for i in range(len(names)):
    print names[i]
'''

# The Pythonic Way (tm)
for name in names:
    print name

# Whenever you are looping
# and using an index (``obj[index]``),
# there's probably a better way.

############################################

enumerate(names)
reversed(names)
sorted(names)
sorted(names, key=len)
sorted(names, key=str.lower)

roles = ['hero', 'princess', 'pilot', 'copilot']
zip(names, roles)

lengths = map(len, names)

############################################

def myrange(stop):
    '''
    a re-implementation of `range`
    without using `range`.
    '''
    if not isinstance(stop, int):
        raise TypeError('expected an int, got %r' % stop.__class__.__name__)
    numbers = []
    current = 0
    while current < stop:
        numbers.append(current)
        current += 1
    return numbers

def myrange(a, b=None, step=1):
    # TODO: handle negative step
    if b is None:
        start = 0
        stop = a
    else:
        start = a
        stop = b

    if step == 0:
        raise ValueError('step must not be zero')
    if not isinstance(stop, int):
        raise TypeError('expected an int, got %r' % stop.__class__.__name__)
    numbers = []
    current = start
    while current < stop:
        numbers.append(current)
        current += step
    return numbers




def myxrange(a, b=None, step=1):
    # TODO: handle negative step
    if b is None:
        start = 0
        stop = a
    else:
        start = a
        stop = b

    if step == 0:
        raise ValueError('step must not be zero')
    if not isinstance(stop, int):
        raise TypeError('expected an int, got %r' % stop.__class__.__name__)

    current = start
    while current < stop:
        yield current
        current += step




def mymap(func, sequence):
    results = []
    for element in sequence:
        results.append(func(element))
    return results


def myimap(func, sequence):
    for element in sequence:
        yield func(element)




class Iterable:
    'an iterable can be iterated'

    def __init__(self, maximum):
        self.maximum = maximum

    def __getitem__(self, index):
        if index >= self.maximum:
            raise IndexError(index)
        return index

    def __iter__(self):
        return Iterator(self)


class Iterator:
    'an iterator controls the iteration'

    def __init__(self, seq):
        self.seq = seq
        self.current = 0

    def __iter__(self):
        return self

    def next(self):
        try:
            value = self.seq[self.current]
        except IndexError:
            raise StopIteration
        self.current += 1
        return value








