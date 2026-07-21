from graph import Graph
from prim import prim

g = Graph()

# Undirected graph (roads added both ways)
roads = [
    ("Kathmandu", "Pokhara", 200),
    ("Kathmandu", "Chitwan", 150),
    ("Pokhara", "Butwal", 165),
    ("Chitwan", "Butwal", 120),
    ("Butwal", "Nepalgunj", 280),
]

for source, destination, distance in roads:
    g.add_road(source, destination, distance)
    g.add_road(destination, source, distance)

mst, total = prim(g, "Kathmandu")

print("Minimum Spanning Tree:")

for source, destination, weight in mst:
    print(f"{source} -> {destination} ({weight} km)")

print(f"\nTotal Weight = {total} km")