def bellman_ford(graph, start):
    """
    Bellman-Ford algorithm to find shortest paths.
    Detects negative-weight cycles.
    """

    distances = {city: float("inf") for city in graph.graph}
    distances[start] = 0

    vertices = list(graph.graph.keys())

    # Relax all edges |V|-1 times
    for _ in range(len(vertices) - 1):
        for source in graph.graph:
            for destination, weight in graph.graph[source]:
                if (
                    distances[source] != float("inf")
                    and distances[source] + weight < distances[destination]
                ):
                    distances[destination] = (
                        distances[source] + weight
                    )

    # Check for negative cycles
    for source in graph.graph:
        for destination, weight in graph.graph[source]:
            if (
                distances[source] != float("inf")
                and distances[source] + weight < distances[destination]
            ):
                print("Negative weight cycle detected!")
                return None

    return distances