import sys

sys.path[0] = "/workspace/machine-learning/src"

from matrix import Matrix

matrix_9 = Matrix(
    [
        [5, 4, 2, 4, 6, 3, 8, 5, 2, 7, 9, 3, 0, 9, 8],
        [5, 2, 3, 0, 3, 3, 5, 7, 1, 1, 9, 5, 2, 1, 5],
        [9, 0, 2, 7, 3, 1, 4, 4, 4, 0, 8, 3, 5, 7, 0],
        [2, 9, 6, 4, 1, 4, 5, 0, 2, 5, 3, 5, 0, 7, 3],
        [9, 0, 2, 6, 7, 5, 9, 5, 6, 7, 3, 8, 7, 0, 0],
        [2, 9, 1, 9, 0, 3, 2, 1, 5, 5, 4, 0, 7, 3, 3],
        [6, 8, 6, 6, 1, 9, 2, 8, 4, 2, 0, 4, 2, 2, 1],
        [3, 4, 9, 2, 5, 9, 2, 4, 9, 8, 5, 0, 9, 6, 4],
        [8, 9, 9, 9, 7, 3, 5, 5, 7, 3, 8, 1, 1, 6, 5],
        [9, 7, 5, 0, 6, 7, 2, 6, 6, 3, 2, 9, 5, 2, 1],
        [4, 9, 4, 7, 8, 6, 5, 5, 6, 7, 4, 0, 3, 4, 6],
        [2, 8, 0, 2, 7, 5, 2, 2, 4, 7, 0, 9, 8, 6, 2],
        [3, 7, 1, 6, 9, 3, 2, 6, 1, 9, 6, 5, 9, 9, 6],
        [3, 6, 6, 5, 1, 0, 3, 1, 7, 8, 6, 5, 0, 0, 2],
        [5, 4, 1, 8, 8, 2, 8, 7, 4, 8, 8, 6, 9, 6, 3],
    ]
)

print(matrix_9.determinant_rref())
print(matrix_9.calc_determinant_recursive())
