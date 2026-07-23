import random


class Graph:
    """
    Undirected graph represented as an adjacency matrix.
    """

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def neighbors(self, u):
        return [v for v in range(self.V) if self.graph[u][v] == 1]


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------

def count_conflicts(graph, coloring):
    """
    Count the number of edges whose two endpoints share the same colour.
    A proper colouring has zero conflicts.
    """
    conflicts = 0
    for u in range(graph.V):
        for v in graph.neighbors(u):
            if v > u and coloring[u] == coloring[v]:
                conflicts += 1
    return conflicts


def class_sizes(coloring, k):
    """Return the size of each of the k colour classes."""
    sizes = [0] * k
    for c in coloring:
        sizes[c] += 1
    return sizes


def imbalance(coloring, k):
    """
    Equitable colouring requires |class_i - class_j| <= 1 for all i, j.
    We measure how far the current colouring is from that with
    (max class size - min class size). A properly equitable colouring
    (that also uses all k colours) has imbalance 0 or 1.
    """
    sizes = class_sizes(coloring, k)
    return max(sizes) - min(sizes)


def objective(graph, coloring, k):
    """
    Combined objective to MINIMISE: conflicts are weighted heavily because
    a proper colouring is a hard constraint; imbalance is the soft
    (optimisation) objective on top of that.
    """
    return count_conflicts(graph, coloring) * 1000 + imbalance(coloring, k)


# ---------------------------------------------------------------------------
# Heuristic 1: Greedy construction heuristic (balance-aware)
# ---------------------------------------------------------------------------

def min_colors_needed(graph):
    """
    Estimate a starting number of colours k using standard greedy colouring
    (Welsh-Powell style, largest-degree-first). This gives an upper bound
    on the chromatic number, which we then try to make equitable.
    """
    order = sorted(range(graph.V), key=lambda v: -len(graph.neighbors(v)))
    result = [-1] * graph.V

    for u in order:
        used = {result[v] for v in graph.neighbors(u) if result[v] != -1}
        color = 0
        while color in used:
            color += 1
        result[u] = color

    return max(result) + 1


def greedy_equitable_coloring(graph, k):
    """
    Greedy construction heuristic for EQUITABLE graph colouring.

    Unlike standard greedy colouring (which just picks the first available
    colour), at each step we pick the AVAILABLE colour with the SMALLEST
    current class size. This actively steers the construction towards
    balanced colour classes instead of leaving balance to chance.
    """
    order = sorted(range(graph.V), key=lambda v: -len(graph.neighbors(v)))
    coloring = [-1] * graph.V
    sizes = [0] * k

    for u in order:
        used = {coloring[v] for v in graph.neighbors(u) if coloring[v] != -1}
        available = [c for c in range(k) if c not in used]

        if not available:
            # No legal colour left in k colours: fall back to the least
            # loaded colour (may introduce a conflict; local search will
            # try to repair it afterwards).
            color = min(range(k), key=lambda c: sizes[c])
        else:
            color = min(available, key=lambda c: sizes[c])

        coloring[u] = color
        sizes[color] += 1

    return coloring


# ---------------------------------------------------------------------------
# Heuristic 2: Local search (hill climbing with swap / recolour moves)
# ---------------------------------------------------------------------------

def local_search_equitable(graph, coloring, k, max_iterations=2000):
    """
    Hill-climbing local search that repairs conflicts and reduces
    imbalance in the colouring produced by the greedy heuristic.

    Move types:
      1. Recolour move: change a single vertex's colour.
      2. Swap move: exchange the colours of two vertices in different
         classes (keeps class sizes exactly the same, useful once the
         colouring is already balanced but still has conflicts).

    A move is accepted only if it does not increase the objective
    (conflicts * 1000 + imbalance). Ties are broken randomly to allow
    the search to escape flat regions.
    """
    coloring = coloring[:]
    best_score = objective(graph, coloring, k)

    for _ in range(max_iterations):
        if best_score == 0:
            break

        improved = False

        # --- Try recolour moves ---
        vertices = list(range(graph.V))
        random.shuffle(vertices)

        for u in vertices:
            original = coloring[u]
            best_color = original
            best_local_score = best_score

            for c in range(k):
                if c == original:
                    continue
                coloring[u] = c
                score = objective(graph, coloring, k)
                if score < best_local_score:
                    best_local_score = score
                    best_color = c

            coloring[u] = best_color

            if best_local_score < best_score:
                best_score = best_local_score
                improved = True

        if improved:
            continue

        # --- Try swap moves if recolouring alone found no improvement ---
        pairs = [(i, j) for i in range(graph.V) for j in range(i + 1, graph.V)]
        random.shuffle(pairs)

        for i, j in pairs:
            if coloring[i] == coloring[j]:
                continue

            coloring[i], coloring[j] = coloring[j], coloring[i]
            score = objective(graph, coloring, k)

            if score < best_score:
                best_score = score
                improved = True
                break
            else:
                coloring[i], coloring[j] = coloring[j], coloring[i]  # revert

        if not improved:
            break  # local optimum reached

    return coloring


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def equitable_coloring(graph, k=None, seed=None):
    """
    Full pipeline: greedy construction -> local search repair.
    Returns (coloring, k, stats_dict).
    """
    if seed is not None:
        random.seed(seed)

    if k is None:
        k = min_colors_needed(graph)

    greedy_result = greedy_equitable_coloring(graph, k)
    final_result = local_search_equitable(graph, greedy_result, k)

    stats = {
        "k": k,
        "greedy_conflicts": count_conflicts(graph, greedy_result),
        "greedy_imbalance": imbalance(greedy_result, k),
        "final_conflicts": count_conflicts(graph, final_result),
        "final_imbalance": imbalance(final_result, k),
        "class_sizes": class_sizes(final_result, k),
    }

    return final_result, k, stats


if __name__ == "__main__":

    g = Graph(9)

    edges = [
        (0, 1), (0, 2), (1, 2), (1, 3), (2, 4),
        (3, 4), (3, 5), (4, 6), (5, 6), (5, 7),
        (6, 8), (7, 8),
    ]
    for u, v in edges:
        g.add_edge(u, v)

    coloring, k, stats = equitable_coloring(g, seed=42)

    print(f"Vertices: {g.V}, Colours used (k): {k}")
    print(f"Final colouring: {coloring}")
    print(f"Colour class sizes: {stats['class_sizes']}")
    print(f"Conflicts (should be 0 for a valid colouring): {stats['final_conflicts']}")
    print(f"Imbalance (should be 0 or 1 for equitable): {stats['final_imbalance']}")
    print()
    print("Before local search (greedy only):")
    print(f"  conflicts = {stats['greedy_conflicts']}, imbalance = {stats['greedy_imbalance']}")
