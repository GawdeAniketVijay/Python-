#wap to print table of number

n=int(input("enter a number"))
for i in range(1,11):
    print(n,'*',i,"=",n*i)
print()

#wap to accept a number from a user and check.
#whether it is loop or not using for loop.
"""
n=int(input("enter a number"))
for i in range(2,n):
    if n%i==0:
        print("the number is not prime")
        break
    print("it is prime")
"""
#wap to print table of number entered number in continue.
"""
for i in range (1,11):
    if i==5:
     continue
    print(i)
"""
#wap to print prime number between 1 to 100.
'''for num in range(1,101):
    for i in range(2,num):
        if num%i==0:
         break
    else:
        print(num,end=' ')
print()'''
#wap to print horizontal line 4*

i=1
while i<5:
    print("*",end=' ')
    i+=1
for i in range(1,5):
    print('*',end='')

#rows
for i in range(1,5):
 for j in range(1,5,1):
    print(i,end=" ")
 print()
