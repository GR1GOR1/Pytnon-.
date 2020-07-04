from template import *
from sympy import *
from sympy.abc import*
import random

#1.33
class Task1_33(Task):
    def __init__(self):
        self.p1 = random.randrange(200,400,50) #Максимальный уровень
        super().__init__("1_33", self.p1)
	self.pic="img\1_33.png"

    def get_answer(self):
        res = self.p1 * ln(2)
        return str(format(round(res,3),'.2f'))

Task1_33 = Task1_33()
print(Task1_33.description)
print(Task1_33.get_answer())
