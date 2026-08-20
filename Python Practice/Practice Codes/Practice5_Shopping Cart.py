# Add values of a shopping card, and tax. Display total

item1 = 15.99
item2 = 3.25
item3 = 4.95
item4 = 16.99
item5 = 9.00

gst = 0.15

subtotal = print(f"Your order subtotal is: ${((item5 * 3) + item2 + (item3 * 6))}")


total = print(f"Your order total comes to: ${round((((item5 * 3) + item2 + (item3 * 6)) * (1 + gst)),2)}")

