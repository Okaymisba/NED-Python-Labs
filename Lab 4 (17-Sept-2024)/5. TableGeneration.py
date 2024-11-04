start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))

print("\n--- Multiplication Table ---")
for i in range(start, end + 1):
    row = []
    for j in range(start, end + 1):
        row.append(i * j)
    print(" ".join(f"{num:4}" for num in row))
