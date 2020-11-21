'''
Why object orientation?

Introspection
    Using code to learn about your code

Encapsulation
    Hides the implementation details
    so that backwards compatibility is easy.
    The interface stays the same,
        even as implementation changes.

Polymorphism
    Using the same method or attribute name
    on many classes to avoid if/elif chains
'''
class Pet:
    'named animals'
    
    def __init__(self, name):
        self.name = name

class Dog(Pet):
    'our best friends'

    def talk(self):
        print 'Woof! %s is barking' % self.name

class Cat(Pet):
    'semi-domestic mammal'

    def talk(self):
        print 'Meow. %s is purring' % self.name

a = Dog('Fido')
b = Dog('Clifford')
c = Cat('Socks')

pets = [a, b, c]
for pet in pets:
    pet.talk()
