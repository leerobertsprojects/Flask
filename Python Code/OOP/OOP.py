class Animal:

    def __init__(self):
        print('Animal Created')

    def report(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')


a = Animal()
a.__init__()
a.eat()
a.report()

# Inheritance


class Dog(Animal):

    def __init__(self, breed):
        Animal.__init__(self)
        self.breed = breed

    def Breed(self):
        print('I am a dog')
        self.eat()


    def report(self):
        print('I am a dog')

dog = Dog('pug')
dog.eat()
dog.report()





