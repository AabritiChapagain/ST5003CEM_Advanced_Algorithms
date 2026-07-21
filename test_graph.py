from task2.graph import Graph

g = Graph()

g.add_road("Kathmandu", "Pokhara", 200)
g.add_road("Kathmandu", "Chitwan", 150)
g.add_road("Pokhara", "Butwal", 165)
g.add_road("Chitwan", "Butwal", 120)
g.add_road("Butwal", "Nepalgunj", 280)

g.display()