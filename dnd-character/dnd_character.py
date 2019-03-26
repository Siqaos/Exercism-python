
import string
import random
import math
def stat():
        roll = random.choices([1,2,3,4,5,6],k=4)
        roll.remove(min(roll))
        mod = sum(roll)
        return mod
def modifier(constitution):
        mod = math.floor((constitution - 10) / 2)
        return mod
class Character:
    def __init__(self):
        self.strength = stat()
        self.dexterity = stat()
        self.constitution = stat()
        self.intelligence = stat()
        self.wisdom = stat()
        self.charisma = stat()
        self.hitpoints = 10 + modifier(self.constitution)
    def ability(self):
        intList = random.choices([1,2,3,4,5,6],k=4)
        return sum(intList) - min(intList)



