
from template import *
from sympy import *
from sympy.abc import*
import random

#1.14
class Task1_14(Task):
    def __init__(self):
        self.p1 = random.randrange(2,6,1) #Количестово заявленных страховых случаев
        super().__init__("1_14", self.p1)
	#self.pic="img\1_14.png"

    def get_answer(self):
        res = (1 + integrate(1-(1-1/(x**3))**self.p1, (x,1,oo)))*1000
        return str(format(float(round(res,3)),'.2f'))

Task1_14 = Task1_14()
print(Task1_14.description)
print(Task1_14.get_answer())



