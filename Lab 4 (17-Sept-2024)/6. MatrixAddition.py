def add_matrix(matrix1, matrix2):
    size = len(matrix1)
    result = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

first_matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

second_matrix = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

result = add_matrix(first_matrix, second_matrix)
print(result)