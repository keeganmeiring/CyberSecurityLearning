# Here we build a calculator in python

operator = input("Enter an operator (+, -, * or /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result),2)
elif operator == "=":
    result = num1 - num2
    print(round(result),2)
elif operator == "*":
    result = num1 * num2
    print(round(result),2)
elif operator == "/":
    result = num1 / num2
    print(round(result),2)
else:
    print(f"{operator} is not a valid operator.")