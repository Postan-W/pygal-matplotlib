from random import randint

class Dice():
    def __init__(self,number_of_sides = 6):
        self.sides = number_of_sides
    def roll(self):
        return randint(1,self.sides)
