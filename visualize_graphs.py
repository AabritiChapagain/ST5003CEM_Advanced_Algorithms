import networkx as nx
import matplotlib.pyplot as plt

# -----------------------
# Shortest Path Tree
# -----------------------

G = nx.DiGraph()

edges = [
    ("Kathmandu", "Pokhara", 200),
    ("Kathmandu", "Chitwan", 150),
    ("Chitwan", "Butwal", 120),
    ("Butwal", "Nepalgunj", 280)
]

for u, v, w in edges:
    G.add_edge(u, v, weight=w)

plt.figure(figsize=(8,6))

pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    font_size=10
)

labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Dijkstra Shortest Path Tree")
plt.savefig("graphs/dijkstra_tree.png")
plt.close()


# -----------------------
# Minimum Spanning Tree
# -----------------------

H = nx.Graph()

edges = [
    ("Kathmandu", "Chitwan", 150),
    ("Chitwan", "Butwal", 120),
    ("Butwal", "Pokhara", 165),
    ("Butwal", "Nepalgunj", 280)
]

for u, v, w in edges:
    H.add_edge(u, v, weight=w)

plt.figure(figsize=(8,6))

pos = nx.spring_layout(H, seed=42)

nx.draw(
    H,
    pos,
    with_labels=True,
    node_size=2000,
    font_size=10
)

labels = nx.get_edge_attributes(H, "weight")
nx.draw_networkx_edge_labels(H, pos, edge_labels=labels)

plt.title("Prim Minimum Spanning Tree")
plt.savefig("graphs/prim_mst.png")
plt.close()

print("Graph visualizations created successfully!")