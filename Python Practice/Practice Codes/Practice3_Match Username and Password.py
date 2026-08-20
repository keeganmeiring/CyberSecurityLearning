# This program runs 2 to inputs against saved credentials to see if they match.

username = "Administrator"
password = "Password!"

user = input("Please enter your username: ")
pword = input("Please enter your password: ")

if user == username and pword == password:
    print("The credentials you have entered are correct. Login successful.")

else:
    print("The credentials you have entered are incorrect. Login failed.")