'''a=2
b=0
c=a/b
print(c)

l1=[1,2,4,7]
print(l1[2])
print(l1[4])
d={1:'aniket',2:'vijay',3:'gawde'}
print(d[1])
print(d['1'])'''
#without exception handling
a=int(input('enter a first number'))
b=int(input('enter a second number'))
div=a/b
print(div)
print('completed')
#with exception handling
#handle all exceprion in one except block
try:
    a=int(input('enter a first number'))
    b=int(input('enter a second number'))
    div=a/b
    print(div)
except Exception as e:
    print('error occurs in program')
    print('complete')
    print('error')
# handle each exception individualy
try:
    a=int(input('enter a first number'))
    b=int(input('enter a second number'))
    div=a/b
    print('division'+div)
except ZeroDivisionError as e:
    print('second no. should not be zero')
except ValueError as e:
    print('please enter only number')
except Exception as e:
    print('exception',e)
#exception handling with else biock.
try:
    a=int(input('enter a first number'))
    b=int(input('enter a second number'))
    div=a/b
except ZeroDivisionError as e:
    print('second no. should not be zero')
except ValueError as e:
    print('please enter only number')
except Exception as e:
    print('exception',e)
else:
    print('division',div)
#finallay statement
l1=[1,2,4,7,5,26,11]
try:
    a=int(input('enter a index which value you want to print'))
    value=l1[a]
except IndexError as e:
    print(f'index invalid,it must be between 0 to{len(l1)-1}')
except ValueError as e:
    print('value must be number')
else:
    print('value:',value)
finally:
    print('this is final bolck')
print('program complete')
#user define exception
class InvalidAgeError(Exception):
    age=int(input('enter your age'))
if age>17:
    obj=InvalidAgeError(f'Age is less than 18,age={age}')
    raise obj
print('you are eligible')
print('completed')
#raise with handling
class InvalidAgeError(Exception):
    pass
try:
    age=int(input('enter your age'))
    if age<18:
        raise InvalidAgeError('f Age is less then 18,age={age}')
except InvalidAgeError as e:
    print('error',e)
else:
    print('you are eligible')
    print('complete')
#implicit error
try:
    a=int(input('enter your first number'))
    b=int(input('enter your second number'))
    c=a/b
except ZeroDivisionError as e:
    priont('error',e)
else:
    print('division',c)
#explicit manually Exception
try:
    a=int(input('enter your first number'))
    b=int(input('enter your second number'))
    if b==0:
        raise ZeroDivisionError('b should not be Zero')
    c=a/b
except ZeroDivisionError as e:
    print('error',e)
else:
    ('dividion',c)
