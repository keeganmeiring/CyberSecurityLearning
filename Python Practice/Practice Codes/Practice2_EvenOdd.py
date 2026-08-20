# This program determines whether an integer is even or odd

num = int(input("Enter a whole number: "))

# Logic. Determine if the number is even or odd.
# Using modulo (%) to use the fraction/remainder of a simple calc to see if it's whole or not. 
# If the calc returns with a decimal place, then it is odd. If it is a whole number answer, then its even. 

if num % 2 == 0:
    print(f" The number ({num}) entered is even.")
else:
    print(f" The number ({num}) entered is odd.")