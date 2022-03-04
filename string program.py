#string
"""
s1='aniket'
print(s1)

s1=' "aniket" '
print(s1)

s2="aniket,/nvijay,/ngawde"
print(s2)

s3="aniket,/tvijay./tgawde"
print(s3)

name='''aniket'''
print(name)
"""

#slice
"""
s1="aniket"
print(s1[:4:-2])
print(s1[: :])
print(s1[4:0:-3])
print(s1[:2:-3])
"""
"""
s1="itvedant"
print(s1)
print(s1[0])

l=len(s1)
print("length is",l)
print("s1[0]:-",s1[0])

s2="itvedant"
print(s2)
print(s1[0])
print(s1[2: :])
print(s1[2::5])
"""
"""
a="aniket"
b="gawde"
print("address of a is",id(a))
print("address of b is",id(b))
"""

#properties method of string
"""
s1="itvedant"
s2=s1.lower()
print(s1)
print(s2)

s3='itvedant'
s4=s3.upper()
print(s3)
print(s4)
"""
"""
s1="gawde"
s2=s1.upper
print("s1 in upper case",s1.upper())

s1="gawde"
s2=s1.lower
print("s1 in lower case",s1.lower())

s1="gawde"
s2=s1.capitalize
print("s1 in capitalize",s1.capitalize())

s1="gawde"
s2=s1.title
print("s1 in title case",s1.title())
"""
"""
s1="i love python"
s4=s1.partition('love')
print(s4)

s1="i love python"
s4=s1.split('love')
print(s4)
"""
"""
l2={"raj","jay","ajay"}
s2="".join(l2)
s3="-".join("aniket")
print(s2)
print(s3)
print(string.ascii_letters)
"""
for i in range(1,100,2):
    print(i,end=' ')

