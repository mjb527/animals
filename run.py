# !usr/bin/python3
from Animal import Animal
from Dog import Dog
from Lion import Lion
from Object import Object

dog = Dog('Fido', 4)
cat = Animal('Cat', 'Whiskers', 2, True, 'Meow')
elephant = Animal('Elephant', 'Roho', 7, False, 'Harumph!')

dog.getInfo()
# cat.getInfo()
# elephant.getInfo()
# elephant.makeSound()

ball = Object("Ball", 0.2, "Fun to throw and catch, is round")
dog.makeSound()
dog.playFetch(ball)

lion = Lion("Scar", 15)
lion.getInfo()
lion.playFetch(ball)
