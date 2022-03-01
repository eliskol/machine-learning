from math import log
import sys

sys.path.insert(1, sys.path[0].replace('tests', 'src'))

from gen_logistic_regression import LogisticRegressor

logistic_regressor = LogisticRegressor()
test_data = [[0, 0, 1], [2, 2, 1], [6, 0, 9], [0, 6, 7]]

logistic_regressor.fit(test_data, [(1, 2)], 0, 10)
coefficients = logistic_regressor.coefficients

assert round(coefficients[0], 3) == 2.197 and round(coefficients[1], 3) == -0.732 and round(coefficients[2], 3) == -0.507 and round(coefficients[(1, 2)], 3) == 0.620
assert logistic_regressor.predict((5, 5)) < 1
assert logistic_regressor.predict((0, 6)) == 7.0

test_data = [[0, 3, 3, 6], [3, 3, 0, 7], [3, 0, 0, 8], [0, 4, 0, 8], [3, 3, 2, 2]]
logistic_regressor.fit(test_data, [(0, 1, 2)], 0, 10)
coefficients = logistic_regressor.coefficients

assert coefficients == {(0, 1, 2): -0.024744560214742167, 0: -4.183499420135149, 1: 0.9324016863384199, 2: 0.699301264753815, 3: 0.5600435059218473}
assert round(logistic_regressor.predict((3, 0, 0)), 3) == 8