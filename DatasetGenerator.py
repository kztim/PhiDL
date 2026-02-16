import random
from itertools import product

import numpy as np
import pyphi


class DatasetGenerator:

    def __init__(self):
        np.random.seed(67)

        self.network, self.state = self.generate_network_and_state()

    def generate_network_and_state(self):
        num_nodes = random.randint(4, 6)

        tpm_gen = self.tpm_from_weight_gen(num_nodes)
        cm_gen = np.random.randint(0, 2, (num_nodes, num_nodes))
        state_gen = np.random.randint(0, 2, num_nodes)
        label_gen = [chr(65 + i) for i in range(num_nodes)]

        network = pyphi.Network(tpm_gen, cm=cm_gen, node_labels=label_gen)

        return network, state_gen

    def tpm_from_weight_gen(self, num_nodes):
        weight_gen = np.random.randn(num_nodes, num_nodes)
        bias_gen = np.random.randn(num_nodes)

        all_possible_states = list(product([0, 1], repeat=num_nodes))