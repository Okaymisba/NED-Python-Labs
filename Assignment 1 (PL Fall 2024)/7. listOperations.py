numbers = [5, 10, -3, 7, -2, 9, -8, 4, -11]

for number in numbers:
    if number < 0:
        print(f"Skipping processing Negative Number: {number}")
        continue

    if number > 10:
        print(f"Terminating the loop, encountered Number Greater than 10: {number}")

    print(f"Processing Number: {number}")
print("\nAll non-negative numbers less than or equal to 10 are processed")