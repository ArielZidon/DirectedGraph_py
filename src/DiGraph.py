from GraphInterface import GraphInterface
from Node import Node

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
        return self.nodes[id1].toMe

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].fromMe

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.nodes and id2 in self.nodes:
            self.edges[(id1,id2)] = weight
            self.nodes[id1].fromMe[id2] = weight
            self.nodes[id2].toMe[id1] = weight
            self.mc+=1
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False

        self.nodes[node_id] = Node(node_id,pos)
        self.mc+=1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes:

            for d in self.nodes[node_id].fromMe:
                self.edges.pop(node_id,d)
                self.nodes[d].toMe.pop(node_id)

            for s in self.nodes[node_id].toMe:
                self.edges.pop(s,node_id)
                self.nodes[s].fromMe.pop(node_id)

            self.nodes.pop(node_id)
            self.mc+=1
            return True
        else:
            return False














