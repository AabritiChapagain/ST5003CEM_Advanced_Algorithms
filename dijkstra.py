import heapq


def dijkstra(graph, start):
    """
    Finds the shortest path from the starting city to all other cities.
    """

    # Initialize distances
    distances = {city: float("inf") for city in graph.graph}
    distances[start] = 0

    # Priority queue (distance, city)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_city = heapq.heappop(priority_queue)

        # Skip if a shorter path is already known
        if current_distance > distances[current_city]:
            continue

        # Check neighboring cities
        for neighbor, weight in graph.graph[current_city]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances