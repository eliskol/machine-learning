import math
import sys

sys.path.insert(1, sys.path[0].replace("tests", "src"))
from gradient_descent import minimize
from gradient_descent import multivar_minimize


def fprime_test_1(x):
    return 2 * x


def fprime_test_2(x):
    return 2 * x + 9 * (x**2) + 4 * (x**3) + 3


assert math.isclose(minimize(fprime_test_1, -12, 0.91, 100000), 0, abs_tol=1e-09)

assert math.isclose(minimize(fprime_test_2, 10, 0.001, 100000), -2.17851, rel_tol=1e-5)


def two_var_func(vec):
    x, y = vec[0], vec[1]
    return [(x + 20) ** 3, (y + 10)]


min = multivar_minimize(two_var_func, [-3, 30], num_iterations=1000000)
assert round(min[0], 0) == -20 and round(min[1], 0) == -10


def two_variable_grad(vec):
    x, y = vec[0], vec[1]
    return [2 * (x - 1), 3 * (y - 1) ** 2]


min = multivar_minimize(two_variable_grad, [2, 5], learning_rate=0.01)
assert round(min[0], 1) == 1 and round(min[1], 1) == 1


def three_variable_grad(vec):
    x, y, z = vec[0], vec[1], vec[2]
    return [2 * (x - 1), 3 * (y - 1) ** 3, 5 * (z - 1) ** 7]


min = multivar_minimize(
    three_variable_grad, [1, -2, 2], learning_rate=0.01, num_iterations=10000
)
assert round(min[0], 1) == 1
assert round(min[1], 1) == 1
assert round(min[2], 0) == 1


def three_variable_grad(vec):
    x, y, z = vec[0], vec[1], vec[2]
    return [(x + 2) ** 3, 0.4 * (y - 7) ** 3, 7 * (z - 6) ** 9]


min = multivar_minimize(
    three_variable_grad, [6, 0, 7], learning_rate=0.01, num_iterations=500000
)
assert round(min[0], 0) == -2 and round(min[1], 0) == 7 and round(min[2], 0) == 6


def four_var_grad(vec):
    return [
        12 * (vec[0] - 90),
        0.3 * (vec[1] + 1),
        (vec[2] - 2) * (vec[2] + 2),
        vec[3] - 9,
    ]


min = multivar_minimize(four_var_grad, [10, 5, 6, 9], num_iterations=100000)
assert (
    round(min[0], 0) == 90
    and round(min[1], 0) == -1
    and round(min[2], 0) == 2
    and round(min[3], 0) == 9
)
