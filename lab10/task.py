from graph_representation import AdjacencyListGraph
from graph_traversal import bfs

def is_connected(graph):
    visited = bfs(graph, 0)
    return len(visited) == graph.n


if __name__ == "__main__":
    g = AdjacencyListGraph(5)

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    print("Граф связен?" , is_connected(g))
