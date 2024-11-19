try:
    with open("Misbah.txt", "r") as file:
        content = file.read()
    print(content)

except IOError as e:
    print(f"An IOError occurred: {e}")
