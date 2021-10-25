import sys
sys.path[0] = '/home/runner/machine-learning/src'

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

assert matrix_1.transpose().rows == [[3, 4, 5], [2, 4, 6]]
assert matrix_2.transpose().rows == [[4, 0], [0, 6], [2, 3]]

assert matrix_1.add(matrix_2) == "invalid matrix dimensions"
assert matrix_3.add(matrix_4).rows == [[5, 5], [5, 5]]

assert matrix_1.subtract(matrix_3) == "invalid matrix dimensions"
assert matrix_1.subtract(matrix_5).rows == [[2, 0], [1, 0], [0, 0]]

assert matrix_5.scalar_multiply(2).rows == [[2, 4], [6, 8], [10, 12]]
assert matrix_2.scalar_multiply(6).rows == [[24, 0, 12], [0, 36, 18]]

assert matrix_4.matrix_multiply(matrix_3).rows == [[13, 20], [5, 8]]
assert matrix_2.matrix_multiply(matrix_1).rows == [[22, 20], [39, 42]]


assert matrix_3.calc_determinant_recursive() == -2
assert matrix_2.calc_determinant_recursive() == "invalid matrix dimensions (calc_determinant_recursive)"

assert matrix_1.rref().rows == [[1, 0], [0, 1], [0, 0]]
assert matrix_2.rref().rows == [[1, 0, 0.5], [0, 1, 0.5]]

assert matrix_4.inverse().rows == [[-0.5, 1.5], [1.0, -2.0]]
# matrix_6.inverse().print()
# assert matrix_6.inverse().rows == [[0, 0, 0.2], [1, -0.888888888888, 0.8], [0, 0.11111111, -0.2]]

assert is_close(matrix_3.calc_determinant_recursive(), matrix_3.determinant_rref())
assert is_close(matrix_7.calc_determinant_recursive(), matrix_7.determinant_rref())
assert matrix_1.determinant_rref() == "cant take determinant"
assert matrix_8.determinant_rref() == 0