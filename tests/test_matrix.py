import sys
sys.path[0] = '/home/runner/machine-learning/src'

from matrix import Matrix

matrix_1 = Matrix([[3, 2], [4, 4], [5, 6]])
matrix_2 = Matrix([[4, 0, 2], [0, 6, 3]])
matrix_3 = Matrix([[1, 2], [3, 4]])
matrix_4 = Matrix([[4, 3], [2, 1]])
matrix_5 = Matrix([[1, 2], [3, 4], [5, 6]])

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