monthsL = ['Jan', 'Feb', 'Mar', 'May']
monthsT = ('Jan', 'Feb', 'Mar', 'May')

monthsL.insert(3, 'Apr')
print("After inserting 'Apr' in list:", monthsL)

try:
    monthsT = monthsT[:3] + ('Apr',) + monthsT[3:]
    print("\nAfter attempting to insert 'Apr' in tuple:", monthsT)
except TypeError as e:
    print("Error:", e)

monthsL.append('Jun')
print("\nAfter appending 'Jun' in list:", monthsL)

try:
    monthsT += ('Jun',)
    print("\nAfter attempting to append 'Jun' in tuple:", monthsT)
except TypeError as e:
    print("Error:", e)

popped_item = monthsL.pop()
print("\nAfter popping from list:", monthsL)
print("Popped item:", popped_item)

try:
    monthsT = monthsT[:-1]
    print("\nAfter attempting to pop from tuple:", monthsT)
except TypeError as e:
    print("Error:", e)

del monthsL[1]
print("\nAfter removing the second item in list:", monthsL)

try:
    monthsT = monthsT[:1] + monthsT[2:]
    print("\nAfter attempting to remove the second item in tuple:", monthsT)
except TypeError as e:
    print("Error:", e)

monthsL.reverse()
print("\nAfter reversing list:", monthsL)

try:
    monthsT = monthsT[::-1]
    print("\nAfter attempting to reverse tuple:", monthsT)
except TypeError as e:
    print("Error:", e)
