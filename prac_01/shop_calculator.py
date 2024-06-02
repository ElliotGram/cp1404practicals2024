total_price = 0

number_of_items = int(input("Number of items: "))
if number_of_items >= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price_of_items = int(input("Price of item: "))
    total_price = total_price + price_of_items

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
