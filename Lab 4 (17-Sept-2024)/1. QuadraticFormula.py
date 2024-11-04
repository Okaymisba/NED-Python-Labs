from cmath import sqrt

a = int(input("Enter coefficient of first variable: "))
b = int(input("Enter coefficient of second variable: "))
c = int(input("Enter coefficient of third variable: "))

if a == 0:
    print("Equation cannot be solved as there is zero division.")
else:
    result1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    result2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)

    print(f"x1 = {result1}")
    print(f"x2 = {result2}")
