# Shopping Cart Program

foods = []
prices = []
total = 0 

while True: 
    food = input("Enter a food item to buy (q to quit): ")
    if food.lower() == "q":
        break
    else: 
        price = float(input(f"Enter the price of the {food}: $"))
        foods.append(food)
        prices.append(price)

print("==== Your Cart ====")

for food in foods:
    print(food)

for price in prices:
    total = total + price
    #total += price

print(f"Your total comes to: ${total:.2f}")
