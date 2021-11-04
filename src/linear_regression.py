from matrix import Matrix
from helper import put_last_entry_first

class LinearRegressor:

    def fit(self, data, interaction_terms=None):

        self.coefficients = {}

        y_matrix_rows = [[point[-1]] for point in data]
        y_matrix = Matrix(y_matrix_rows)

        coefficient_matrix_rows = []
        for point in data:

            row_to_append = point[:-1]
            row_to_append.append(1)
            coefficient_matrix_rows.append(row_to_append)

        if interaction_terms is not None:
            for interaction_term in interaction_terms:
                self.coefficients[interaction_term] = None
                for i in range(0, len(y_matrix.rows)):
                    interaction_term_to_append = 1
                    for term in interaction_term:
                        interaction_term_to_append *= data[i][term - 1]
                    coefficient_matrix_rows[i].insert(-1, interaction_term_to_append)

        # print(coefficient_matrix_rows)

        coefficient_matrix = Matrix(coefficient_matrix_rows)

        transpose_times_y = coefficient_matrix.transpose().matrix_multiply(y_matrix)
        transpose_times_coefficients = coefficient_matrix.transpose().matrix_multiply(coefficient_matrix)

        m_and_b_matrix = transpose_times_coefficients.inverse().matrix_multiply(transpose_times_y)

        for i in range(0, len(data[0])):
            self.coefficients[i] = put_last_entry_first(m_and_b_matrix.rows)[i][0]


    def predict(self, point_to_predict_at):
        if self.coefficients == None: return "no dtata to fit"
        if len(point_to_predict_at) != len(self.coefficients) - 1: return ":cursed:"
        answer = 0
        for i in range(0, len(point_to_predict_at)):
            answer += point_to_predict_at[i] * self.coefficients[i + 1]
        answer += self.coefficients[0]
        return answer

bruv = LinearRegressor()
bruv.fit([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [
    6, 0, 9], [0, 2, 2], [0, 4, 5], [0, 6, 7], [0, 8, 6], [2, 2, 1], [3, 4, 1]], [(1, 2)])
print(bruv.coefficients)

bruh = LinearRegressor()
# bruh.fit([[1, 0.2], [2, 0.25], [3, 0.5]])
# print(bruh.predict([4]))