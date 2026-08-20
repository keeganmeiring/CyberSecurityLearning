# Concession stand program to utilise a dictionary function

menu = {"hot dog": 1.99, # key: value
        "burger": 2.49, 
        "cheeseburger": 3.50,
        "milkshake": 3.99,
        "fries": 5.99,
        "steak sandwich": 9.99}

cart = []
total = 0 

print()
print("-------- Menu --------")
print()
for key, value in menu.items(): 
    print(f"{key:<15}: ${value:.2f}")
print()

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None: 
        cart.append(food)

print()
print("----- Your Order -----")

for food in cart: 
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your total comes to: ${total:.2f}")
print()