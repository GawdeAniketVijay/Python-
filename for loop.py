#for loop
"""
sl="it veadnt"
for ch in sl:
 print(ch)
 """
#list
"""
l1=[4,6,16,5]
for i in l1:
    print(i,"=",i**2,",",i**3)
"""
#dictionary
"""
dl={'empid':101,'empname':'aniket','empsal':36000}
for i in dl:
    print(i,'=',dl[i])
"""
#wap to accept a stirng from a user to print the vowels and remove.
"""
name=input("enter a name")
for ch in name:
    if ch in 'AEIOUaeiou':
     if (ch>='A' and ch<='Z')or(ch>='a' and ch<='z'):
        print(ch)
"""
for i in range(5):
    print(i,end=" ")
    print()
