#remove
"""
l1=[1,2,7,4,5]
l1.remove(2)
print(l1)
#index value
l1=[1,2,7,5,4,2]
index=l1.index(2,2)
print("index of 2 is",index)

#countvalue
l1=[2,3,7,4,5]
print("count of 2 in l1",l1.count(2))
"""
#wap to find second index of the value of given list
"""
l1=[2,3,4,7,5,2,4]
element=int(input("enter the element to find second index:"))
if l1.count(element)>0:
  if l1.count(element)>=2:
      print("element is found")
  else:
      print("element is presenting once in list:")
else:
    print("element is not found:")

#reverse()
l2=[1,7,5,2]
l2.reverse()
print(l2)
"""
#sort #ascending order
"""
l2=[1,7,5,4]
l2.sort()
print(l2)

#sort#desending order
l2=[1,7,5,4]
l2.sort(reverse=True)
print(l2)
"""
#copy
l1=[1,2,3,4]
l2=l1
l3=l1.copy
print(l1)
print(l2)
print(l3)
l1.pop(0)
print(l1)
print(l2)
print(l3)
print("address of l1",id(l1))
print("address of l2",id(l2))
print("address of l3",id(l3))
