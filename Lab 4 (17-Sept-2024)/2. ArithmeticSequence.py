first_term = int(input("Enter first term: "))
common_difference = int(input("Enter common difference: "))

while True:
    nth_term = int(input("Enter nth term: "))

    value_of_the_nth_term = first_term + (nth_term - 1) * common_difference
    print(f"The value of {nth_term}th term is {value_of_the_nth_term}")

    while True:
        continue_or_exit = input("Would you like to continue? [Yes/No]: ")
        if continue_or_exit.lower() == "yes":
            break
        elif continue_or_exit.lower() == "no":
            exit()
        else:
            print("Please enter a valid input (Yes or No).")