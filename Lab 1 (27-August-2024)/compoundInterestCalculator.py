
principle_amount = int(input("Enter the Investment Amount: "))
rate_of_interest = float(input("What will be the Annual Interest Rate: "))
time = int(input("Enter Time Period in years: "))
amount = principle_amount * ( 1 + rate_of_interest / 100 ) ** time
compound_interest = amount - principle_amount
print(f"\nCompound Interest is {compound_interest}")