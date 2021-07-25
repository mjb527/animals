# !usr/bin/python3
from Animal import Animal

class Dog(Animal):
    def __init__(self, name, age):
        species = "Dog"
        domesticated = True
        sound = "Woof"

        super().__init__(species, name, age, domesticated, sound)

    def playFetch(self, thrownObject):
        print("Get the",  thrownObject.name, "!")
        print("**", self.name, "brought back the", thrownObject.name, "**")
