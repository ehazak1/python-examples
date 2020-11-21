'''
Demonstrating a few magic methods.


operator/function       magic method            vocabulary
+                       __add__                 addable
/                       __div__                 divisible
repr, >>>               __repr__
str, print              __str__
[]                      __getitem__             indexable, subscriptable
cmp, <, >, ...          __cmp__, __eq__, ...    comparable
len()                   __len__                 sizeable
for, iter()             __getitem__, __iter__   iterable
next()                  next                    iterator

'''

class Dog:
    'our best friends'

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Dog(%r)' % self.name

    def __add__(self, other):
        return Dog('%s, Jr.' % self.name)

    # __eq__, __lt__, etc. take precedence over __cmp__
##    def __eq__(self, other):
##        return self.name == other.name

    def __cmp__(self, other):
        return cmp(self.name, other.name)

    def bark(self):
        print 'Woof! %s is barking' % self.name


class Kennel:
    'a place to store dogs'

    def __init__(self, dogs=None):
        if dogs is None:
            self.dogs = []
        else:
            self.dogs = dogs

    def __repr__(self):
        return 'Kennel(%s)' % self.dogs

    def __getitem__(self, index):
        return self.dogs[index]

    def __len__(self):
        return len(self.dogs)

    def board(self, dog):
        self.dogs.append(dog)

# "the main section"
if __name__ == '__main__':
   a = Dog('Fido')
   b = Dog('Fluffy')
   c = Dog('Clifford')
   k = Kennel()
   k.board(a)
   k.board(b)
   k.board(c)



print 'my name is', __name__
if __name__ == '__main__':
    print 'executed as a script'
else:
    print 'imported as a module'
