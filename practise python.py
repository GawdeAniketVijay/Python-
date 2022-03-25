#first python program.
#way 2 display content.
'''name=input("enter your name:")
age=input("enter your age:")
print("hey",name,"you are",age,"years old")'''

#Multiline statement using--> \
'''a=7+5+6+\
   2+3\
   +1
print(a)'''

#numbers
'''a=10
b=a+2
print(b)
print(type(b))
true=True
print(type(true))'''

#Arithmetic Operator (add,sub,mul,div,mod%,floordiv,pow**,)
"""a=12+3
print(a)
b=2-3
print(b)
c=2*3
print(c)
d=5.6/2.5
print(d)
e=12%12
print(e)
f=12//22.6
print(f)
g=5**2
print(g)
h=True+2
print(h)"""

#Comparison Operator is also called as relational operator(==,>,>=,<,<=,!=)
'''x='str'
y='s'
c=x>y
print(c)'''

#logical operator(and,or,not)
'''name="rutvik"
if name.startswith("k")or name.endswith("k"):
    print("name is allowed")
else:
    print("name is not allowed")
a=10
b=12
c=0
x=a<b and a>c
print(x)'''

#Assingment operator(=,+=,-=,*=,/=,%=,//=,**=,|=,^=,>>=,<<=)
'''a=3
b=5
a+=b
print(a)'''

#Conditional statement
'''x=input("enter a number")
a=int(x)
if a==5:
    print("is valid")
else:
    print('not valid')

x=input("enter first number:")
a=float(x)
y=input("enetr second number:")
b=float(y)
z=input("enter third number:")
c=float(z)
if a>b:
    print("a is greater")
if b>c:
    print("b is greater")
else:
    print("c is greater")

x=input("enter a number")
n=int(x)
r=n%2
if r==0:
    print("it is a even")
else:
    print("it is odd")

x=float(input("enter first number:"))
if n>0:
    print("is positive")
else:
    print("is negative")'''

#armstrong number means(153)
'''n=153
a=1*1*1 + 5*5*5 + 3*3*3
print(a)

x=input("enter three digit number:")
n=int(x)
a=n//10
print(a)
b=n%10
print(b)
c=a//10
print(c)
d=a%10
print(d)
sum=b**3+c**3+d**3
print(sum)'''

'''per =float(input("enter percentage:"))
if per >=75:
    print("you got distinct")
elif per >=60:
    print("you got first class:")
elif per >=50:
    print("you got second class:")
elif per >=40:
    print("you got pass")
else:
    print("you r fail:")'''

'''a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))

if a>b:
    print("a is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater")'''

#the range function
'''for i in range(1,20,2): #range function is use to find numbers
    print(i,end="\t")
    #print()-->with this we can see number in column way and without this it will in row format'''

#for loops
'''lines="""hii aniket how r u""" #lines function is use to find string 
for char in lines:
    print(char)

#while loop
name=input("enter your name:")
a=1
while a<=5:
    print(a,name)
    a+=1
else:
    print("loop completed")'''

#nested loop(interview question)
'''lines=int(input('enter number of lines in square'))
rows=0#initalize 
while rows <lines:#condition
    cols=0#initalize 
    while cols <lines:#condition
      print('*', end=' ')
      cols +=1#increment
    print()
    rows +=1#increment
'''

#right angle triangle
'''number=int(input('enter number of lines'))
for row in range(0,number):
    for col in range(0, row+1):
        print('*',end=' ')
    print()'''

#pass
'''name=input("enter your name")
for i in range(10):
    pass

#continue
num=int(input("enter a number"))
for n in range(1,100):
    if n%num==0:
        continue
    print(n,end="-")
print()'''

#break
'''for i in range(10,100):
    if i%9==0:
        break
    print(i)

#infinte loop
total=0
while True:
    total+=int(input("enter a number:"))
    ch=input("enter do u wish u add more numbers y/n:")
    if ch=='y' or ch=='y':
        continue
    else:
        break
print(total)'''

#string
'''s='aniket'
s.capitalize()
print(s[0:5])
print(s[0:2:1])

a='itvedant'
print(a.capitalize())
print(a.count(a))
print(a.lower())
print(a.endswith('t'))
print(a.find('a'))
print(a.index('v'))'''

#list
'''l1=[1,2,3,4,8,5,6,6]
print(sum(l1))
print(max(l1))
print(min(l1))
print(l1[2])
l1.append(7)
print(l1)
l1.insert(0,0)
print(l1)
l1.sort()
print(l1)
l1[l1.index(4)]=10#replace
print(l1)
l1.pop()
print(l1)
l1.remove(6)
print(l1)
print(l1)
l1.reverse()
print(l1)'''

#tuple
'''a=(1,2,3,4,5,6)
b=a[2]
print(b)
t1=tuple(range(1,21,1))
print(t1) 
b=(1,2,3,4,2,5,6,2)
print(b.count(2))
print(b.index(3))
print(b[0:4])
print(b[::-1])'''

#membership operator(or,in,not in)
'''n=int(input('enter the number:'))
if n==20 or n==50 or n==60:
    print('match')
else:
    print('not')

n=int(input('enter the number:'))
if n not in (20,40,60):
      print('match')
else:
    print('not')'''

#indentity operator(is,not is)
'''n=int(input('enter the number:'))
if n is not 30:
    print('different')
else:
    print('identity')
'''
#set
'''s={1,2,3,4,12}
#s.add(12)
#s.discard(3)
#s.add(26)
#s.pop()
#print(s)
s1={5,6,7,8,12}
a=s.union(s1)
print(a)
b=s.intersection(s1)
print(b)
c=s.difference(s1)
print(c)'''

#Dictionary
'''d={'name':'aniket',
   'from':'mumbai',
   'state':'maharashtra'
   }
print(d.items())
print(d.keys())
print(d.values())
print(d.pop('name'))
print(d.get('state'))
d.update({'gawde':'vijay'})
print(d)'''

#Function
'''def function():
    return"hey there,hello world"
x=function()
print(x)

def greeting():
    return'good morning'
y=greeting()
print(y)'''

'''def product():
    num1=int(input('enter the number'))
    num2=int(input('enter the second number'))
    num3=int(input('enter the third number'))
    a=num1+num2+num3
    return a
print(product())'''

#Global variable
'''x=1
def f1():
    #local variable
    x=3
    print("f1:",x)

def f2():
    global x
    x+=3
    print("f2:",x)

def f3():
    global x
    x=20

if __name__=='__main__':
    print("main:",x)
    f1()
    print("main:",x)
    f2()
    print("main:",x)
    f3()
    print("main:",x)'''

#using filter function (lambda)
'''def prime(number):
    for i in range(2,number):
        if number%i==0:
            return False
        return True
lst=list(range(1,100,5))
print("original List=",lst)
prime_lst=list(filter(prime, lst))
print(prime_lst)
'''
#1
'''n=int(input("enetr a number of lines :"))
for row in range(0,n):
    for col in range(0,row+1):
        print("*",end=" ")
    print()

2 n=int(input("enetr a number :"))
mod=n%2
if mod>0:
    print("the number is odd :")

else:
    print("the number is even :")

3 import calendar
y=int(input("enetr a year :"))
m=int(input("enetr a month :"))
d=int(input("enetr a day :"))
print(calendar.month(y,m,d))

4 for row in range(1,5):
    for sp in range(4,row,-1):
        print(" ",end=" ")
    for col in range(1,row*2):
        print("x",end=" ")
    print()

5 num=int(input("enter a number :"))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("the reverse number :",rev)

6 exam=(19,12,2021)
print("the examination date is : %i / %i / %i "%exam)

7 from datetime import date
f=date(2021,11,2)
l=date(2021,12,12)
delta=l-f
print(delta.days)

#8
color_list_1=set(["red","white","orange"])
color_list_2=set(["orange","red"])
print(color_list_1.difference(color_list_2))

#9
p=4
r=2
t=2
si=(p*r*t)
print("the simple interest of interset :",si)

#10
a=int(input("enetr a number :"))
n1=int("%s"% a)
n2=int("%s%s"%(a,a))
n3=int("%s%s%s"%(a,a,a))
print(n1+n2+n3)

#11 import datetime
now=datetime.datetime.now()
print("the current date and time ")
print(now.strftime("%Y-%M-%D %H:%M:%S"))

12)height=float(input("input your height in meters :"))
weight=float(input("input your weight in kg :"))
print("your body mass index is :",round(weight/(height*height),2))

13) def user(**Gawde):
    for key,value in Gawde.items():
        print(key,"=",value)
user(id=2211,name='AniketVijayGawde',Salary=35000,State="Mahrashtra")

#14)
n=int(input("enter a number :"))
for i in range(2,n):
    if n%2==0:
        print("the number is not prime :")
        break
    else:
        print("the number is prime :")

15)
num=float(input("enter a number  :"))
if num>0:
    print("its a positive number :")
elif num==0:
    print("zero")
else: 
    print("its a negative number :")

#16)remove duplicate from list
l1=[1,2,3,4,5,6,2,1,3,6,5]
l1=list(dict.fromkeys(l1))
print(l1)

#17
l1=[1,2,3,4,5,6]
l1.reverse()
print(l1)

#18 calculater
x=input("enter a expression :")
print(eval(x))

from getpass import getpass
username=input("enter a username :")
password=getpass("enter a password :")

for i in range(1,5):
    for j in range(1,5,1):
        print(i,end=" ")
    print()

for i in range(1,5):
    for col in range(1,i+1):
        print(col,end=' ')
    print()

for row in range(1,5):
 for col in range(4,row-1,-1):
    print('x',end=' ')
 print()

#create a function that parameters and checks for equality between any two of them
def compare(a,b,c):
    if int(a)==int(b) or int(a)==int(c) or int(b)==int(c):
        return True
    else:
        return False
print(compare(1,1,2))
print(compare(1,2,2))
print(compare(1,2,1))
print(compare(1,2,3))
print(compare(6,5,"5"))
'''
'''#factorial
n=5
product=3
for i in range(n):
    product=product*(i+1)
print(product)

a=frozenset({"Aniket"})
print(a)

multiply=lambda a,b,c:a*b*c
a=multiply(2,2,2)
print(a)'''











