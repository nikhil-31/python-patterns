

mat_1 =  [
            [2, 14, 8], 
            [12, 7, 14], 
            [3, 3, 7]
        ]

mat_2 = [
            [3, 1, 1, 7], 
            [15, 12, 13, 13], 
            [4, 14, 12, 4],
            [10, 5, 11, 12]
        ]
def rotate_img(matrix):
    n = len(matrix)

    for row in range(n // 2):

        for col in range(row, n - row - 1):

            matrix[row][col], matrix[col][n - row - 1] = matrix[col][n - row - 1], matrix[row][col]

            matrix[row][col], matrix[n - row  - 1][n - col - 1] = matrix[n - row  - 1][n - col - 1], matrix[row][col]

            matrix[row][col], matrix[n - col - 1][row] = matrix[n - col - 1][row],  matrix[row][col]

    return matrix

# print(rotate_img(mat_1))

print(rotate_img(mat_2))

