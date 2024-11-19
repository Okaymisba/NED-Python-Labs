try:
    while True:
        user_input = input("Enter anything (Ctrl+D to trigger EOFError): ")
        print(f"You entered: {user_input}")
except EOFError:
    print("\nEOFError encountered.")
