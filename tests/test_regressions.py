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
interaction_term_test_2_data = [[41, 41, 26, 3, 37, 37, 19, 11, 5, 50], [14, 19, 38, 16, 46, 38, 47, 50, 25, 6], [32, 23, 45, 29, 23, 2, 1, 10, 27, 31], [34, 46, 1, 27, 3, 6, 31, 4, 20, 11], [12, 4, 2, 12, 35, 33, 28, 11, 46, 20], [23, 29, 35, 6, 38, 17, 33, 50, 42, 31], [42, 4, 46, 22, 50, 10, 37, 14, 34, 16], [8, 48, 50, 8, 31, 6, 45, 19, 40, 23], [8, 1, 44, 27, 47, 5, 8, 17, 46, 2], [42, 24, 8, 26, 34, 46, 14, 46, 47, 6]]
interaction_term_test_2.fit(interaction_term_test_2_data, [(1, 6)])
print(interaction_term_test_2.coefficients)

# for row in interaction_term_test_2_data:

#test