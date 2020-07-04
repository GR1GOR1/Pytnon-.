from template import *
from sympy import *
from sympy.abc import*
import random

#1.15
class Task1_15(Task):
    def __init__(self):
        self.p1 = random.randrange(15,25,5) #Ущерб дому от величины общего ущерба
        super().__init__("1_15", self.p1)
	self.pic="img\1_15.png"

    def get_answer(self):
        res = 1 - (1 - self.p1/100)**3
        return str(format(round(res,3),'.2f'))

Task1_15 = Task1_15()
print(Task1_15.description)
print(Task1_15.get_answer())




