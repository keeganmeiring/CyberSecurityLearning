# If Else statements using True and False logic conditions

# if = execute a process only IF a condition is TRUE
# ELSE do another process
# Decision making

age = int(input("Enter your age: "))

if age >= 18: 
    age = True
    print("You are old enough to sign up, congratulations!")
elif age <= 0:
    print("You are still a fetus.")
else:
    age = False
    print("You must be 18 or older to sign up.")

