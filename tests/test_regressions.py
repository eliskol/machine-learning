from logistic_regression import LogisticRegressor
from linear_regression import LinearRegressor
import math
import sys
sys.path[0] = '/home/coder/project/src'


# bruh = LinearRegressor()
# bruh.fit([[1, 0.2], [2, 0.25], [3, 0.5]])

# assert math.isclose(bruh.coefficients[0], 0.01666666666, rel_tol=0.01)
# assert math.isclose(bruh.coefficients[1], 0.15, rel_tol=0.00001)
# assert math.isclose(bruh.predict([4]), 0.616666, rel_tol=0.0001)

# bruh2 = LinearRegressor()
# bruh2.fit([[0.7, 0.9], [0.752, 0.69834], [1238, 1289]])

# assert math.isclose(bruh2.coefficients[0], 0.04329, rel_tol=0.0001)
# assert math.isclose(bruh2.coefficients[1], 1.0412, rel_tol=0.0001)
# assert math.isclose(bruh2.predict([9]), 9.41409, rel_tol=0.0001)

# bruh3 = LogisticRegressor()
# bruh3.fit([[1, 0.2], [2, 0.25], [3, 0.5]])

# assert math.isclose(bruh3.coefficients[0], 2.21459, rel_tol=0.0001)
# assert math.isclose(bruh3.coefficients[1], -0.693147, rel_tol=0.0001)
# assert math.isclose(bruh3.predict([2]), 0.304004, rel_tol=0.0001)

# bruh4 = LogisticRegressor()
# bruh4.fit([[5, 0.6], [3, 0.4], [1, 0.2], [7, 0.8]])
# assert math.isclose(bruh4.coefficients[0], 1.82573, rel_tol=0.0001)
# assert math.isclose(bruh4.coefficients[1], -0.45643, rel_tol=0.0001)
# assert math.isclose(bruh4.predict([7]), 0.79726, rel_tol=0.0001)

bruh5 = LinearRegressor()
bruh5.fit([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [0, 8, 6]])
assert bruh5.coefficients == [0.5999999999999996, 0.675, 1.799999999999999]


bruh6 = LinearRegressor()
bruh6.fit([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [0, 8, 6], [0, 6, 7]])
assert bruh6.coefficients == [0.8203125, 0.78515625, 1.7265624999999991]


bruh7 = LogisticRegressor()
bruh7.fit([[9, 0, 0.1], [1, 0, 0.2], [2, 0, 0.4], [4, 0, 0.8], [0, 8, 0.6]])
assert bruh7.coefficients == [0.017376675350033288, -0.05285522293227471, 0.15832393650276566]

bruh8 = LogisticRegressor()
bruh8.fit([])
