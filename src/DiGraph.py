from GraphInterface import GraphInterface
from Node import Node
import matplotlib.pyplot as plt
import numpy as np

class DiGraph(GraphInterface):
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.mc = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.nodes)

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].In

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].out

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.nodes and id2 in self.nodes:
            self.edges[(id1, id2)] = weight
            self.nodes[id1].out[id2] = weight
            self.nodes[id2].In[id1] = weight
            self.mc += 1
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        self.nodes[node_id] = Node(node_id, pos)
        self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes:

            for d in self.nodes[node_id].out:
                self.edges.pop(node_id, d)
                self.nodes[d].In.pop(node_id)

            for s in self.nodes[node_id].In:
                self.edges.pop(s, node_id)
                self.nodes[s].out.pop(node_id)

            self.nodes.pop(node_id)
            self.mc += 1
            return True

        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.nodes and node_id2 in self.nodes:
            self.edges.pop(node_id1,node_id2)
            self.nodes[node_id1].out.pop(node_id2)
            self.nodes[node_id2].In.pop(node_id1)
            self.mc += 1
            return True
        return False

    def __repr__(self) -> str:
        return f'{self.nodes} ' f'{self.edges}'


def draw_plot(g: DiGraph):
    # Xs = [float(p[0] for p in g)]
    # Ys = [float(p[1] for p in g)]
    #
    # for src in range(len(g) - 1):
    #     dx = Xs[src + 1] - Xs[src]
    #     dy = Ys[src + 1] - Ys[src]
    #     plt.arrow(Xs[src], Ys[src], dx, dy, width=1, length_includes_head=True)
    #     plt.text(Xs[src], Ys[src], str(src.key))
    # plt.plot(Xs, Ys, '^-')
    # plt.show()

    for src in g.nodes.values():
        x, y = float(src.pos[0]),float(src.pos[1])
        plt.plot(x, y, markersize=10, marker="o", color="black")
        plt.text(x, y, str(src.key), color="blue", fontsize=12)
    plt.show()
    # for v in g.nodes.values():
    #     x, y = v.pos['x'], v.pos['y']
    #     print(x, y)
    #     plt.plot(x, y, markersize=4, marker='o', color='blue')
    #     plt.text(x, y, str(v.id), color="red", fontsize=12)
    #     for nai, w in g.edges[v.id].items():
    #         u = g.nodes[nai]
    #         x_, y_ = u.pos['x'], u.pos['y']
    #         plt.annotate("", xy=(x, y), xytext=(x_, y_), arrowprops=dict(arrowstyle="<-"))
    #
    # plt.show()


