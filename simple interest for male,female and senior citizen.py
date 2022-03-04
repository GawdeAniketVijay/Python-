#Write a Program to Calculate the Simple Interest for Bank Customer for Fixed Deposit.
age=int(input("enter your age:"))
gen=input("enter your gender:")
p=int(input("enter your principal amt:"))
r=int(input("enter your rate:"))
t=int(input("enter your time of invest:"))
if age>=50 and gen=='f':
    r=8
elif age<=60 and gen=='f':
    r=6
elif age>=60 and gen=='m':
    r=7
else:
    r=5
si=(p*r*t)/100
print("simple interest for fd-",si,'rs')
