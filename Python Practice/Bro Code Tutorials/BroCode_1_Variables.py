# this is my first Python program. Wish me luck.

# We are looking at Variables (String, Int, Float, Boolean) - 4 basic data types
        # A variable behaves as it it was the value that it contains

# Strings Examples (strings of characters)
first_name = "Keegan"
last_name = "Meiring"
food = "sandwiches"
email = "123sandwich@email.com"

print(first_name, last_name)
print(f"Hello {first_name}, you like {food} ")
print(f"Your email is {email}")

# Integer examples (whole numbers)
age = 35
quantity = 12
num_of_students = 20

print(f"You are {age}")
print(f"You would like to buy {quantity} {food}?")
print(f"there are {num_of_students} students in our class")

# Equation examples using Integers
def multiply(age, quantity):
    return f"{age} * {quantity} = {age * quantity}"
print(multiply(age,quantity))

def sum(quantity, num_of_students):
    return f"{quantity} + {num_of_students} = {quantity + num_of_students}"
print(sum(quantity,num_of_students))

def multiply(a,b,c,d):
    return f"{a} * {b} * {c} * {d} = {a * b * c * d}"
print(multiply(1,2,3,4))

def subtract(a,b):
    return f"{a} - {b} = {a - b}"
print(subtract(15,17))

# Floats - a number which has decimal places 

item_1 = 11.99 
item_2 = 6.49
item_3 = 18.29
item_4 = 21.99
item_5 = 8.99

print(f"The order total comes to ${item_1 + item_2 + item_3 + item_4 + item_5}")

distance = 7.61

print(f"You have {distance} kilometers left until you reach your destination.")

#Boolean - true or false logic statements

is_student = True # starts with an uppercase T or F to signify that it's a function/logical statement.

# print(f"Are you a student? {is_student}") - not typically used. T/F usually used within a program

if is_student:
    print("You are a student. Continue as you were. Apologies for the disturbance.")
else:
    print("You are not a student. Get off campus or we'll call security.")
