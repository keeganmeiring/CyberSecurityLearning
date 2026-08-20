# Exercise 1: Calculate the circumference of a circle

# import math

# Circumference = 2 x pi x R(radius)

#radius = float(input("Enter the radius of a circle: "))

# circumference = 2 * math.pi * radius

# print(f"The circumference is: {round(circumference, 2)}.")


# --------------------------- 


# Exercise 2: Calculate the area of a circle


# import math

# radius = float(input("Enter the radius of a circle: "))

# area = math.pi * pow(radius, 2)

# print(f"The area of the circle is: {round(area, 2)} cm²")

# ----------------------------

# Exercise 3: Calculate the hypotenuse of a right angle triangle

import math

# C = sqrt of (a^2 + b^2)

a = float(input("Enter the length of side a (cm): "))
b = float(input("Enter the length of side b (cm): "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(round(c, 2))