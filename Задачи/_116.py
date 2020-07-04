from template import *
from sympy import *
from sympy.abc import*
import random

#1.16
class Task1_16(Task):
    def __init__(self):
        self.p1 = random.randrange(15,25,1)/10 #Значение X
        self.p2 = random.randrange(5,15,1)/10 #Значение Y
        super().__init__("1_16", self.p1, self.p2)

    def get_answer(self):
        res = integrate(self.p2/(self.p2*self.p1*t + 1),(t,0,oo))
        return round(res,3)

Task1_16 = Task1_16()
print(Task1_16.description)
print(Task1_16.get_answer())

