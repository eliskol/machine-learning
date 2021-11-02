from matrix import Matrix
import math
class LogisticRegressor:

    def fit(self, data):

        for i in range(0, len(data)):
            current_point = data[i]
            if current_point[-1] >= 1 or current_point[-1] <= 0:
                print('you cant do that')
                return "no"
            
        y_matrix_rows = [[math.log((1 / point[-1]) - 1)] for point in data]
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

        self.coefficients = [coefficient[0] for coefficient in m_and_b_matrix.rows[::-1]]


    def predict(self, point_to_predict_at):
        if self.coefficients == None: return "no dtata to fit"

        e_power = 0
        for i in range(0, len(point_to_predict_at)):
            e_power += point_to_predict_at[i] * self.coefficients[i + 1]
        e_power += self.coefficients[0]

        return 1 / (1 + (math.e**e_power))
