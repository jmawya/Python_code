"""
Problem Statement
You are given a username and password.
If username is "admin" and password is "1234" → "Login successful"
If username is correct but password is wrong → "Wrong password"
If username is wrong → "User not found"
"""

user=input("username:")
password=input("password:")


if user=="admin" and password=="1234":
   print("Login successful")
elif user=="admin" and password!="1234":
   print("Wrong password")
else:
   print("User not found")
   
