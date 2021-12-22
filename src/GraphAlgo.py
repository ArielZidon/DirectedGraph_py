from typing import List
from Node import Node
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from src import GraphInterface
import matplotlib.pyplot as plt
import numpy as np
import json

class GraphAlgo(GraphAlgoInterface):
    def __init__(self,graph=DiGraph()) -> None:
        self.graph = graph
        self.dijkstra = dijkstra

    def dijkstraAlgo(self, src: int) -> bool:
        if src == self.dijkstra.src and self.graph.mc == self.dijkstra.MC:
            return False
        else:
            self.dijkstra.src = src
            self.dijkstra.MC = self.graph.mc
            self.dijkstra.goForIt()
            return True

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            dict={}
            graph_res = self.graph
            with open(file_name,"r") as f:
                dict=json.load(f)

            for n in dict["Nodes"]:
                if "pos" in n:
                    data = n["pos"].split(',')
                    graph_res.add_node(n["id"],(data[0],data[1],data[2]))
                else:
                    graph_res.add_node(n["id"])

            for e in dict["Edges"]:
                graph_res.add_edge(e["src"],e["dest"],e["w"])

        except IOError as e:
            print(e)
            return False
        self.graph = graph_res
        return True



    def save_to_json(self, file_name: str) -> bool:
        graph_dict = {"Edges": [], "Nodes": []}
        for e in self.graph.edges:
            graph_dict["Edges"].append(
                {"src": e[0],"w": self.graph.edges[e],"dest": e[1]})
        for n in self.graph.nodes.values():
            id = n.key
            if(n.pos!=None):
                pos = f'{n.pos[0]},{n.pos[1]},{n.pos[2]}'
                graph_dict["Nodes"].append({"pos": pos, "id": id})
            else:
                graph_dict["Nodes"].append({"pos": None, "id": id})
        try:
            with open(file_name,"w") as f:
                json.dump(graph_dict, fp=f, indent=2, default=lambda o:o.__dict__)
        except IOError as e:
            print(e)
            return False
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        self.dijkstra(id1,id2)
        self.dijkstra.addPath(id2)
        return self.dijkstra.r

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        super().centerPoint()

    def plot_graph(self) -> None:
        pass

    def __repr__(self) -> str:
        return f'{self.graph}'


    def draw_plot(self):
        for node in self.graph.nodes.values():
            x = float(node.pos[0])
            y = float(node.pos[1])
            id = int(node.key)
            plt.plot(x, y, markersize=10, marker="o", color="pink")
            for edge in self.graph.all_out_edges_of_node(id):
                his_x = float(self.graph.nodes[edge].pos[0])
                his_y = float(self.graph.nodes[edge].pos[1])
                plt.annotate("", xy=(x, y), xytext=(his_x, his_y), arrowprops=dict(arrowstyle="<-"))
        plt.show()


class dijkstra:
    def __init__(self,src:int,graph:GraphInterface):
        self.src = src
        self.graph = graph
        self.mc = 0

    #hashmaps
        self.roads = {}
        self.paps = {}
        self.D = {}

    def initshate(self,fathers: dict, listPerNode: list) -> None:
        for node in self.graph.nodes.keys():
            if node != self.src:
                self.D[node] = float('inf')
                fathers[node] = float('inf')
                listPerNode.append(node)
                self.roads[node] = []
        fathers[self.src] = self.src
        self.D[self.src] = 0.0
        self.roads[self.src] = []
        listPerNode.append(self.src)

    def theSmallest(self, Q: list) -> int:
        min2 = float('inf')
        ans = float('-inf')
        for node in Q:
            if min2 > self.D[node]:
                ans = node
                min2 = self.D[node]
        if ans != float('-inf'):
            Q.remove(ans)
        return ans

    def updating(self, src: int, dest: int) -> None:
        newDist = self.D[src] + self.graph.edges[(src, dest)]
        if newDist < self.D[dest]:
            self.D[dest] = newDist
            self.paps[dest] = src

    def goForIt(self):
        Q = []
        self.initshate(self.paps, Q)
        while len(Q) != 0:
            u = self.theSmallest(Q)
            if u == float('-inf'):
                return
            for dest in self.graph.all_out_edges_of_node(u).keys():
                self.updating(u, dest)

    def addPath(self, dest: int) -> None:
        if len(self.roads[dest]) != 0:
            return
        self.roads[dest] = []
        if dest == self.src:
            self.roads[dest].append(dest)
            return
        dad = self.paps[dest]
        if dad == float('inf'):
            return
        if dad in self.roads:
            self.addPath(dad)
        self.roads[dest].extend(self.roads[dad])
        self.roads[dest].append(dest)





