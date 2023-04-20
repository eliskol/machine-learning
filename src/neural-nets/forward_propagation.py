import math
import numpy as np


A_1 = np.matrix([[5], [-5], [5], [-5]])
A_2 = np.matrix([[10, 10, 0, 0], [0, 0, 10, 10]])
A_3 = np.matrix([10, 10])

A = [A_1, A_2, A_3]

b_1 = np.matrix([[-0.75], [1.75], [-3.25], [4.25]])
b_2 = np.matrix([[-12.5], [-12.5]])
b_3 = np.matrix([-2.5])

b = [b_1, b_2, b_3]

x = np.matrix(0)
y = 0

sigmoid = np.vectorize(lambda x: 1 / (1 + math.e ** -x))
sigmoid_prime = np.vectorize(lambda x: (math.e ** -x) / (1 + math.e ** -x) ** 2)


def propagate_forward(A, b, x, y):
    Sigma = [None]
    h = [x]
    for i in range(len(A)):
        Sigma.append(A[i] * h[i] + b[i])
        h.append(sigmoid(Sigma[i + 1]))
    return Sigma, h


def propagate_backward(A: list[np.matrix], b, x, y, Sigma: list[np.matrix], h: list[np.matrix]):
    dRSS_arr = []
    dRSS_arr.append(2 * (h[-1] - y))
    for l, A_l in enumerate(reversed(A[1:])):
        dRSS_arr.append(A_l.transpose() * (np.multiply(dRSS_arr[-1], sigmoid_prime(Sigma[-l - 1]))))
    return dRSS_arr[::-1]


Sigma, h = propagate_forward(A, b, x, y)
dRSS_arr = propagate_backward(A, b, x, y, Sigma, h)
for matrix in dRSS_arr:
    print(matrix)
    print()