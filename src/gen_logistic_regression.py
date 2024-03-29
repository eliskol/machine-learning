from matrix import Matrix
from helper import put_last_entry_first
import math


class LogisticRegressor:
    def fit(self, data, interaction_terms=None, lower_bound=0, upper_bound=1):
        self.coefficients = {}
        self.num_interaction_terms = 0
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

        y_matrix_rows = [
            [math.log(((upper_bound - point[-1]) / (point[-1] - lower_bound)))]
            for point in data
        ]
        y_matrix = Matrix(y_matrix_rows)

        coefficient_matrix_rows = []
        for point in data:
            row_to_append = point[:-1]
            row_to_append.append(1)
            coefficient_matrix_rows.append(row_to_append)

        if interaction_terms is not None:
            self.num_interaction_terms = len(interaction_terms)

            for interaction_term in interaction_terms:
                self.coefficients[interaction_term] = None

                for i in range(0, len(y_matrix.rows)):
                    interaction_term_to_append = 1

                    for term in interaction_term:
                        interaction_term_to_append *= data[i][term - 1]

                    coefficient_matrix_rows[i].insert(-1, interaction_term_to_append)

        # print(coefficient_matrix_rows)

        coefficient_matrix = Matrix(coefficient_matrix_rows)
        # coefficient_matrix.print()
        # print('\n')
        transpose_times_y = coefficient_matrix.transpose().matrix_multiply(y_matrix)
        transpose_times_coefficients = coefficient_matrix.transpose().matrix_multiply(
            coefficient_matrix
        )
        # transpose_times_coefficients.print()
        m_and_b_matrix = transpose_times_coefficients.inverse().matrix_multiply(
            transpose_times_y
        )

        coefficient_first_list = put_last_entry_first(m_and_b_matrix.rows)

        for i in range(0, len(data[0])):
            self.coefficients[i] = coefficient_first_list.pop(0)[0]

        for key in self.coefficients:
            if self.coefficients[key] is None:
                self.coefficients[key] = coefficient_first_list.pop(0)[0]

    def predict(self, point_to_predict_at):
        if self.coefficients is None:
            return "no dtata to fit"
        if len(point_to_predict_at) != len(self.coefficients) - (
            self.num_interaction_terms + 1
        ):
            return ":cursed:"
        answer = 0
        # for i in range(0, len(point_to_predict_at)):
        # answer += point_to_predict_at[i] * self.coefficients[i + 1]
        for beta in self.coefficients:
            if beta == 0:
                continue
            elif isinstance(beta, int):
                answer += self.coefficients[beta] * point_to_predict_at[beta - 1]
            else:
                interaction_term = self.coefficients[beta]
                for term in beta:
                    interaction_term *= point_to_predict_at[term - 1]
                answer += interaction_term
        answer += self.coefficients[0]
        return self.lower_bound + (self.upper_bound - self.lower_bound) / (
            1 + math.e**answer
        )
