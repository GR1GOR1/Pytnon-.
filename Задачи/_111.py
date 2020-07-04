from template import *
from sympy import *
from sympy.abc import*
import random

#1.11
class Task1_11(Task):
    def __init__(self):
        self.p = random.randrange(2200,2800,100)
        super().__init__("1_11",self.p)

    def get_answer(self):
        ex = 4 * self.p
        exx = 4 * 5 * self.p**2
        res = int(sqrt(exx - ex**2))
        return str(format(round(res,3),'.2f'))

Task1_11 = Task1_11()
print(Task1_11.description)
print(Task1_11.get_answer())

