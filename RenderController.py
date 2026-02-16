import networkx as nx
import matplotlib.pyplot as plt

class RenderController():
    def con_matrix_to_edges_and_color_map(self, cm, labels, sia):
        edges = []
        edge_color_map = []

        cut_from_nodes = []
        cut_to_nodes = []

        if getattr(sia.cut, 'is_null', False):
            cut_from_nodes = set()
            cut_to_nodes = set()
        else:
            cut_from_nodes = set(sia.cut.from_nodes) if hasattr(sia.cut, 'from_nodes') else set()
            cut_to_nodes = set(sia.cut.to_nodes) if hasattr(sia.cut, 'to_nodes') else set()

        for i in range(len(cm)):
            from_node = labels[i]
            for j in range(len(cm[i])):
                to_node = labels[j]

                if cm[i][j] != 0:
                    edges.append((from_node, to_node))

                    if i in cut_from_nodes and j in cut_to_nodes:
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

        self.plt = plt.figure(figsize=(10, 7))
        plt.ion()
        self.ax = plt.gca()

        self.ax.set_title(f'System Graph - Iteration 0')
        plt.text(-0.04, 1.09, f'Phi: {sia.phi} bits', color='tomato', transform=self.ax.transAxes, verticalalignment='top')
        plt.text(-0.04, 1.06, f'Major Complex: {sia.subsystem}', color='tomato', transform=self.ax.transAxes, verticalalignment='top')
        plt.text(-0.04, 1.03, f'MIP: {sia.cut}', color='orange', transform=self.ax.transAxes, verticalalignment='top')

        pos = nx.spring_layout(self.graph)

        nx.draw(self.graph, pos, ax=self.ax, with_labels=True, node_color=node_color_map, edgelist=edges, edge_color=edge_color_map, node_size=2000, font_weight='bold', arrows=True, arrowsize=20)
        self.plt.savefig(f'Data/Graphs/0.png')
        plt.pause(1)

    def render(self, network, sia, iteration):
        self.ax.clear()

        nodes = network.node_labels
        node_color_map = self.nodes_to_color_map(nodes, sia)
        edges, edge_color_map = self.con_matrix_to_edges_and_color_map(network.cm, nodes, sia)
        self.graph.add_nodes_from(nodes)
        self.graph.add_edges_from(edges)

        self.ax = plt.gca()

        self.ax.set_title(f'System Graph - Iteration {iteration}')
        plt.text(-0.04, 1.09, f'Phi: {sia.phi} bits', color='tomato', transform=self.ax.transAxes, verticalalignment='top')
        plt.text(-0.04, 1.06, f'Major Complex: {sia.subsystem}', color='tomato', transform=self.ax.transAxes,
                 verticalalignment='top')
        plt.text(-0.04, 1.03, f'MIP: {sia.cut}', color='orange', transform=self.ax.transAxes, verticalalignment='top')

        pos = nx.spring_layout(self.graph)

        nx.draw(self.graph, pos, ax=self.ax, with_labels=True, node_color=node_color_map, edgelist=edges, edge_color=edge_color_map,
                node_size=2000, font_weight='bold', arrows=True, arrowsize=20)

        self.plt.savefig(f'Data/Graphs/{iteration}.png')
        plt.pause(1)
