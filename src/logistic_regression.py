from matrix import Matrix
import math
class LogisticRegressor:

    def fit(self, data):

        for i in range(0, len(data)):
            current_point = data[i]
            if current_point[1] >= 1 or current_point[1] <= 0:
                print('you cant do that')
                return "no"
            
        y_matrix_rows = [[math.log((1 / point[1]) - 1)] for point in data]
        y_matrix = Matrix(y_matrix_rows)

        coefficient_matrix_rows = [[point[0], 1] for point in data]
        coefficient_matrix = Matrix(coefficient_matrix_rows)

        transpose_times_y = coefficient_matrix.transpose().matrix_multiply(y_matrix)
        transpose_times_coefficients = coefficient_matrix.transpose().matrix_multiply(coefficient_matrix)

        m_and_b_matrix = transpose_times_coefficients.inverse().matrix_multiply(transpose_times_y)

        self.coefficients = []
        self.coefficients.append(m_and_b_matrix.rows[1][0])
        self.coefficients.append(m_and_b_matrix.rows[0][0])

    def predict(self, x_value):
        if self.coefficients == None: return "no dtata to fit"
        return 1 / (1 + (math.e**((self.coefficients[1] * x_value) + self.coefficients[0])))
