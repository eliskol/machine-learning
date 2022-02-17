from matrix import Matrix


class PolynomialRegressor:

    def fit(self, data, n):
        self.n = n

        y_matrix_rows = [[point[1]] for point in data]
        y_matrix = Matrix(y_matrix_rows)

        coefficient_matrix_rows = []
        for point in data:
            x = point[0]
            row_to_append = [x ** n for n in range(n + 1)]
            coefficient_matrix_rows.append(row_to_append)

        coefficient_matrix = Matrix(coefficient_matrix_rows)

        transpose_times_y = coefficient_matrix.transpose().matrix_multiply(y_matrix)
        transpose_times_coefficients = coefficient_matrix.transpose(
        ).matrix_multiply(coefficient_matrix)

        m_and_b_matrix = transpose_times_coefficients.inverse(
        ).matrix_multiply(transpose_times_y)

        self.coefficients = [coefficient[0]
                             for coefficient in m_and_b_matrix.rows]

    def predict(self, x_value):
        y_value = 0
        for power in range(self.n + 1):
            y_value += self.coefficients[power] * (x_value ** power)
        return y_value
