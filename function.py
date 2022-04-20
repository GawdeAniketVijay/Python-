
#wap to create a function to print a "Hello msg"
"""
def sayHii():
    print("hello everyone")
sayHii()
"""
#wap to create welcome function to a specific user
"""
def welcome(name):
     print("hii",name)
     print("welcome itvedant")
welcome('aniket')
welcome('gawde')
"""
"""
def saywelcome(name,age):
    print("hii i am",name,'and my age is',age)
saywelcome('aniket',20)
"""
#addition of n1+n2
"""
def addition(n1,n2):
    return n1+n2
ans=addition(2,5)
print(ans)
"""
#multiple return value
"""
def calc(n1,n2):
    return n1+n2,n1-n2,n2*n2,n1/n2
ans=calc(6,3)
print("addition and subtraction and multiplication and divide")
print(ans)
"""
#writing style in function
#no parameter no return
"""
def add():
 n1=2
 n2=6
 print("addition",n1+n2)
add()
"""
#parameter with return
"""
def add(n1,n2):
    return n1+n2
print("addition is",add(2,6))
print("addition is",add(3,4))
"""
#no parameter with return
"""
def add():
    n1=5
    n2=5
    return n1+n2
print("addition is",add())
"""
#function with default parameter
"""
def add(n1,n2=0):
    return n1+n2
print("addition is",add(6,5))
print("addition is",add(7))
"""
#wap to create function to return multiply of 3 number with 1.requried parameter and 2 default
"""
def mul(n1,n2=1,n3=1):
    return n1*n2*n3
print("multiply is",mul(2,1))
print("multiply is",mul(1))
print("multiply is",mul(1))
"""
#function with variable number of argument
"""
def add(*num):
    sum=0
    for n in num:
        sum+=n
    print("addition",sum)
add(3,7,9,2,3)
add(2,1)
add()
"""
#sequence
"""
l1=[1,2,17,8,9]
additionl1=sum(l1)
print(additionl1)
maxl1=max(l1)
print(maxl1)
minl1=min(l1)
print(minl1)
sortl1=sorted(l1)
print(sortl1)
"""
#key word number of argument
def user(**gawde):
    for key, value in gawde.items():
        print(key,'=',value)
user(id=2611,name='aniket.viajy.gwade',age='21',salary='35000',area='marol',city='mumbai',state='maharashtra')


