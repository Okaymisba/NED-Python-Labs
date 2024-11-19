def hexASCII():
    for char in range(ord('a'), ord('z') + 1):
        hex_value = format(char, 'x')
        print(f"{chr(char)}: {hex_value}")


hexASCII()
