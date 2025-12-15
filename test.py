n1=6
n2=2
n3=n1*n2
print(n3)
n1=4
n3=n1*n2
print(n3)

mark=51
if mark>= 20:
    print("pass")
elif mark<50:
  print("this is nothing")
  
else:
    print("Faill")

mark=input("Enter a value:")
mark=int(mark)
if mark>=90:
   print("Grade")
elif mark>=80:
   print("A+")
elif mark>=70:
   print("A")
elif mark>=60:
   print("A-")

else:
   print("Fail")

"""
Problem Statement
You are given an integer num.
If num is positive, print "Positive".
If num is negative, print "Negative".
If num is zero, print "Zero".
"""
num=input("Give an integer:")  
 
num=int(num)
if num>=1:
   print("Positive")
elif num==0:
   print("Zero") 
else:
   print("Negative")     
#Problem 1: Even or Odd

num=input("Enter a number")
num=int(num)
if num%2==0:
   print("Even")
else:
   print("odd")


   """
   Problem Statement
Given a student's marks (0–100), print the grade.
Grading Criteria
90–100 → A
80–89 → B
70–79 → C
60–69 → D
< 60 → F

   """
number=input("Given a student's marks:")
number=int(number)
if number>=90:
   print("A")
elif number>=80:
   print("B")
elif number>=70:
   print("C")
elif number>=60:
   print("D")
else:
   print("Fail")

"""
Problem Statement
You are given a username and password.
If username is "admin" and password is "1234" → "Login successful"
If username is correct but password is wrong → "Wrong password"
If username is wrong → "User not found"
"""

user=input("username:")
password=input("password:")
user=int(user)
pas=int(password)

if user==admin & password==1234:
   print("Login successful")
elif user==admin & password!=1234:
   print("Wrong password")
else:
   print("User not found")
   