sample = [(2, 3), (4, 7), (8, 11), (3, 6)]
maximum_first = max(x[0] for x in sample)
minimum_first = min(x[0] for x in sample)
maximum_second = max(x[1] for x in sample)
minimum_second = min(x[1] for x in sample)

print(f"The Maximum of First Element is : {maximum_first}")
print(f"The Minimum of First Element is : {minimum_first}\n")

print(f"The Maximum of Second Element is : {maximum_second}")
print(f"The Minimum of Second Element is : {minimum_second}")
