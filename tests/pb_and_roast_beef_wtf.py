import sys
sys.path[0] = "/workspace/machine-learning/src/"
from linear_regression import LinearRegressor
pain = [[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [6, 0, 9], [0, 2, 2], [0, 4, 5], [0, 6, 7], [0, 8, 6]]
bruh = LinearRegressor()
bruh.fit(pain)
print(bruh.coefficients)
stuff = open("pb_and_roast_beef_predictions.txt", "w")
stuff.write("5 rb and 5 pb: " + str(bruh.predict([5, 5])) + "\n")
stuff.write("5 rb and 0 pb: " + str(bruh.predict([5, 0])))