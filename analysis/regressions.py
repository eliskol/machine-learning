import sys
sys.path[0] = '/home/runner/machine-learning/src'
from matrix import Matrix

class LinearRegressor:

    def fit(self, data):
        y_matrix_rows = [[point[1]] for point in data]
        y_matrix = Matrix(y_matrix_rows)

        coefficient_matrix_rows = [[point[0], 1] for point in data]
        coefficient_matrix = Matrix(coefficient_matrix_rows)

        transpose_times_y = coefficient_matrix.transpose().matrix_multiply(y_matrix)
        transpose_times_coefficients = coefficient_matrix.transpose().matrix_multiply(coefficient_matrix)

        m_and_b_matrix = transpose_times_coefficients.inverse().matrix_multiply(transpose_times_y)

        self.coefficients = []
        self.coefficients.append(m_and_b_matrix.rows[1])
        self.coefficients.append(m_and_b_matrix.rows[0])

    def predict(self, x_value):
        

bruh = LinearRegressor()
bruh.fit([[1, 0.2], [2, 0.25], [3, 0.5]])
print(bruh.coefficients)

a = Matrix([[0.5, -1], [-1, 14/6]])
b = Matrix([[2.2], [0.95]])
# a.matrix_multiply(b).print()