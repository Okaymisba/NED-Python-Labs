def calculate_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)


x = 0

while x <= 10:
    print(calculate_factorial(x))
    x += 1
