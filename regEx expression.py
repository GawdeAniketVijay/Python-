#regEx
import re
s1='''python is object oriented programming language.
python ie easy to understand.'''
#searching with string in given sting #find method return the value of list
#1.findall()
l1=re.findall('python',s1)
print(l1)
l2=re.findall('[io]',s1)
print(l2)
#2.search method()
matchobj=re.search('python',s1)
print(matchobj)
#here span()is method of match class which index of search word.
print('index range',matchobj.span(),'in',matchobj.string)
#3.split(pattern,string)# to remove the word from sentences
l1=re.split('python',s1)
print(l1)
#sub(oldword,newword,string)# to replace the word
print(s1)
s2=re.sub('python','aniket',s1)
print(s2)
#findall method with pattern
pattern1='[aeiou]'
l1=re.findall(pattern1,s1)
print(l1)
#here it will findall the small vowels in given string
print(l1)
uniquelist=set(l1)
for ch in uniquelist:
    print(ch,':-',l1.count(ch))
#validation
import re
name=input('enter your name')
isfound=re.search('^[a-z]+$',name)
if isfound:
    print('hii',name)
else:
    print('invalid input')
#email pattern
emailpattern='^[a-zA-Z][0-9._]+@[a-z]{3,}.[a-z]{2,3}$'
email=input('enter your email')
isfound=re.search(emailpattern,email)
if isfound:
    print('your email id is',email)
else:
    print('invalid input')
    
