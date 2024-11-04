string = input("Enter a string: ")

if string.casefold() == string.casefold()[::-1]:
    print("Yes,Your String is Palindrome")
else:
    print("No,Your String is not Palindrome")