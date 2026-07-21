import heapq


def prim(graph, start):
    """
    Prim's Algorithm to find the Minimum Spanning Tree (MST).
    Returns the edges in the MST and the total weight.
    """

    visited = set()
    mst = []
    total_weight = 0

    priority_queue = [(0, start, None)]

    while priority_queue:
        weight, current, parent = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        if parent is not None:
            mst.append((parent, current, weight))
            total_weight += weight

        for neighbor, edge_weight in graph.graph[current]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (edge_weight, neighbor, current)
                )

    return mst, total_weight