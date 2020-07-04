from template import *
from sympy import *
from sympy.abc import*
import random

#1.43
class Task1_43(Task):
    def __init__(self):
        #Стоимость лечения
        self.s1 = random.randrange(83,93,1)/10 #Случ обр для кажд с шаг 0.5
        self.s2 = random.randrange(109,119,1)/10 #определяем проценты инфляции
        self.s3 = random.randrange(101,111,1)/10
        self.s4 = random.randrange(62,72,1)/10
        self.s5 = random.randrange(77,87,1)/10
        self.s6 = random.randrange(51,61,5)/10
        self.s7 = 7
        #Число 
        self.p1 = random.randrange(982,1382,10) #Случ обр для кажд с шаг 10
        self.p2 = random.randrange(964,1364,10) #определяем средний размер ущерба
        self.p3 = random.randrange(1234,1634,10)
        self.p4 = random.randrange(1340,1740,10)
        self.p5 = random.randrange(1253,1653,10)
        self.p6 = random.randrange(1510,1910,10)
        self.p7 = random.randrange(1667,2067,10)
        
        super().__init__("1_43")
        self.table_1 = [['Год','Средний размер ущерба'],['t-7',self.p1],['t-6',self.p2],
                      ['t-5',self.p3],['t-4',self.p4],['t-3',self.p5],
                      ['t-2',self.p6],['t-1',self.p7]]
        self.table_2 = [['Год','Инфляция'],['t-7',self.s1],['t-6',self.s2],
                      ['t-5',self.s3],['t-4',self.s4],['t-3',self.s5],
                      ['t-2',self.s6],['t-1',self.s7]]
        
    def get_answer(self):
        
        x = [self.s1,self.s2,self.s3,self.s4,self.s5,self.s6,self.s7] #Инфляция
        y = [self.p1,self.p2,self.p3,self.p4,self.p5,self.p6,self.p7] #Средний размер ущерба
        z = [0,0,0,0,0,0,0]
        z[6] = self.p7
        
        for i in range(0,6,1):
            z[i] = (1 + x[i]/100)*y[i]
        
        sum = 0
        for i in range(0,7,1):
            print(z[i])
            sum = sum + z[i]
        
        res = sum/7
        return str(format(round(res,3),'.2f'))

Task1_43 = Task1_43()
print(Task1_43.description)
print(Task1_43.get_answer())