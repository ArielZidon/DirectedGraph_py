from typing import List
from Node import Node
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from src import GraphInterface
import json

class GraphAlgo(GraphAlgoInterface):
    def __init__(self,graph=DiGraph()) -> None:
        self.graph = graph

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
                    graph_res.add_node(n["id"], pos=(n["pos"][0], n["pos"][1], n["pos"][2]))
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
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        super().centerPoint()

    def plot_graph(self) -> None:
        pass

    def __repr__(self) -> str:
        return f'{self.graph}'
