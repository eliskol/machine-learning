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


def propagate_forward(A, b, x, y):
    Sigma = [None]
    h = [x]
    for i in range(len(A)):
        Sigma.append(A[i] * h[i] + b[i])
        h.append(sigmoid(Sigma[i + 1]))
    return h


print(propagate_forward(A, b, x, y)[-1])