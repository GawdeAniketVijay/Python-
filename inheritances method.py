#to find out the both parent
"""class A1:
    def m1(self):
        print('method of A1 class:')
class A2:
    def m1(self):
        print('metod of A2 class:')
class B(A1,A2):
    def m1(self):
        super().m1()
        A2.m1(self)
        print('method of B class')
obj=B()
obj.m1()
B.m1(obj)
#operators oveerloading with different object
class circle:
    def __init__(self,radius):
        self.radius=radius
    def __add__(self,other):
        obj=circle()
        obj.radius=self.radius+other.radius
        return obj
    def __lt__(self,other):
        return self.radius<other.radius
    def __str__(self):
        return f'circle[radius={self.radius}]'
c1=circle(2.3)
c2=circle(3.3)
print(c1)
print(c2)
#hierarchical method:
class vehicle:
    def m1(self):
        print('i am a vehicle')
class bike(vehicle):
    def m2(self):
        print('i am a bike')
class car(vehicle):
    def m3(self):
        print('i am a car')
objbike=bike()
objbike.m1()
objbike.m2()
objcar=car()
objcar.m1()
objcar.m3()
#string foramt into iterable object
class employee:
    def __init__(self,eid,ename):
        self.eid=eid
        self.ename=ename
    def __repr__(self):
        return f'({self.eid},{self.ename})'
    def __str__(self):
        return f'({self.eid},{self.ename})'
e1=employee(101,'aniket')
print(e1)
l1=[e1]
print(l1)
#polymorphims(poly=many,morphims=form's)
#yser define polymorphims with functions
def add(n1,n2=0,n3=0):
    return n1+n2+n3
print('function with 3 parametrs',add(1,2,3))
print('function with 2 parametrs',add(1,2))
print('function with 2 parametrs',add(1))
#without riding
class animal:
    def eat(self):
        print('every animal eat')
class cat(animal):
    def eat(self):
        super().eat()
        print('every cat love to eat fish')
catobj=cat()
catobj.eat()"""
#hybrid inheritances
class school:
    def stud1(self):
        print('i am school')
class teacher(school):
    def stud2(self):
        print('i am a teacher')
class sir(school):
    def stud3(self):
        print('i am sir')
class student(teacher,sir):
    def stud4(self):
        print('i am a student')
obj=student()
obj.stud1()
obj.stud2()
obj.stud3()
obj.stud4()
        
