# !usr/bin/python3

class Object:
    def __init__(self, name, weight, description):
        self.name = name
        self.weight = weight # in kg
        self.description = description

    def getDescription(self):
        print(self.description)
