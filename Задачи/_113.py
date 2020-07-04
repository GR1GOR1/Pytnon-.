from template import *
from sympy import *
from sympy.abc import*
import random

#1.13
class Task1_13(Task):
    def __init__(self):
        self.p1 = random.randrange(8,12,1)/10 #годовые потери
        self.p2 = random.randrange(13,18,1)/10 
        self.p3 = random.randrange(22,25,1)/10  
        super().__init__("1_13", self.p1, self.p2, self.p3)

    def get_answer(self):
        a = 1/self.p1
        b = 1/self.p2
        c = 1/self.p3
        res = 1 - (1 - exp(-a * 3)) * (1 - exp(-b * 3)) * (1 - exp(-c * 3))
        return str(format(round(res,3),'.2f'))

Task1_13 = Task1_13()
print(Task1_13.description)
print(Task1_13.get_answer())



