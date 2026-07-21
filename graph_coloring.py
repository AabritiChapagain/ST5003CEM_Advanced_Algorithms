class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1


def greedy_coloring(graph):
    """
    Greedy heuristic for graph coloring.
    """

    result = [-1] * graph.V
    result[0] = 0

    available = [True] * graph.V

    for u in range(1, graph.V):

        for v in range(graph.V):
            if graph.graph[u][v] == 1 and result[v] != -1:
                available[result[v]] = False

        color = 0
        while color < graph.V:
            if available[color]:
                break
            color += 1

        result[u] = color

        available = [True] * graph.V

    return result


def local_search(graph, coloring):
    """
    Simple local search heuristic.
    Attempts to reduce the highest color number used.
    """

    improved = coloring[:]

    for vertex in range(graph.V):

        used = set()

        for neighbor in range(graph.V):
            if graph.graph[vertex][neighbor]:
                used.add(improved[neighbor])

        for color in range(max(improved)):
            if color not in used:
                improved[vertex] = color
                break

    return improved


if __name__ == "__main__":

    g = Graph(5)

    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(2,4)
    g.add_edge(3,4)

    greedy = greedy_coloring(g)

    print("Greedy Coloring")
    print(greedy)

    improved = local_search(g, greedy)

    print("\nLocal Search Coloring")
    print(improved)