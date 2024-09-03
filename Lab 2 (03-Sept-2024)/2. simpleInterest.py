principleAmount = int(input("Enter Principle Amount: "))
rate = int(input("Enter Annual Rate: "))
time = int(input("Enter Time span in Years: "))
simple_interest = (principleAmount * rate * time) / 100
print(f"The Amount Of Interest is {simple_interest}")
