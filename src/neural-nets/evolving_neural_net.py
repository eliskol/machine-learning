import math
import numpy as np
import pandas as pd
from neural_net import NeuralNet
from numpy.random import normal as N

rng = np.random.default_rng()


class EvolvingNeuralNet:
    def __init__(
        self,
        num_nodes_by_layer,
        num_nets,
        activation_functions_and_derivatives,
        datapoints,
        learning_rate,
        initial_mutation_rate,
    ):
        """structure of num_nodes_by_layer: list of number of nodes, each entry is num of non-bias nodes for that layer
        this will have 1 bias node on every layer"""
        self.num_nodes_by_layer = num_nodes_by_layer
        self.num_nets = num_nets
        self.A_weight_matrix_shapes = [
            (self.num_nodes_by_layer[i + 1], self.num_nodes_by_layer[i])
            for i in range(len(self.num_nodes_by_layer) - 1)
        ]
        self.b_weight_matrix_shapes = [
            (self.num_nodes_by_layer[i + 1], 1)
            for i in range(len(self.num_nodes_by_layer) - 1)
        ]
        self.activation_functions_and_derivatives = activation_functions_and_derivatives
        self.datapoints = datapoints
        self.learning_rate = learning_rate
        self.initial_mutation_rate = initial_mutation_rate

        self.neural_nets = []

        for i in range(num_nets):
            A = []
            b = []
            for shape in self.A_weight_matrix_shapes:
                A.append(np.matrix(rng.uniform(low=-0.2, high=0.2, size=shape)))
            for shape in self.b_weight_matrix_shapes:
                b.append(np.matrix(rng.uniform(low=-0.2, high=0.2, size=shape)))
            self.neural_nets.append(
                NeuralNet(
                    A,
                    b,
                    self.activation_functions_and_derivatives,
                    self.datapoints,
                    self.learning_rate,
                )
            )
            self.neural_nets[-1].mutation_rate = self.initial_mutation_rate

        self.average_RSS = self.compute_average_RSS()
        self.average_mutation_rate = self.compute_average_mutation_rate()

        self.set_log_data()

    def create_child_net(self, neural_net):
        new_mutation_rate = neural_net.mutation_rate * math.e ** (
            N(0, 1) / ((2 * neural_net.number_of_weights**0.5) ** 0.5)
        )
        new_A_weights = []
        new_b_weights = []
        for A_weights in neural_net.A:
            A_l_weights = np.zeros(shape=A_weights.shape)
            for i in range(A_weights.shape[0]):
                for j in range(A_weights.shape[1]):
                    A_l_weights[i, j] = A_weights[i, j] + np.matrix(
                        new_mutation_rate * N(0, 1)
                    )
            new_A_weights.append(A_l_weights)

        for b_weights in neural_net.b:
            b_l_weights = np.zeros(shape=b_weights.shape)
            for i in range(b_weights.shape[0]):
                for j in range(b_weights.shape[1]):
                    b_l_weights[i, j] = b_weights[i, j] + np.matrix(
                        new_mutation_rate * N(0, 1)
                    )
            new_b_weights.append(b_l_weights)

        child_neural_net = NeuralNet(
            new_A_weights,
            new_b_weights,
            self.activation_functions_and_derivatives,
            self.datapoints,
            0.01,
        )
        child_neural_net.mutation_rate = new_mutation_rate
        return child_neural_net

    def create_next_generation(self, log=False):
        child_neural_nets = []
        for neural_net in self.neural_nets:
            child_neural_nets.append(self.create_child_net(neural_net))
        self.neural_nets += child_neural_nets
        for i in range(self.num_nets):
            neural_net_RSS_list = [
                neural_net.compute_RSS() for neural_net in self.neural_nets
            ]
            assert self.neural_nets[
                neural_net_RSS_list.index(max(neural_net_RSS_list))
            ].compute_RSS() == max(neural_net_RSS_list)
            del self.neural_nets[neural_net_RSS_list.index(max(neural_net_RSS_list))]

        self.average_RSS = self.compute_average_RSS()
        self.average_mutation_rate = self.compute_average_mutation_rate()

        self.set_log_data()

        if log:
            print('Generation', len(self.log_data["Average RSS"]))

            print(
                "Avg. RSS:",
                self.log_data["Average RSS"][-1],
                "; avg. mutation rate:",
                self.log_data["Average mutation rate"][-1],
            )
            print(
                f"Change in avg. RSS:",
                self.log_data["Average RSS"][-1] - self.log_data["Average RSS"][-2],
            )
            print(
                f"Change in avg. mutation rate",
                self.log_data["Average mutation rate"][-1]
                - self.log_data["Average mutation rate"][-2],
            )

    def compute_average_RSS(self):
        return (
            sum(neural_net.compute_RSS() for neural_net in self.neural_nets)
            / self.num_nets
        )

    def compute_average_mutation_rate(self):
        return (
            sum(neural_net.mutation_rate for neural_net in self.neural_nets)
            / self.num_nets
        )

    def set_log_data(self):
        if hasattr(self, "log_data"):
            self.log_data["Average RSS"].append(self.average_RSS)
            self.log_data["Average mutation rate"].append(self.average_mutation_rate)
        else:
            self.log_data = {
                "Average RSS": [self.average_RSS],
                "Average mutation rate": [self.average_mutation_rate],
            }

    def plot(self):
        max_input = int(max(point[0] for point in self.datapoints))
        neural_net_df = pd.DataFrame(
            [
                [
                    x / (1000 * max_input),
                    *[
                        float(neural_net.predict(np.matrix(x / (1000 * max_input))))
                        for neural_net in self.neural_nets
                    ],
                ]
                for x in range(1000 * max_input)
            ]
        )
        datapoint_df = pd.DataFrame(self.datapoints)
        datapoint_plot = datapoint_df.plot(x=0, y=1, kind="scatter")
        for i in range(self.num_nets):
            datapoint_plot = neural_net_df.plot(ax=datapoint_plot, x=0, y=i + 1)
        return datapoint_plot

    def train(self, iterations=None, auto=True, threshold=0.15, log=False):
        if iterations is not None:
            for i in range(iterations):
                self.create_next_generation(log)
        elif auto:
            while self.average_RSS > threshold:
                self.create_next_generation(log)

    # todo: add logging (in progress)
    # todo: add save weights function (pickling)
    #    index weights by the datapoints & nn architecture?
    # todo: be able to configure distributions


datapoints = [
    (0.0, 1.0), (0.04, 0.81), (0.08, 0.52), (0.12, 0.2), (0.17, -0.12),
    (0.21, -0.38), (0.25, -0.54), (0.29, -0.58), (0.33, -0.51), (0.38, -0.34),
    (0.42, -0.1), (0.46, 0.16), (0.5, 0.39), (0.54, 0.55), (0.58, 0.61),
    (0.62, 0.55), (0.67, 0.38), (0.71, 0.12), (0.75, -0.19), (0.79, -0.51),
    (0.83, -0.77), (0.88, -0.95), (0.92, -1.0), (0.96, -0.91), (1.0, -0.7)
]

tanh = np.vectorize(lambda x: (math.e ** x - math.e ** -x) / (math.e ** x + math.e ** -x))
tanh_prime = np.vectorize(lambda x: 4 / ((math.e ** x + math.e ** -x) ** 2))

num_nodes_by_layer = [1, 3, 6, 6, 3, 1] # 3, 6, 3: 991 gens
num_nets = 10
activation_functions_and_derivatives = [[tanh, tanh_prime] for _ in range(len(num_nodes_by_layer) - 1)]

evolving_neural_net = EvolvingNeuralNet(num_nodes_by_layer, num_nets, activation_functions_and_derivatives, datapoints, 0.01, 0.5)
print(evolving_neural_net.average_RSS)
evolving_neural_net.train(log=True, threshold=0.5)
print(len(evolving_neural_net.log_data["Average RSS"]))

evolving_neural_net.plot().get_figure().savefig('./bruh.pdf')