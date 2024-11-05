y = 1
x = 14

while y <= 8:
    asterisks = '*' * x
    if y > 4:
        space = ' ' * (x + 4)
        print(space, asterisks)
    else:
        print(asterisks)
    y += 1
