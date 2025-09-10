foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: ₹"))  # Convert price to float
        foods.append(food)
        prices.append(price)

print("\n----- Your Cart -----")
for food, price in zip(foods, prices):  # Display foods with prices
    print(f"{food}: ₹{price:.2f}")  # Format price to 2 decimal places

total = sum(prices)  # Calculate total
print(f"\nYour total is: ₹{total:.2f}")


'''
#Shopping Cart Program 
foods =[] 
prices =[]
 total = 0 
 while True: 
 food = input("Enter a food to buy(q to quit):") 
 if food.lower() == "q":
  break
   else: price = input(f"Enter the price of a {food}:₹") 
   foods.append(food) 
   prices.append(price) 
   print("-----Your Cart-----") 
   for food in foods: 
   print(food, end="") 
   for price in prices:
    total +=price print()
     print(f"Your total is : ₹{total}")'''
