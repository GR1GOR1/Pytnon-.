from template import *
from sympy import *
from sympy.abc import*
import random

#1.40
class Task1_40(Task):
    def __init__(self):
        #Стоимость лечения
        self.s1 = random.randrange(30,70,5) #Случ обр для кажд с шаг 5
        self.s2 = random.randrange(80,120,5) #определяем стоимость лечения
        self.s3 = random.randrange(180,220,5)
        self.s4 = random.randrange(380,420,5)
        self.s5 = random.randrange(780,820,5)
        self.s6 = random.randrange(1580,1620,5)
        #Число 
        self.p1 = random.randrange(1688,1768,10) #Случ обр для кажд с шаг 10
        self.p2 = random.randrange(1306,1386,10) #определяем стоимость лечения
        self.p3 = random.randrange(1829,1909,10)
        self.p4 = random.randrange(1782,1862,10)
        self.p5 = random.randrange(867,947,10)
        self.p6 = random.randrange(109,189,10)
        
        self.pA = self.p1+self.p2+self.p3+self.p4+self.p5+self.p6 #Всего обратившихся человек
        super().__init__("1_40",self.pA)
        self.table = [['Стоимость лечения','Число случаев'],['0-'+str(self.s1),self.p1],[str(self.s1)+'-'+str(self.s2),self.p2],
                      [str(self.s2)+'-'+str(self.s3),self.p3],[str(self.s3)+'-'+str(self.s4),self.p4],[str(self.s4)+'-'+str(self.s5),self.p5],
                      [str(self.s5)+'-'+str(self.s6),self.p6]]
        
    def get_answer(self):
        #Выборочные начальные моменты 1,2 и 3 порядка
        p = 1/self.pA
        x = [self.s1,self.s2,self.s3,self.s4,self.s5,self.s6]
        y = [self.p1,self.p2,self.p3,self.p4,self.p5,self.p6]

        #Считаем 1 начальный момент
        sum = (self.s1/2)*self.p1
        for i in range(1,6,1):
            sum = sum + (x[i-1] + (x[i] - x[i-1])/2)*y[i]
        a1 = p*sum

        #Считаем 2 начальный момент
        sum = ((self.s1/2)**2)*self.p1
        for i in range(1,6,1):
            sum = sum + ((x[i-1] + (x[i] - x[i-1])/2)**2)*y[i]
        a2 = p*sum
        
        #Считаем 2 начальный момент
        sum = ((self.s1/2)**3)*self.p1
        for i in range(1,6,1):
            sum = sum + ((x[i-1] + (x[i] - x[i-1])/2)**3)*y[i]
        a3 = p*sum
        
        s = sqrt(a2 - a1**2) #Среднее отклонение
        a = a3 - 3*a2*a1 + 2*a1**3 #Третий центральный момент
        
        res = a/(s**3)
        return str(format(round(res,3),'.2f'))

Task1_40 = Task1_40()
print(Task1_40.description)
print(Task1_40.get_answer())

