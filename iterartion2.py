'''
How to loop like a Pythonista
'''

names = ['Luke', 'Leia', 'Han', 'Chewie']

enumerate(names)
reversed(names)
sorted(names)
sorted(names, key=len)
sorted(names, key=str.lower)

roles = ['hero', 'princess', 'pilot', 'copilot']

lengths = map(len, names)

#############################################

def myrange(stop):
    '''
    a re-implmentation of `range`
    without using `range`.
    '''
    if not isinstance(stop, int):
        raise TypeError('expected an int, got %r', stop.__class__.__name__)
    numbers = []
    current = 0
    while current < stop:
        numbers.append(current)
        current += 1
    return numbers

def myrange(a, b=None, step=1):
    if b is None:
        start = 0
        stop = a
    else:
        stop = b
        start = a

    if step == 0:
        raise ValueError('step must not be zero')
    if not isinstance(stop, int):
        raise TypeError('expected an int, got %r', stop.__class__.__name__)
    numbers = []
    current = start
    while current < stop:
        numbers.append(current)
        current += step
    return numbers


def mymap(func, sequence):
    results = []
    for element in sequence:
        results.append(func(element))
    return results

# Important note for later ....
def myxmap(func, sequence):
    for element in sequence:
        yield func(element))

class Iterable:
    'an iterable can be iterated'


    def __init__(self, maximum):
        self.maximum = maximum
        
    def __getitem__(self, index):
        if index >= self.maximum:
            raise IndexError(index)
        return index


class Iterator:
    'an iterator controls the iterator'

    def __init__(self, seq):
        self.seq = seq
        self.current = 0

    def next(self):
        try:
            value = self.seq[self.current]
        except IndexError:
            raise StopIteration
        self.current += 1
        return value

    
def myxrange(a, b=None, step=1):
    if b is None:
        start = 0
        stop = a
    else:
        stop = b
        start = a

    if step == 0:
        raise ValueError('step must not be zero')
    if not isinstance(stop, int):
        raise TypeError('expected an int, got %r', stop.__class__.__name__)
    current = start
    while current < stop:
        yield current
        current += step
