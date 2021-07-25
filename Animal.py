# !usr/bin/python3

class Animal:
    def __init__(self, species, name, age, domesticated, sound):
        self.species = species
        self.name = name
        self.age = age
        self.isDomesticated = domesticated
        self.sound = sound

    def getInfo(self):
        isDomesticated = 'is domesticated' if self.isDomesticated is True else 'is not domesticated'
        print(self.name, 'is a', self.species, 'is', self.age, 'years old and', isDomesticated)

    def makeSound(self):
        print(self.sound)
