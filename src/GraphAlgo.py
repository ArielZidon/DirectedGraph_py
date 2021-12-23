from typing import List

from Node import Node
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from src import GraphInterface
import json
import copy


class GraphAlgo(GraphAlgoInterface):

    def __init__(self,graph=DiGraph()) -> None:
        self.graph = graph
        self.dijkstra = dijkstra(graph)
        self.inf = float('inf')

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

########################################################################################################################
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        self.getdijk(id1)
        self.dijkstra.addPath(id2)
        start = self.dijkstra.D[id2]
        end = self.dijkstra.roads[id2]
        return (start,end)


    def TSP(self, node_lst: List[int]) -> (List[int], float):
        try:
            chosen,road = self.inf,[]
            for i in node_lst:
                self.getdijk(i)
                path = []
                new = self.check_greedy(i,copy.deepcopy(node_lst), path)
                if new < chosen:
                    chosen,road = new,path
                else:
                    continue
            return (road,chosen)
        except:
            return ([],self.inf)


    def check_greedy(self, i: int, c: list, ins: list):
        ins.append(i)
        c.remove(i)
        index = None
        sum = 0
        while len(c):
            low = float('inf')
            for j in c:
                if self.dijkstra.D[j]< low:
                    low = self.dijkstra.D[j]
                    index = j

            sum += low
            f = True
            path = self.shortest_path(i,index)[1]
            for j in path:
                if f:
                    f = False
                    continue
                else:
                    ins.append(j)
            i = index
            self.getdijk(i)
            c.remove(index)
        return sum



    def centerPoint(self) -> (int, float):
        try:
            res = (0, self.inf)
            for i in self.graph.nodes:
                self.getdijk(i)
                rD = (i, max(self.dijkstra.D.values()))
                if res[1] > rD[1]:
                    res = rD
            return res
        except:
            return (0,self.inf)


    def plot_graph(self) -> None:
        pass


    def __repr__(self) -> str:
        return f'{self.graph}'


    def getdijk(self, src: int) -> bool:
        if src == self.dijkstra.src and self.graph.mc == self.dijkstra.mc:
            return False
        else:
            self.dijkstra.src = src
            self.dijkstra.MC = self.graph.mc
            self.dijkstra.goForIt()
            return True


class dijkstra:

    def __init__(self,graph:GraphInterface):
        self.src = 0
        self.graph = graph
        self.mc = 0
        self.inf = float('inf')

    #hashmaps
        self.roads = {}
        self.paps = {}
        self.D = {}

    def initshate(self,fathers: dict, listPerNode: list) -> None:
        for node in self.graph.nodes.keys():
            if node != self.src:
                self.D[node] = self.inf
                fathers[node] = self.inf
                listPerNode.append(node)
                self.roads[node] = []
        fathers[self.src] = self.src
        self.D[self.src] = 0.0
        self.roads[self.src] = []
        listPerNode.append(self.src)

    def theSmallest(self, Q: list) -> int:
        min2 = self.inf
        ans = -self.inf
        for node in Q:
            if min2 > self.D[node]:
                ans = node
                min2 = self.D[node]
        if ans != -self.inf:
            Q.remove(ans)
        return ans

    def updating(self, src: int, dest: int) -> None:
        updatedDistance = self.D[src] + self.graph.edges[(src, dest)]
        if updatedDistance >= self.D[dest]:
            return
        else:
            self.D[dest] = updatedDistance
            self.paps[dest] = src


    def goForIt(self):
        var = []
        self.initshate(self.paps, var)
        while len(var) != 0:
            small = self.theSmallest(var)
            if small == -self.inf:
                return
            for i in self.graph.all_out_edges_of_node(small):
                self.updating(small,i)


    def addPath(self, next: int) -> None:
        if len(self.roads[next]) != 0:
            return
        self.roads[next] = []
        if next == self.src:
            self.roads[next].append(next)
            return
        dad = self.paps[next]
        if dad == self.inf:
            return
        if dad in self.roads:
            self.addPath(dad)
        self.roads[next].extend(self.roads[dad])
        self.roads[next].append(next)








