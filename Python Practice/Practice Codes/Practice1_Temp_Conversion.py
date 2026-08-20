# This program runs a temporary conversion 

# input the temperature value as a float type in order to work in a calculation. A string won't work and would need to be convered.

input_temp = float(input("What is the temperature?: "))
input_type = int(input("Is it Celsius or Farenheit? Enter 1 for C, 2 for F: "))

# Equations: Both options depending on input2 "input_type"

equation1 = ((input_temp * 1.8) + 32)
equation2 = ((input_temp - 32) / 1.8)


# Logic & printing the output
# this section determines the process needed based on answer to input 2: input_type.
#           If 1, then it performs the equation one way and rounds to 1 decimal place.
#           If 2, then it performs the inverse equation and rounds to 1 decimal place.
#           It then prints the answer based on which equation was used

if input_type == 1:
    answer = round(equation1, 1)
    print(f"The converted temperature is: {answer}")
elif input_type == 2:
    answer = round(equation2, 1)
    print(f"The converted temperature is: {answer}")
else:
    print("Invalid input")