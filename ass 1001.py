#ass 1001
n=int(input("enter a number"))
k=1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(k%2,end=" ")
        k+=1
    print()
