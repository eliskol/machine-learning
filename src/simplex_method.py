from operator import indexOf
from matrix import Matrix


def simplex_method(initial_array):
    simplex_matrix = Matrix(initial_array)
    while max(simplex_matrix.rows[0][0:-1]) > 1e-8:
        index_of_variable_with_largest_slope = simplex_matrix.rows[0].index(
            max(simplex_matrix.rows[0])
        )
        index_of_strictest_constraint_row = 1

        for i in range(1, simplex_matrix.num_rows):
            row = simplex_matrix.rows[i]
            current_row_constraint = row[-1] / row[index_of_variable_with_largest_slope]

            strictest_constraint_so_far = (
                simplex_matrix.rows[index_of_strictest_constraint_row][-1]
                / simplex_matrix.rows[index_of_strictest_constraint_row][
                    index_of_variable_with_largest_slope
                ]
            )

            if (
                current_row_constraint < strictest_constraint_so_far
                and current_row_constraint > 0
            ):
                index_of_strictest_constraint_row = i

        simplex_matrix.clear_above(
            index_of_strictest_constraint_row, index_of_variable_with_largest_slope
        )
        simplex_matrix.clear_below(
            index_of_strictest_constraint_row, index_of_variable_with_largest_slope
        )

    return simplex_matrix.rows


simplex_test_array = [
    [1, 2, 1, 0, 0, 0, 0],
    [2, 1, 1, 1, 0, 0, 14],
    [4, 2, 3, 0, 1, 0, 28],
    [2, 5, 5, 0, 0, 1, 30],
]

# print(simplex_method(simplex_test_array))

simplex_test_array2 = [
    [20, 10, 15, 0, 0, 0, 0, 0],
    [3, 2, 5, 1, 0, 0, 0, 55],
    [2, 1, 1, 0, 1, 0, 0, 26],
    [1, 1, 3, 0, 0, 1, 0, 30],
    [5, 2, 4, 0, 0, 0, 1, 57],
]

simplex_method(simplex_test_array2)
