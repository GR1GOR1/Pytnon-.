from template import *
from sympy import *
from sympy.abc import*
import random

#1.42
class Task1_42(Task):
    def __init__(self):
        self.p1 = random.randrange(3664,4064,50) #Случ обр для кажд с шаг 50
        self.p2 = random.randrange(3496,3896,50) #определяем размер ущерба
        self.p3 = random.randrange(3708,4108,50)
        self.p4 = random.randrange(3554,3954,50)
        self.p5 = random.randrange(3120,3520,50)
        self.p6 = random.randrange(3732,4132,50)
        self.p7 = random.randrange(3534,3934,50)
        self.p8 = random.randrange(3776,4176,50)
        super().__init__("1_42" )
        self.table = [['Год','Средний размер ущерба'],['t-8',self.p1],['t-7',self.p2],
                      ['t-6',self.p3],['t-5',self.p4],['t-4',self.p5],['t-3',self.p6],
                      ['t-2',self.p7],['t-1',self.p1]]

    def get_answer(self):
        r = self.p1 + self.p2 + self.p3 + self.p4 + self.p5 + self.p6 + self.p7 + self.p8
        res = r/8
        return str(format(round(res,3),'.2f'))

Task1_42 = Task1_42()
print(Task1_42.description)
print(Task1_42.get_answer())

