from task2.graph import Graph
from task2.bellman_ford import bellman_ford

g = Graph()

g.add_road("A", "B", 1)
g.add_road("B", "C", -2)
g.add_road("C", "A", -2)

bellman_ford(g, "A")