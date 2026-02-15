import networkx as nx
import matplotlib.pyplot as plt

class RenderController():
    def con_matrix_to_edges(self, cm, labels):
        edges = []

        for i in range(len(cm)):
            from_node = labels[i]

            for j in range(len(cm[i])):
                to_node = labels[j]

                if cm[i][j] == 1:
                    edges.append((from_node, to_node))

        return edges

    def __init__(self, network, sia):
        self.graph = nx.DiGraph()

        nodes = network.node_labels
        edges = self.con_matrix_to_edges(network.cm, nodes)
        self.graph.add_nodes_from(nodes)
        self.graph.add_edges_from(edges)

        plt.figure(figsize=(8, 6))
        ax = plt.gca()

        ax.set_title('System Graph')
        plt.text(0.02, 0.98, f'Phi: {sia.phi} bits', transform=ax.transAxes, verticalalignment='top')
        plt.text(0.02, 0.95, f'Major Complex: {sia.subsystem}', transform=ax.transAxes, verticalalignment='top')


        pos = nx.spring_layout(self.graph)

        nx.draw(self.graph, pos, ax=ax, with_labels=True, node_color='lightblue', node_size=2000, font_weight='bold', arrows=True)
        plt.show()