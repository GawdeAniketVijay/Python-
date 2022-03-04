#to print all even number into the evenlist
"""
l1=(24,6,7,4,17,45,90)
evenlist=[]
for i in l1:
    if i%2==0:
        evenlist.append(i)
print(evenlist)
"""
#for reverse
"""
l1=(24,6,7,4,17,45,90)
evenlist=[]
for i in l1:
    if i%2==0:
        evenlist.insert(0,i)
print(evenlist)
"""
#in single loop
"""
evenlist1=[i for i in l1 if i%2==0]
print(evenlist)
"""
#list comprehension with condition
"""
evenlist1=[i**2 for i in l1 if i%2==0]
print(evenlist1)
#set comprehension
evenlist2={i**2 for i in l1 if i%2==0}
print(evenlist2)
"""
#dictionary
"""
d1={101:18000,
    102:25000,
    103:22000,
    104:24000,
    105:15000
}
sadlist1=[d1[i]for i in d1 if d1[i]>20000]
print(sadlist1)
sadlist2=[i for i in d1.values()if i>20000]
print(sadlist2)
"""
#dictionary comprehension
"""
l1={1,32,5,26,3}
d1={i:i**2 for i in l1}
print(d1)
#to increase the value of employee by 2%
d2={key:value+value*0.02 for key,value in d1.items()}
print(d1)
print(d2)
"""
#radiuslist
radiuslist={2.3,4.7,2.7,3}
d3={key:key*3.14*key for key in radiuslist}
print(d3)
