#  DirectedWeightedGraph
![graph](https://user-images.githubusercontent.com/93768578/147350320-173cb108-05a2-482e-9b2c-aa4e6bdebbc4.png)


In this project we will deal with directed graphs and all kinds of algorithms that can be run on them.
In the project we will examine the runtimes of the algorithms and see visually how they work.

#  Project departments
The project works so that when we run a graph from one of the json files the graph will be built in the program and then we can run the algorithms on it, add or remove nodes and edges from the graph or get information about nodes and edges in the graph.
The graph is divided into 2 main parts:

A. Graph construction.

B. Display the graph in a visual interface with *matplotlib*

#  Project idea
The idea of ​​the project is basically to create a directed graph as we wish and the possibility to look at the algorithms that can be run on directed graphs.

#  So how does the project actually work?
The project is divided into 2 parts the first is the creation of the graph itself and the second is a visual presentation of the graph.

#  Creating the graph
The graph is created and works according to the following slide:
#*ariel photo*

The graph is created by edgs and nodes as you can see in the slide and you can add or subtract sides and vertices and run new graphs as you wish.

#  classes

*DiGraph* - The class contains lists of nodes and edges and in addition is responsible for their creation and the structure of the graph.

*GraphAlgo* - his class get DiGraph and can calculate the next list of algorithms: If the graph is connected. A shorted path between 2 nodes. The ideal center of the graph. Tsp problem for a group of verticals in the graph

*Node* - The class contains פarameters of nodes and lists of edges that go out and enter the nodes.

#  DirectedWeightedGraphAlgorithm
The algorithm class is a class where certain algorithms can be run on the graph.
We will now explain each of the existing functions in the class:

*isConnected* - Finds whether the graph is a link or not. (Is it possible to reach from any node to any other node)

*shortestPath* - Finds the shortest path in the graph between any 2 nodes we want. (Receives source node and destination node)

*center* - Finds the node with the smallest trajectory value toward all other graphite nodes.

*dijkstra* - dijkstra algorithm. https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

*tsp* - will find the best way to do circle on group of nodes in the graph.

#  Matplotlib
The class receives the graph after the creation of all nodes and edges and the class creates a graphical interface on the screen:

*plot_graph* - (The function is inside the *GraphAlgo* class) The function takes the lists of the graph that show the position of the nodes and the eges that connect the nodes and draw it on the screen:

![graph](https://user-images.githubusercontent.com/93768578/147351645-8f2a5ebe-fa34-4a6f-b95d-792241c137db.png)


#  How to run the project
/////
