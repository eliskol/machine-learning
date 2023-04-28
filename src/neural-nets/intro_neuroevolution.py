from neural_net import *
import pandas as pd
import numpy as np
import math
import time
from numpy.random import normal as N

rng = np.random.default_rng()

tanh = np.vectorize(lambda x: (math.e ** x - math.e ** -
                    x) / (math.e ** x + math.e ** -x))
tanh_prime = np.vectorize(lambda x: 4 / ((math.e ** x + math.e ** -x) ** 2))

datapoints = [
    (0.0, 1.0), (0.04, 0.81), (0.08, 0.52), (0.12, 0.2), (0.17, -0.12),
    (0.21, -0.38), (0.25, -0.54), (0.29, -0.58), (0.33, -0.51), (0.38, -0.34),
    (0.42, -0.1), (0.46, 0.16), (0.5, 0.39), (0.54, 0.55), (0.58, 0.61),
    (0.62, 0.55), (0.67, 0.38), (0.71, 0.12), (0.75, -0.19), (0.79, -0.51),
    (0.83, -0.77), (0.88, -0.95), (0.92, -1.0), (0.96, -0.91), (1.0, -0.7)
]

A_weight_matrix_shapes = [(10, 1), (6, 10), (3, 6), (1, 3)]
b_weight_matrix_shapes = [(10, 1), (6, 1), (3, 1), (1, 1)]
activation_functions_and_derivatives = [[tanh, tanh_prime] for _ in range(4)]

neural_nets = []
for i in range(15):
    A = []
    b = []
    for shape in A_weight_matrix_shapes:
        A.append(np.matrix(rng.uniform(low=-0.2, high=0.2, size=shape)))
    for shape in b_weight_matrix_shapes:
        b.append(np.matrix(rng.uniform(low=-0.2, high=0.2, size=shape)))
    neural_nets.append(
        NeuralNet(A, b, activation_functions_and_derivatives, datapoints, 0.01))
    neural_nets[-1].mutation_rate = 0.05

print(sum(neural_net.compute_RSS() for neural_net in neural_nets) / 15)


def replicate_and_create_child(neural_net):
    new_mutation_rate = neural_net.mutation_rate * \
        math.e ** (N(0, 1) /
                   ((2 * neural_net.number_of_weights ** 0.5) ** 0.5))
    new_A_weights = []
    new_b_weights = []
    for A_weights in neural_net.A:
        A_l_weights = np.zeros(shape=A_weights.shape)
        for i in range(A_weights.shape[0]):
            for j in range(A_weights.shape[1]):
                A_l_weights[i, j] = A_weights[i, j] + np.matrix(new_mutation_rate * N(0, 1))
        new_A_weights.append(A_l_weights)

    for b_weights in neural_net.b:
        b_l_weights = np.zeros(shape=b_weights.shape)
        for i in range(b_weights.shape[0]):
            for j in range(b_weights.shape[1]):
                b_l_weights[i, j] = b_weights[i, j] + np.matrix(new_mutation_rate * N(0, 1))
        new_b_weights.append(b_l_weights)

    child_neural_net = NeuralNet(
        new_A_weights, new_b_weights, activation_functions_and_derivatives, datapoints, 0.01)
    child_neural_net.mutation_rate = new_mutation_rate
    return child_neural_net


def next_generation(neural_nets):
    child_neural_nets = []
    for neural_net in neural_nets:
        child_neural_nets.append(replicate_and_create_child(neural_net))
    neural_nets += child_neural_nets
    for i in range(15):
        neural_net_RSS_list = [neural_net.compute_RSS()
                               for neural_net in neural_nets]
        assert neural_nets[neural_net_RSS_list.index(
            max(neural_net_RSS_list))].compute_RSS() == max(neural_net_RSS_list)
        del neural_nets[neural_net_RSS_list.index(max(neural_net_RSS_list))]
    return neural_nets


beginning = time.time()
data = [beginning, 0, sum(neural_net.compute_RSS()
        for neural_net in neural_nets) / 15]

for i in range(5000):
    prev_RSS = data[2]
    neural_nets = next_generation(neural_nets)
    # if (sum(neural_net.compute_RSS()
    #         for neural_net in neural_nets) / 15) - prev_RSS == 0:
    #     print('bruh')
    # if time.time() - data[0] > 5:
    #     print(i + 1, 'completed;', (i - data[1]) / (time.time() - data[0]),
    #           'per second in last interval;', (i + 1) / (time.time() - beginning), 'iter/s overall')
    data = [time.time(), i, sum(neural_net.compute_RSS()
                                for neural_net in neural_nets) / 15]
    print('avg RSS at generation', i + 1, sum(neural_net.compute_RSS()
          for neural_net in neural_nets) / 15, 'change in avg rss:', (sum(neural_net.compute_RSS()
                                                                          for neural_net in neural_nets) / 15) - prev_RSS)
    print('avg mutation rate', sum(
        neural_net.mutation_rate for neural_net in neural_nets) / 15)

print(sum(neural_net.compute_RSS() for neural_net in neural_nets) / 15)
