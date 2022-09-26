from matrix import Matrix


def simplex_method(initial_array):
    simplex_matrix = Matrix(initial_array)
    while max(simplex_matrix.rows[0]) > 0:
        index_of_variable_with_largest_slope = simplex_matrix.rows[0].index(max(simplex_matrix.rows[0]))
        index_of_strictest_constraint_row = 1

        for i in range(1, simplex_matrix.num_rows):
            row = simplex_matrix.rows[i]
            constraint = row[-1] / row[index_of_variable_with_largest_slope]
            if constraint < simplex_matrix.rows[index_of_strictest_constraint_row][-1] / simplex_matrix.rows[index_of_strictest_constraint_row][index_of_variable_with_largest_slope]:
                index_of_strictest_constraint_row = i

        simplex_matrix.clear_above(index_of_strictest_constraint_row, index_of_variable_with_largest_slope)
        simplex_matrix.clear_below(index_of_strictest_constraint_row, index_of_variable_with_largest_slope)

    return simplex_matrix.rows


simplex_test_array = [[1, 2, 1, 0, 0, 0, 0],
                      [2, 1, 1, 1, 0, 0, 14],
                      [4, 2, 3, 0, 1, 0, 28],
                      [2, 5, 5, 0, 0, 1, 30]]

print(simplex_method(simplex_test_array))
# works
# make variables to make the code more intuitive