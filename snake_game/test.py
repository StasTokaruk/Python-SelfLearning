class Dog:
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woof!")

class Labrador(Dog):
    def __init__(self):
        self.temperament = "bark"

pes = Labrador()
pes.bark()