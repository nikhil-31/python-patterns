"""
https://leetcode.com/problems/matrix-diagonal-sum/?envType=study-plan-v2&envId=programming-skills
"""

mat = [
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]
    ]


def diagonal_sum(mat):
    n = len(mat)
    sum = 0

    for i in range(n):

        sum += mat[i][i]
        sum += mat[n - i - 1][i]

        if n % 2 != 0:
            sum -= mat[n // 2][n // 2]

    return sum


print(diagonal_sum(mat))


