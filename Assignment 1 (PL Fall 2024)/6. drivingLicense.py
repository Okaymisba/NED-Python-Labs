age = int(input("Enter your age: "))
if age >= 18:

    has_license = input("Do you Have a Driving License or not? (yes/no)").strip().lower()

    if has_license == "yes":
        print("You are eligible for Driving.")
    else:
        print("You are not eligible for Driving as you Don't Have a Driving License.")
else:
    print("You can't drive because you are under 18.")