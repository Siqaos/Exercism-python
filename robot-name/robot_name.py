import string
import random
class Robot(object):
    old_name = set()
    def __init__(self):
        self.reset()
    def generate_names(self):
        while True:
            name = ''.join(random.choices(string.ascii_uppercase,k=2)) \
            + ''.join(random.choices(string.digits,k=3))
            if name not in self.old_name:
                return name
        return name
    def reset(self):
        self.name = self.generate_names()
        self.old_name.add(self.name)


 
    

