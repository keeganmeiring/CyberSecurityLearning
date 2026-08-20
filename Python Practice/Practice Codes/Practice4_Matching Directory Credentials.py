# Database of Users and their corresponding passwords
# Each variable string must be enclosed in "", and passwords divided by a :
# Whole user list encased in {} to show that they are variables/values

users_db = {
    "Olivia": "Password1",
    "Keegan": "Password2",
    "Aubrey": "Password3",
    "Lennon": "Password4"
}
# Ask for input. Enter username and password

username = input("Username: ")
password = input("Password: ")

# Check if it matches an existing user credentials in the database. username and password must match exactly

if username in users_db and users_db[username] == password:
    print(f"Welcome back, {username}!")
else:
    print("Invalid username or password.")