from graph import Graph

g = Graph()

g.add_node("Input0", 0.2)
g.add_node("Input1", 0.4)
g.add_node("Hidden0", 0.1)
g.add_node("Hidden1", 0.02)

g.add_line("Input0", "Hidden0", 0)
g.add_line("Input0", "Hidden1", 1)
g.add_line("Input1", "Hidden0", 2)
g.add_line("Input1", "Hidden0", 3)


for i in g.nodes:
    print(i)
