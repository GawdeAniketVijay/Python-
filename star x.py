#for star*
for row in range (1,5):
    for sp in range(4,row,-1):
        print(" ",end=' ')
    for col in range(1,2*row):
        print('x',end=' ')
    print()
    
#for number 1,2,3
"""n=int(input("enter a number of rows:"))
for i in range(1,n+1):
  for sp in range(" ",end=' '):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


n=input("enter number og lines")
for col in range(0,n):
    for row in range(0,row+1):
        print("*",end=" ")
    print()"""


for row in range(1,5):
    for sp in range(4,row,-1):
       print(" ",end=" ")
    for col in range(1,2*row):
        print("x",end=" ")
    print()
