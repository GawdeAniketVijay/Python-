#Write a program to Accept marks 0f 5 subject each subject out 100 and Display Each subject marks.
#Total Marks, Percentage and  Grade.
name=input("enter a name:")
marathi=int(input("enter marks of marathi:"))
hindi=int(input("enter marks of hindi:"))
english=int(input("enter marks of english:"))
history=int(input("enter marks of history:"))
datascience=int(input("enter marks of data science:"))
total=marathi+hindi+english+history+datascience
print("total marksheet of student is:",total)
#percentage
percentage=total/5
print("percentage of the student is:",percentage)
#grade
if percentage>=80 and percentage<=100:
    print("your grade is A+")
elif percentage>=70 and percentage<=80:
    print("your grade is A")
elif percentage>=60 and percentage<=70:
    print("your grade is B")
elif percentage>=50 and percentage<=60:
    print("your grade is c")
elif percentage>=40 and percentage<=50:
    print("your grade is D")
else:
    print("fail")
    

