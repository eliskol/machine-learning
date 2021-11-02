from matrix import Matrix

class LinearRegressor:

    def fit(self, data):
        y_matrix_rows = [[point[-1]] for point in data]
        y_matrix = Matrix(y_matrix_rows)

        coefficient_matrix_rows = []
        for point in data:

            row_to_append = point[:-1]
            row_to_append.append(1)
            coefficient_matrix_rows.append(row_to_append)

        coefficient_matrix = Matrix(coefficient_matrix_rows)

        transpose_times_y = coefficient_matrix.transpose().matrix_multiply(y_matrix)
        transpose_times_coefficients = coefficient_matrix.transpose().matrix_multiply(coefficient_matrix)

        m_and_b_matrix = transpose_times_coefficients.inverse().matrix_multiply(transpose_times_y)

        self.coefficients = [coefficient[0] for coefficient in m_and_b_matrix.rows[:-1]]
        self.coefficients.insert(0, m_and_b_matrix.rows[-1][0])


    def predict(self, point_to_predict_at):
        if self.coefficients == None: return "no dtata to fit"
        if len(point_to_predict_at) != len(self.coefficients) - 1: return ":cursed:"
        answer = 0
        for i in range(0, len(point_to_predict_at)):
            answer += point_to_predict_at[i] * self.coefficients[i + 1]
        answer += self.coefficients[0]
        return answer
