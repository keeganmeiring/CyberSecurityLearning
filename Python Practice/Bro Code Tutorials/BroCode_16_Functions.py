# Functions = a block of reusable code
#            you NEED to place a set of () after the function in order to be able to use/invoke it


# Return
# This returns the defined function once the parameters have been entered. Allowing you to print the returned/processed function.

# -----------------------------------------------------------------

# def create_name(first, middle, last):
#     first = first.capitalize()
#     middle = middle.capitalize()
#     last = last.capitalize()
#     return first + " " + middle + " " + last

# full_name = create_name("keegan","robert","meiring" )

# print(full_name)

# def happy_birthday(name, age): - works
#     name = name.capitalize()
#     print("Happy birthday to you")
#     print("Happy birthday to you")
#     print(f"Happy birthday dear {name}")
#     print("Happy birthday to you!")
#     print(f"You are {age} years old.")
#     return

# song = (happy_birthday("dave", 21))

# print(song)

# -----------------------------------------------------------------

# Greet - Works

# def greet(name):
#     print()
#     print(f"Hello, {name}. Welcome!")
#     print()
#     return

# greet("Keegan")

# greet("Olivia")

# greet("Dad")

# -----------------------------------------------------------------

# Calculator Function - Works

# def add(x, y):
#     z = x + y
#     return z

# def subtract(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# def divide(x, y):
#     try:
#         z = x / y
#         return z
#     except ZeroDivisionError:
#          return "Error, cannot divide by zero."

# x = 1
# y = 0

# print()
# print("Math results")
# print()
# print("Division: ")
# print(f"{x} / {y} = {divide(x, y)}")
# print()
# print("Multiplication: ")
# print(f"{x} x {y} = {multiply(x, y)}")
# print()
# print("Addition: ")
# print(f"{x} + {y} = {add(x, y)}")
# print()
# print("Subtraction: ")
# print(f"{x} - {y} = {subtract(x, y)}")


# -----------------------------------------------------------------

# Grade Checker - Works

# def grade(score):
#     if score == 100:
#         return "You got full marks! Congratulations. Your grade is A."
#     if score >= 90:
#         return "Your grade is A. Congratulations."
#     if score >= 80:
#         return "Your grade is B. Well done."
#     if score >= 70:
#         return "Your grade is C."
#     if score >= 60: 
#         return "Your grade is D."
#     else:
#         return "You failed the assessment."

# print(grade(100))

# -----------------------------------------------------------------

# Analyser - Works, but is too simplified.

# def total(x, y):
#     total = x + y
#     return total 

# def average(x, y):
#     total = (x + y) / 2
#     return total

# def highest(x, y):
#     if x > y:
#         return x
#     if y > x:
#         return y

# def lowest(x, y):
#     if x < y:
#         return x
#     if y < x:
#         return y

# x = 10
# y = 20

# print(f"The total amount is: {total(x,y)}.")
# print(f"The average of x and y is: {average(x,y)}.")
# print(f"The highest value between x and y is: {highest(x,y)}.")
# print(f"The lowest value between x and y is: {lowest(x,y)}.")

# -----------------------------------------------------------------

# Analyser 2.0 - Better

def analyse(numbers):
    total = 0
    highest = numbers[0]
    lowest = numbers[0]

    for num in numbers:
        total += num
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num
    
    average = total / len(numbers)

    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")

analyse([21, 13, 46, 75, 99, 81 ,53])