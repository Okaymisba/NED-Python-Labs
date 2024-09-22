number = int(input("Enter a Number: "))
if number % 2 != 0:
    print("Karachi")
elif number % 2 == 0 and number in range(2,5):
    print("lahore")
elif number % 2 == 0 and number in range(6,21):
    print("Islamabad")
elif number % 2 == 0 and number > 20:
    print("Pakistan")