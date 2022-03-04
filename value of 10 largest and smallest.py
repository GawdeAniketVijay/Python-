#Write the program to accept the 10 values from the user and find the largest and the smallest among them.
i=1
while i<=10:
    num=int(input("enter a number:"))
    if i==1:
        high=low=num
    if num>high:
        high=num
    if num<low:
        low=num
    i+=1
print("maximum:-",high)
print("lowest:-",low)
