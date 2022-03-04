#types of function
#wap to print addition of 1 to n numbers
"""
def addition(n):
    if n>0:
        return n+addition(n-1)
    else:
        return 0
ans=addition(3)
print(ans)
"""
#wap to print hii msg 5 times
"""
def sayhii(n):
    if n>0:
     print('hii')
     sayhii(n-1)
    else:
        return 0
sayhii(5)
"""
"""
userlist=[{'name':'aniket','email':'aniket@gmail.com','mobile':'9967506697','password':'2611'},
          {'name':'gawde','email':'gawde@gmail.com','mobile':'8652363008','password':'2601'}]
def login(**vijay):
    for user in userlist:
        if user['email']==vijay['email']and user['password']==vijay['password']:
            return 'login succesfully'
        else:
            return 'in valid email or password'
print(login(email='aniket@gmail.com',password='2611'))
"""
#anonymous of function
"""
sq=lambda x:x**2
ans=sq(2)
print(ans)
#multiply of 2 numbers using lambda
multiply=lambda a,b,c:a*b*c
ans=multiply(26,1,2)
print(ans)
"""
#filter
"""
numlist=['aniket','vijay','vijaya','ankit']
filterlist=list(filter(lambda name:name[0]=='a',numlist))
print("filter list",filterlist)
"""
#map find out the length of a name
"""
namelist=['aniket','vijaya','vijay','gawde']
namelen=list(map(lambda name:len(name),namelist))
print(namelen)
"""
#zip
"""
empid=[101,102,103,104]
empname=['aniket','body','builder','champ']
emplocation=['marol','gym','andheri','mumbai']
empsalary=[50000,60000,25000,45000]
emplist=list(zip(empid,empname,emplocation,empsalary))
print(emplist)
"""
#reduce
from functools import reduce
numlist=[12,26,21,11]
sum=reduce(lambda a,b:a+b,numlist)
print("sum",sum)

