'''
Why object orientation?

Introspection
    Using code to learn about your code

Encapsulaltion
    Hids the implementation details
    so that backwards compatibility is easy
    The interface stays the smae, even as implementation changes

Polymorphism
    Using the same method or attribute name on man classes
    to avoid if/elif/else
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
        print 'Meow, %s is purring' % self.name

        

a = Dog('Fido')
b = Dog('Clifford')
c = Cat('Socks')



def cat_talk(cat):
    print 'Meow, %s is purring' % cat.name

pets = [a, b, c]
for pet in pets:
    pet.talk()
    
