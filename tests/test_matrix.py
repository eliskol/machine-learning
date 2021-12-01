import sys
sys.path.insert(1, sys.path[0].replace('tests', 'src'))

from matrix import Matrix
from is_close import is_close

matrix_1 = Matrix([[3, 2], [4, 4], [5, 6]])
matrix_2 = Matrix([[4, 0, 2], [0, 6, 3]])
matrix_3 = Matrix([[1, 2], [3, 4]])
matrix_4 = Matrix([[4, 3], [2, 1]])
matrix_5 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_6 = Matrix([[4, 1, 8], [9, 0, 9], [5, 0, 0]])
matrix_7 = Matrix([[0 , 7 , 8 , 5], [3 , 8 , 5 , 0], [7 , 8 , 3 , 2], [2 , 3 , 1 , 6]])
matrix_8 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_9 = Matrix([[5 , 4 , 2 , 4 , 6 , 3 , 8 , 5 , 2 , 7 , 9 , 3 , 0 , 9 , 8], [5 , 2 , 3 , 0 , 3 , 3 , 5 , 7 , 1 , 1 , 9 , 5 , 2 , 1 , 5], [9 , 0 , 2 , 7 , 3 , 1 , 4 , 4 , 4 , 0 , 8 , 3 , 5 , 7 , 0], [2 , 9 , 6 , 4 , 1 , 4 , 5 , 0 , 2 , 5 , 3 , 5 , 0 , 7 , 3], [9 , 0 , 2 , 6 , 7 , 5 , 9 , 5 , 6 , 7 , 3 , 8 , 7 , 0 , 0], [2 , 9 , 1 , 9 , 0 , 3 , 2 , 1 , 5 , 5 , 4 , 0 , 7 , 3 , 3], [6 , 8 , 6 , 6 , 1 , 9 , 2 , 8 , 4 , 2 , 0 , 4 , 2 , 2 , 1], [3 , 4 , 9 , 2 , 5 , 9 , 2 , 4 , 9 , 8 , 5 , 0 , 9 , 6 , 4], [8 , 9 , 9 , 9 , 7 , 3 , 5 , 5 , 7 , 3 , 8 , 1 , 1 , 6 , 5], [9 , 7 , 5 , 0 , 6 , 7 , 2 , 6 , 6 , 3 , 2 , 9 , 5 , 2 , 1], [4 , 9 , 4 , 7 , 8 , 6 , 5 , 5 , 6 , 7 , 4 , 0 , 3 , 4 , 6], [2 , 8 , 0 , 2 , 7 , 5 , 2 , 2 , 4 , 7 , 0 , 9 , 8 , 6 , 2], [3 , 7 , 1 , 6 , 9 , 3 , 2 , 6 , 1 , 9 , 6 , 5 , 9 , 9 , 6], [3 , 6 , 6 , 5 , 1 , 0 , 3 , 1 , 7 , 8 , 6 , 5 , 0 , 0 , 2], [5 , 4 , 1 , 8 , 8 , 2 , 8 , 7 , 4 , 8 , 8 , 6 , 9 , 6 , 3]])
# assert matrix_1.transpose().rows == [[3, 4, 5], [2, 4, 6]]
# assert matrix_2.transpose().rows == [[4, 0], [0, 6], [2, 3]]

# assert matrix_1.add(matrix_2) == "invalid matrix dimensions"
# assert matrix_3.add(matrix_4).rows == [[5, 5], [5, 5]]

# assert matrix_1.subtract(matrix_3) == "invalid matrix dimensions"
# assert matrix_1.subtract(matrix_5).rows == [[2, 0], [1, 0], [0, 0]]

# assert matrix_5.scalar_multiply(2).rows == [[2, 4], [6, 8], [10, 12]]
# assert matrix_2.scalar_multiply(6).rows == [[24, 0, 12], [0, 36, 18]]

assert matrix_4.matrix_multiply(matrix_3).rows == [[13, 20], [5, 8]]
bruh = matrix_4 @ matrix_3
print(bruh.rows)
# assert matrix_2.matrix_multiply(matrix_1).rows == [[22, 20], [39, 42]]


# assert matrix_3.calc_determinant_recursive() == -2
# assert matrix_2.calc_determinant_recursive() == "invalid matrix dimensions (calc_determinant_recursive)"

# assert matrix_1.rref().rows == [[1, 0], [0, 1], [0, 0]]
# assert matrix_2.rref().rows == [[1, 0, 0.5], [0, 1, 0.5]]

# assert matrix_4.inverse().rows == [[-0.5, 1.5], [1.0, -2.0]]
# # matrix_6.inverse().print()
# # assert matrix_6.inverse().rows == [[0, 0, 0.2], [1, -0.888888888888, 0.8], [0, 0.11111111, -0.2]]

# assert is_close(matrix_3.calc_determinant_recursive(), matrix_3.determinant_rref())
# assert is_close(matrix_7.calc_determinant_recursive(), matrix_7.determinant_rref())
# assert matrix_1.determinant_rref() == "cant take determinant"
# assert matrix_8.determinant_rref() == 0
# print(matrix_9.determinant_rref())
# print(matrix_9.calc_determinant_recursive())
