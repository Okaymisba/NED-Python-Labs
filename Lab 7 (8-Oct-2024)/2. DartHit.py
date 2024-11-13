def is_dart_within_board(x, y):
    return x ** 2 + y ** 2 <= 100


sample_values = [(0, 0), (10, 10), (6, 6), (7, 8)]
result = {values: is_dart_within_board(*values) for values in sample_values}

for keys, items in result.items():
    print(f"{keys} : {items}")
