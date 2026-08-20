    # Exercise 3: Create a shopping cart programme, with item menu and if/else statements

item1 = "cheese pizza"
item2 = "pepperoni pizza"
item3 = "margerita pizza"

price1 = 9.99
price2 = 12.99
price3 = 14.99

# show menu
print("Menu:")
print(f"1. {item1}", f"${price1}")
print(f"2. {item2}", f"${price2}")
print(f"3. {item3}", f"${price3}")

# input item selection & quantity

choice = int(input("Select item (1-3): "))
quantity = int(input("Enter quantity: "))

# logic

if choice == 1:
    item = item1
    price = price1
elif choice == 2:
    item = item2
    price = price2
elif choice == 3:
    item = item3
    price = price3
else:
    print("Invalid choice")

#Calculate total
subtotal = price * quantity

#Output result

print(f"You ordered: {quantity} x {item}")
print(f"Your order comes to: ${round(subtotal, 2)}")
