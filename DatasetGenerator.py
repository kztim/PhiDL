import random
import time
from itertools import product

import numpy as np
import pyphi


class DatasetGenerator:

    def __init__(self):
        np.random.seed(67)

        self.network, self.state, self.weight_gen = self.generate_network_and_state()

    def generate_network_and_state(self):
        np.random.seed(int(time.time()))
        num_nodes = random.randint(3, 3)

        weight_gen, tpm_gen = self.tpm_from_weight_gen(num_nodes)
        state_gen = np.random.randint(0, 2, num_nodes)
        label_gen = [chr(65 + i) for i in range(num_nodes)]

        cm_gen = []
        for col in weight_gen:
            node_connections = []

            for node in col:

                if node != 0:
                    node_connections.append(1)
                else:
                    node_connections.append(0)

            cm_gen.append(node_connections)

        network = pyphi.Network(tpm_gen, cm=cm_gen, node_labels=label_gen)

        return network, state_gen, weight_gen

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def tpm_from_weight_gen(self, num_nodes):
        weight_gen = np.random.randn(num_nodes, num_nodes)

        weighted_weights = []
        for col in weight_gen:
            node_connections = []

            for node in col:

                if np.abs(node) > 0.25:
                    node_connections.append(node)
                else:
                    node_connections.append(0)

            weighted_weights.append(node_connections)

        weight_gen = weighted_weights

        bias_gen = np.random.randn(num_nodes)
        all_possible_states = np.array(list(product([0, 1], repeat=num_nodes)))

        logits = (np.matmul(all_possible_states, weight_gen) + bias_gen)

        tpm_gen = self.sigmoid(logits)

        print(tpm_gen)
        return weight_gen, tpm_gen