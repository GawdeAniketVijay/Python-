#set
"""
s1={2,46,13,37,2,10}
print(s1)
#add 1 value
s={4,7,2,3,82,1,21}
s.add(26)
s.update(["aniket"])
print(s)
"""
#remove values from set
"""
s={4,7,2,3,82,1}
print(s)
#remove
s.remove(7)
print(s)
"""
#discard value
"""
s={4,5,6,26,11}
print(s)
s.discard(26)
print(s)
"""
#pop()
"""
s={26,11,12,52,4}
element=s.pop()
print("remove element of pop method is",element)
print(s)
"""
#union method of set
s1={1,4,7,9}
s2={24,11,4,7,25,1,9}
s3=s1.union(s2)
print(s3)
s4=s1.difference(s2)
print(s4)
s6=s1.intersection(s1)
print(s6)
s7=s1.symmetric_difference(s2)
print(s7)
s8=s1|s2
print(s1)
print(s2)
#intersection
s9=s1&s2
print(s9)

