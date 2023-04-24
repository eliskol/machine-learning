import math
import numpy as np

sigmoid = np.vectorize(lambda x: 1 / (1 + math.e ** -x))
sigmoid_prime = np.vectorize(lambda x: (
    math.e ** -x) / (1 + math.e ** -x) ** 2)


class NeuralNet:
    def __init__(self, A, b, datapoints, learning_rate):
        self.A = A
        self.b = b
        self.datapoints = datapoints
        self.learning_rate = learning_rate
        self.dRSS_da = [np.zeros(matrix.shape) for matrix in self.A]
        self.dRSS_db = [np.zeros(matrix.shape) for matrix in self.b]
        for [x, y] in datapoints:
            self.Sigma, self.h = self.propagate_forward(self.A, self.b, x, y)
            self.dRSS_dh = self.propagate_backward(self.A, self.b, x, y, self.Sigma, self.h)
            dRSS_da, dRSS_db = self.expand_neuron_gradients_to_weight_gradients(self.dRSS_dh, self.Sigma, self.h)
            for l in range(len(self.dRSS_da)):
                self.dRSS_da[l] += dRSS_da[l]
                self.dRSS_db[l] += dRSS_db[l]

    def propagate_forward(self, A, b, x, y):
        Sigma = [None]
        h = [x]
        for i in range(len(A)):
            Sigma.append(A[i] * h[i] + b[i])
            h.append(sigmoid(Sigma[i + 1]))
        return Sigma, h

    def propagate_backward(self, A: list[np.matrix], b, x, y, Sigma: list[np.matrix], h: list[np.matrix]):
        dRSS_dh = []
        dRSS_dh.append(2 * (h[-1] - y))
        for l, A_l in enumerate(reversed(A[1:])):
            dRSS_dh.append(A_l.transpose() *
                        (np.multiply(dRSS_dh[-1], sigmoid_prime(Sigma[-l - 1]))))
        return dRSS_dh[::-1]

    def expand_neuron_gradients_to_weight_gradients(self, dRSS_dh, Sigma, h):
        dRSS_db = []
        for l in range(0, len(h) - 1):
            dRSS_db.append(np.multiply(dRSS_dh[l], sigmoid_prime(Sigma[l + 1])))
        dRSS_da = []
        for l in range(0, len(h) - 1):
            dRSS_da.append(np.matrix(np.outer(dRSS_db[l], h[l])))
        return dRSS_db, dRSS_da

    # def descend_gradient_to_new_weights:
    #     for l, weight_matrix in enumerate(self.A):
    #         weight_matrix -= self.dRSS

A_1 = np.matrix([[5], [-5], [5], [-5]])
A_2 = np.matrix([[10, 10, 0, 0], [0, 0, 10, 10]])
A_3 = np.matrix([10, 10])

A = [A_1, A_2, A_3]

b_1 = np.matrix([[-0.75], [1.75], [-3.25], [4.25]])
b_2 = np.matrix([[-12.5], [-12.5]])
b_3 = np.matrix([-2.5])

b = [b_1, b_2, b_3]

datapoints = [[np.matrix(0), 0], [np.matrix(0.25), 1], [np.matrix(0.5), 0.5], [np.matrix(0.75), 1], [np.matrix(1), 0]]

learning_rate = 0.01

bruh = NeuralNet(A, b, datapoints, learning_rate)
print(bruh.dRSS_da)