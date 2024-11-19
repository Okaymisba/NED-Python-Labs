def stats(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)

        print(f"line count: {line_count}")
        print(f"word count: {word_count}")
        print(f"character count: {char_count}")


x = input("Enter name of File : ")
stats(x)
