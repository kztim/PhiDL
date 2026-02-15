import networkx as nx
import matplotlib.pyplot as plt

class RenderController():
    def con_matrix_to_edges_and_color_map(self, cm, labels, sia):
        edges = []
        edge_color_map = []

        for i in range(len(cm)):
            from_node = labels[i]

            for j in range(len(cm[i])):
                to_node = labels[j]

                if cm[i][j] != 0:
                    edges.append((from_node, to_node))

                    if i in sia.cut.from_nodes and j in sia.cut.to_nodes:
                        edge_color_map.append('tomato')
                    else:
                        edge_color_map.append('lightgrey')

        return edges, edge_color_map

    def nodes_to_color_map(self, nodes, sia):
        color_map = []

        for node in nodes:
            if sia.subsystem.node_labels.index(node) in sia.subsystem.node_indices:
                color_map.append('tomato')

            else:
                color_map.append('lightblue')
                print(node, sia.subsystem.node_indices)


        return color_map

    def __init__(self, network, sia):
        self.graph = nx.DiGraph()

        nodes = network.node_labels
        node_color_map = self.nodes_to_color_map(nodes, sia)
        edges, edge_color_map = self.con_matrix_to_edges_and_color_map(network.cm, nodes, sia)
        self.graph.add_nodes_from(nodes)
        self.graph.add_edges_from(edges)

        plt.figure(figsize=(10, 7))
        ax = plt.gca()

        ax.set_title('System Graph')
        plt.text(-0.04, 1.09, f'Phi: {sia.phi} bits', color='tomato', transform=ax.transAxes, verticalalignment='top')
        plt.text(-0.04, 1.06, f'Major Complex: {sia.subsystem}', color='tomato', transform=ax.transAxes, verticalalignment='top')
        plt.text(-0.04, 1.03, f'MIP: {sia.cut}', color='orange', transform=ax.transAxes, verticalalignment='top')

        pos = nx.spring_layout(self.graph)

        nx.draw(self.graph, pos, ax=ax, with_labels=True, node_color=node_color_map, edge_color=edge_color_map, node_size=2000, font_weight='bold', arrows=True)
        plt.show()