import math
import sys

sys.path.insert(1, sys.path[0].replace('tests', 'src'))
from gradient_descent import minimize


def fprime_test_1(x):
    return 2 * x


def fprime_test_2(x):
    return 2 * x + 9 * (x ** 2) + 4 * (x ** 3) + 3


assert math.isclose(minimize(fprime_test_1, -12, 0.91, 100000), 0, abs_tol=1e-09)
assert math.isclose(minimize(fprime_test_2, 10, 0.001, 100000), -2.17851, rel_tol=1e-5)
