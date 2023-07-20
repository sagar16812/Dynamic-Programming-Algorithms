'''
The Bellman-Ford algorithm is used to find the shortest paths from a source 
vertex to all other vertices in a weighted directed graph, even in the 
presence of negative weight edges (as long as there are no negative weight 
cycles reachable from the source vertex). 


In this implementation, we define a Graph class that represents the directed 
graph. The add_edge() method is used to add edges to the graph.

The bellman_ford() method implements the Bellman-Ford algorithm. It initializes 
the distances array with infinity for all vertices except the source vertex, 
which is set to 0. Then, it iterates V-1 times (V is the number of vertices) 
and relaxes all the edges. If a shorter path is found, the distance is updated.

After the V-1 iterations, it checks for negative-weight cycles. If a shorter 
path is still found, it means the graph contains a negative-weight cycle.

After finding the shortest distances using the Bellman-Ford algorithm, we plot 
the graph using networkx and matplotlib. The graph is visualized with nodes, 
edges, edge weights, and labels.

The nx.draw() function is used to draw the graph, and nx.draw_networkx_edge_labels() 
is used to display the edge weights. Finally, plt.show() is called to display the graph.

Now, when you run the code, it will print the shortest distances from the source 
vertex and display the graph visualization.

In the example usage, a graph is created with 5 vertices and edges are added. 
The source vertex is set to 0, and the bellman_ford() method is called to find 
the shortest paths from the source vertex.
'''

import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, source):
        # Step 1: Initialize distances
        distances = [float('inf')] * self.V
        distances[source] = 0

        # Step 2: Relax all edges V-1 times
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

        # Step 3: Check for negative-weight cycles
        for u, v, w in self.graph:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                print("Graph contains negative-weight cycle")
                return

        # Step 4: Print shortest distances
        print("Vertex\tDistance from Source")
        for i in range(self.V):
            print(f"{i}\t{distances[i]}")

        # Plotting the graph
        G = nx.DiGraph()
        G.add_weighted_edges_from(self.graph)
        pos = nx.spring_layout(G)

        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12, edge_color='gray')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
        plt.title("Bellman-Ford Shortest Paths")
        plt.show()


# Example usage
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

source_vertex = 0
g.bellman_ford(source_vertex)

