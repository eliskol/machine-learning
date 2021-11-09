import sys
sys.path[0] = '/home/coder/project/src'


from logistic_regression import LogisticRegressor
from linear_regression import LinearRegressor
import math



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

# bruh5 = LinearRegressor()
# bruh5.fit([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [0, 8, 6]])
# assert bruh5.coefficients == [0.5999999999999996, 1.799999999999999, 0.675]


# bruh6 = LinearRegressor()
# bruh6.fit([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [0, 8, 6], [0, 6, 7]])
# assert bruh6.coefficients == [0.8203125, 1.7265624999999991, 0.78515625]


# bruh7 = LogisticRegressor()
# bruh7.fit([[9, 0, 0.1], [1, 0, 0.2], [2, 0, 0.4], [4, 0, 0.8], [0, 8, 0.6]])
# assert bruh7.coefficients == [0.017376675350033288, 0.15832393650276566, -0.05285522293227471]

# bruh8 = LogisticRegressor()
# bruh8.fit([[11, 22, 0.3], [17, 1, 0.6], [0, 10, 0.2]])
# assert bruh8.coefficients == [1.0382279040554385, -0.08697056811000278, 0.03480664570644529]

interaction_term_test_1 = LinearRegressor()
interaction_term_test_1.fit([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [
    6, 0, 9], [0, 2, 2], [0, 4, 5], [0, 6, 7], [0, 8, 6], [2, 2, 1], [3, 4, 1]], [(1, 2)])
assert interaction_term_test_1.coefficients == {(1, 2): -0.6641667008659251, 0: 0.9396930274551654, 1: 1.4395493905692112, 2: 0.7837751877539292}
assert interaction_term_test_1.predict([5, 5]) == -4.5478516025772615

interaction_term_test_2 = LinearRegressor()
interaction_term_test_2_data = [[9, 9, 8, 9, 8, 2, 4, 9, 5, 0, 1, 3, 7, 4, 3], [9, 4, 5, 3, 2, 7, 3, 1, 9, 1, 7, 2, 2, 1, 2], [7, 1, 5, 6, 8, 8, 3, 8, 0, 1, 4, 4, 6, 9, 2], [7, 0, 5, 4, 6, 1, 1, 7, 4, 1, 4, 0, 0, 2, 6], [4, 0, 4, 7, 4, 4, 8, 5, 1, 4, 0, 5, 2, 3, 2], [2, 3, 9, 2, 9, 6, 0, 0, 9, 3, 5, 3, 2, 7, 8], [3, 4, 3, 9, 3, 9, 8, 5, 9, 9, 4, 5, 0, 7, 1], [9, 5, 0, 8, 0, 1, 5, 4, 0, 5, 2, 8, 0, 7, 2], [9, 0, 2, 0, 0, 3, 5, 6, 4, 8, 7, 6, 9, 8, 4], [0, 8, 4, 1, 6, 0, 9, 5, 2, 6, 6, 1, 5, 2, 3], [3, 6, 8, 8, 5, 7, 5, 4, 1, 9, 7, 0, 6, 2, 2], [6, 0, 7, 7, 7, 3, 5, 5, 9, 9, 5, 4, 8, 8, 1], [3, 1, 5, 3, 0, 7, 3, 0, 7, 5, 0, 9, 2, 2, 6], [2, 6, 4, 1, 8, 6, 2, 2, 2, 0, 2, 4, 7, 4, 8], [8, 3, 3, 3, 1, 2, 5, 6, 4, 6, 7, 7, 5, 3, 9]]
interaction_term_test_2.fit(interaction_term_test_2_data)
print(interaction_term_test_2.coefficients)


