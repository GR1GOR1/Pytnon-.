from template import *
from sympy import *
from sympy.abc import*
import random

#1.19
class Task1_19(Task):
    def __init__(self):
        self.p = random.randrange(20,35,5)/10 
        super().__init__("1_19",self.p)

    def get_answer(self):
        res = integrate(((2-self.p/x)*(3/8)*x**2),(x,1.5,2))
        return str(format(round(res,3),'.2f'))

Task1_19 = Task1_19()
print(Task1_19.description)
print(Task1_19.get_answer())

