class Graph:
    """
    Weighted Directed Graph using an Adjacency List.
    """

    def __init__(self):
        self.graph = {}

    def add_city(self, city):
        """Add a city (vertex) to the graph."""
        if city not in self.graph:
            self.graph[city] = []

    def add_road(self, source, destination, distance):
        """
        Add a directed road (edge) with a weight.
        """
        self.add_city(source)
        self.add_city(destination)

        self.graph[source].append((destination, distance))

    def display(self):
        """Display the graph."""
        for city in self.graph:
            print(f"{city} -> {self.graph[city]}")