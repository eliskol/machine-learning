import math
import numpy as np
import time

sigmoid = np.vectorize(lambda x: 1 / (1 + math.e ** -x))
sigmoid_prime = np.vectorize(lambda x: (
    math.e ** -x) / (1 + math.e ** -x) ** 2)


class NeuralNet:
    def __init__(self, A, b, datapoints, learning_rate):
        self.A = A
        self.b = b
        self.datapoints = datapoints
        self.learning_rate = learning_rate

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

    def sum_weight_gradients(self):
        self.dRSS_da = [np.zeros(matrix.shape) for matrix in self.A]
        self.dRSS_db = [np.zeros(matrix.shape) for matrix in self.b]
        for [x, y] in self.datapoints:
            Sigma, h = self.propagate_forward(self.A, self.b, x, y)
            dRSS_dh = self.propagate_backward(self.A, self.b, x, y, Sigma, h)
            dRSS_db, dRSS_da = self.expand_neuron_gradients_to_weight_gradients(dRSS_dh, Sigma, h)
            for l in range(len(self.dRSS_da)):
                self.dRSS_da[l] += dRSS_da[l]
                self.dRSS_db[l] += dRSS_db[l]

    def descend_gradient_to_new_weights(self):
        for l in range(len(self.A)):
            self.A[l] = self.A[l] - self.learning_rate * self.dRSS_da[l]
            self.b[l] = self.b[l] - self.learning_rate * self.dRSS_db[l]

    def train(self, iterations):
        beginning = time.time()
        data = [beginning, 0]
        for i in range(iterations):
            self.sum_weight_gradients()
            self.descend_gradient_to_new_weights()
            if time.time() - data[0] > 1:
                print(i, 'completed;', (i - data[1]) / (time.time() - data[0]), 'per second in roughly last second;', (i + 1) / (time.time() - beginning), 'iter/s overall')
                data = [time.time(), i]
            # print('predictions:')
            # for point in self.datapoints:
            #     print(np.matrix.round(self.propagate_forward(self.A, self.b, point[0], point[1])[1][-1], decimals=3))
            # print()
        print('training completed!')

    def predict(self, x):
        return self.propagate_forward(self.A, self.b, x, None)[1][-1]


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
bruh.train(100000)

for datapoint in datapoints:
    print(np.matrix.round(bruh.predict(datapoint[0]), decimals=3))