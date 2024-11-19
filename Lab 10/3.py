def duplicate(file_name):
    try:
        with open(file_name, 'r') as file:
            words = file.read().split()
            seen = set()
            for word in words:
                if word in seen:
                    return True
                seen.add(word)
        return False
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return False


def abc(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()

        words = content.split()
        modified_words = ['xxxx' if len(word) == 4 else word for word in words]
        modified_content = ' '.join(modified_words)

        with open('abc.txt', 'w') as new_file:
            new_file.write(modified_content)
        print("File 'abc.txt' created with modifications.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")


x = input("enter name of the file : ".title())
duplicate(x)
abc(x)
