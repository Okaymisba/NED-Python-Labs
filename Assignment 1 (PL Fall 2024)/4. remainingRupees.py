amount = int(input("Enter Amount in Rupees: "))

thousands = 0
fiveHundreds = 0
hundreds = 0
fifties = 0
tens = 0
fives = 0
twos = 0
ones = 0

if amount >= 1000:
    thousands += amount // 1000
    amount -= thousands * 1000
if amount >= 500:
    fiveHundreds += amount // 500
    amount -= fiveHundreds * 500
if amount >= 100 >= 1:
    hundreds += amount // 100
    amount -= hundreds * 100
if amount >= 50 >= 1:
    fifties += amount // 50
    amount -= fifties * 50
if amount >= 10 >= 1:
    tens += amount // 10
    amount -= tens * 10
if amount >= 5 >= 1:
    fives += amount // 5
    amount -= fives * 5
if amount >= 2 >= 1:
    twos += amount // 2
    amount -= twos * 2
if amount >= 1:
    ones += amount
    amount -= ones

print(f"1000's in the given Amount is: {thousands}")
print(f"500's in the given Amount is: {fiveHundreds}")
print(f"100's in the given Amount is: {hundreds}")
print(f"50's in the given Amount is: {fifties}")
print(f"10's in the given Amount is: {tens}")
print(f"5's in the given Amount is: {fives}")
print(f"2's in the given Amount is: {twos}")
print(f"1's in the given Amount is: {ones}")