rows = int(input("Enter Number of Rows: "))

for values in range(rows, 0, -1):
    spaces = '  ' * (rows - values)
    stars = '* ' * ((values * 2) - 1)
    print(spaces + stars)
