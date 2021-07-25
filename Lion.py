# !usr/bin/python3
from Animal import Animal
from util import getYesNoInput

class Lion(Animal):
    def __init__(self, name, age):
        species = "Lion"
        domesticated = False
        sound = "ROAR!"

        super().__init__(species, name, age, domesticated, sound)

    def annoy(self):
        print("You decided to bother the lion...")
        self.makeSound()
        print("You were eaten by the lion...")

    def playFetch(self, myObject):
        print("You want to play fetch with a lion? Wow, ballsy...")
        print("You have", myObject.name, ", are you sure you want to throw it at the lion?")
        if(getYesNoInput() is True):
            self.annoy()
        else: print("That's probably a good idea")
