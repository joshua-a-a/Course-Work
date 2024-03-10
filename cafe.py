
# Create a list called menu, which should contain at least four items sold in the cafe

menu = ["Sandwich", "Pastry", "Tea", "Apple"]

# Create a dictionary called stock, which should contain the stock value for each item on your menu.

stock = {
        "Sandwich": 48,
        "Pastry"  : 75,
        "Tea"     : 200,
        "Apple"   : 40,
        }

# Create another dictionary called price, which should contain the prices for each item on your menu.

prices = {
       "Sandwich": 5.99,
       "Pastry"  : 3.99,
       "Tea"     : 2.99,
       "Apple"   : 0.99,
        }

# sanity check, print out price and stock of each item sold on shop. 
for key in prices:
        print(f"\n{key}")
        print(f"Price: {prices[key]}")
        print(f"Stock: {stock[key]}\n")

# calculate the total_stock worth in the cafe. 
total_stock = 0
for key in prices:
        value = prices[key] * stock[key] # individually work out the total value for each key
        total_stock = total_stock + value # work out 

# print out the result of the calculation.
print(f"Total stock value in the Cafe is: £{total_stock}\n") 

