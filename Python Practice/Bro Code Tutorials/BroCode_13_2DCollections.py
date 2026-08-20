# 2D Collections - a list of lists. Good for creating matrices like tables. 

# fruits =        ["apple", "lychee", "tomato", "banana", "guava"]
# vegetables =    ["carrot", "cucumber", "broccoli", "cabbage", "potato"]
# meats =         ["chicken", "beef", "pork", "lamb", "fish"]

# groceries = [fruits, vegetables, meats]
# # print(groceries[2][2])

# for food in groceries:
#     print(food, end=" ")

# fruits =        ["apple", "lychee", "tomato", "banana", "guava"]
# vegetables =    ["carrot", "cucumber", "broccoli", "cabbage", "potato"]
# meats =         ["chicken", "beef", "pork", "lamb", "fish"]

# groceries = [("apple", "lychee", "tomato", "banana", "guava"), 
#              ("carrot", "cucumber", "broccoli", "cabbage", "potato"), 
#              ("chicken", "beef", "pork", "lamb", "fish")]

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#         # print()

num_pad = ((7, 8, 9),
           (4, 5, 6),
           (1, 2, 3),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
      print(num, end= " ")
    print()


