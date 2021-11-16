import sys
sys.path.insert(1, '/home/elias/Coding-Projects/Eurisko/machine-learning/src/')


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
interaction_term_test_2_data = [[0, 0, 0, 1], [1, 0, 5, 2], [2, 0, 1, 4], [4, 0, 0, 8], [6, 0, 0, 9], [0, 2, 0, 2], [0, 4, 0, 5], [0, 6, 0, 7], [0, 8, 0, 6], [2, 2, 0, 1], [3, 4, 0, 1], [5, 0, 1, 9], [5, 0, 5 ,3], [0, 3, 3, 1], [3, 3, 3, 1]]
interaction_term_test_2.fit(interaction_term_test_2_data, [(1, 2), (2, 3)])
# print(interaction_term_test_2.predict([5, 0, 2]))

for i in range(0, len(interaction_term_test_2_data)):
    interaction_term_test_2_data[i].insert(-1, interaction_term_test_2_data[i][0] * interaction_term_test_2_data[i][1])
    interaction_term_test_2_data[i].insert(-1, interaction_term_test_2_data[i][2] * interaction_term_test_2_data[i][1])

check = LinearRegressor()
check.fit(interaction_term_test_2_data)
assert check.predict([5, 0, 2, 0, 0]) ==  interaction_term_test_2.predict([5, 0, 2])