items = {
    ("Laptop", 200000),
    ("Phone", 50000),
    ("Headphones", 5000),
    ("Keyboard", 3000),
    ("Mouse", 2000)
}

total_sales = 0
prices_sold = []

print("Initial items in stock:")
for item in items:
    print(f"Item: {item[0]}, Price: {item[1]} Rupees")

print("\nPurchasing items...")
while items:
    item = items.pop()
    item_name, price = item
    total_sales += price
    prices_sold.append(price)
    print(f"Sold: {item_name}, Price: ${price}")

max_price = max(prices_sold) if prices_sold else 0
min_price = min(prices_sold) if prices_sold else 0

print("\nSales Summary:")
print(f"Total items sold: {len(prices_sold)}")
print(f"Total amount: ${total_sales}")
print(f"Maximum price of an item sold: ${max_price}")
print(f"Minimum price of an item sold: ${min_price}")
