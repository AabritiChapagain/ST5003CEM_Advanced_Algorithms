def is_safe(v, graph, path, pos):
    """
    Check whether the vertex can be added to the Hamiltonian Cycle.
    """

    # Must be adjacent to previous vertex
    if graph[path[pos - 1]][v] == 0:
        return False

    # Cannot already be in the path
    if v in path:
        return False

    return True


def hamiltonian_util(graph, path, pos):
    n = len(graph)

    # All vertices included
    if pos == n:
        return graph[path[pos - 1]][path[0]] == 1

    for v in range(1, n):

        if is_safe(v, graph, path, pos):

            path[pos] = v

            if hamiltonian_util(graph, path, pos + 1):
                return True

            # Backtrack
            path[pos] = -1

    return False


def hamiltonian_cycle(graph):

    n = len(graph)

    path = [-1] * n
    path[0] = 0

    if not hamiltonian_util(graph, path, 1):
        print("No Hamiltonian Cycle exists.")
        return False

    print("Hamiltonian Cycle:")

    for vertex in path:
        print(vertex, end=" -> ")

    print(path[0])

    return True


if __name__ == "__main__":

    graph = [

        [0,1,1,0,1],

        [1,0,1,1,0],

        [1,1,0,1,1],

        [0,1,1,0,1],

        [1,0,1,1,0]

    ]

    hamiltonian_cycle(graph)