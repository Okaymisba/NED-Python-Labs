totalCalls = int(input("Tell me How many Calls You Would want to make in a Month: "))
price = None
if totalCalls > 200:
    price = 2000 + 50 * 0.60 + 50 * 0.50 + (totalCalls - 200) * 0.40
elif totalCalls > 150:
    price = 2000 + 50 * 0.60 + (totalCalls - 150) * 0.50
elif totalCalls > 100:
    price = 2000 + (totalCalls - 100) * 0.60
else:
    price = 2000
print(f"Your Monthly Charges For {totalCalls} will be {price}")