from template import *
from sympy import *
from sympy.abc import*
import random

#1.12
class Task1_12(Task):
    def __init__(self):
        self.p1 = random.randrange(8,12,1) #время до отказа оборудования
        self.p2 = random.randrange(40,60,5) #проценты по выплате
        self.p3 = random.randrange(1000,2000,100) #ожидаемые выплаты клмпании 
        super().__init__("1_12", self.p1, self.p2, self.p3)

    def get_answer(self):
        lam = 1/self.p1
        res = self.p3/((2 - exp(-lam) - exp(-3 * lam)) * self.p2/100)
        return str(format(round(res,3),'.2f'))

Task1_12 = Task1_12()
print(Task1_12.description)
print(Task1_12.get_answer())


