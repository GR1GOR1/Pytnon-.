from template import *
from sympy import *
from sympy.abc import*
import random

#1.18
class Task1_18(Task):
    def __init__(self):
        self.p1 = 0.5#random.randrange(3,7,1)/10 #Значение вероятности <Y
        super().__init__("1_18", self.p1)

    def get_answer(self):
        res = 1 - (self.p1**2)/2
        ans = round(res,3)
        return str(format(ans,'.2f'))

Task1_18 = Task1_18()
print(Task1_18.description)
print(Task1_18.get_answer())

