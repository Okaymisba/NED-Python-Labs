balance = 1000
withdraw_limit = 5
attempts = 0
while attempts < withdraw_limit:
    if balance != 0:
        amount = int(input("Enter the Amount to withdraw: "))
        if amount > balance:
            print("You Don't Have enough balance!\n")
            continue
        elif amount < 0:
            print("Invalid Amount!\n")
            continue
        else:
            balance -= amount
            print("Withdrawal Successful!")
            print(f"Balance Remaining: {balance}")
            attempts += 1
    else:
        break
