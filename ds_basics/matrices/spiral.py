

mat_2 = [
            [3, 1, 1, 7], 
            [15, 12, 13, 13], 
            [4, 14, 12, 4],
            [10, 5, 11, 12]
        ]


def spiral(matrix):

    result = []
    rows = len(matrix)
    cols = len(matrix[0])
    direction = 1

    row = 0
    col = -1

    while rows > 0 and cols > 0:

        for _ in range(cols):
            col += direction
            result.append(matrix[row][col])
        rows -= 1


        for _ in range(rows):
            row += direction
            result.append(matrix[row][col])
        cols -= 1

        direction *= -1

    return result

print(spiral(mat_2))