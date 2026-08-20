## Typecasting is the processes of converting a variable from one datatype to another. Ex: Converting a string to an integer or float
##               str(), int(), float(), bool()

name = "Keegan Meiring"
age = 35
height = 190.8
male = True

print(type(name))
print(type(age))
print(type(height))


round(height)
rounded_height = int(round(height))
print(rounded_height)

# age = float(age)
# print(age)

# age = str(age)
# print(age)

if male:
    print("Congratulations! It's a boy.")
else: 
    print("Congratulations! It's a girl.")

# print(age + 1)

name = bool(name)
if name:
    print("Thank you.") # doesnt work if I add {name} because it's now converted it into a bool
else:
    print("Please re-enter your name.")