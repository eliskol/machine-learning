import math


def is_close(a, b):
    return math.isclose(a, b, rel_tol=0.0001)
