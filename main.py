from graph import Graph

g = Graph()

# g.add_node("Input0", 0.2)
# g.add_node("Input1", 0.4)
# g.add_node("Hidden0", 0.1)
# g.add_node("Hidden1", 0.02)

# g.add_line("Input0", "Hidden0", 0)
# g.add_line("Input0", "Hidden1", 1)
# g.add_line("Input1", "Hidden0", 2)
# g.add_line("Input1", "Hidden1", 3)

g.add_node("1", 1)
g.add_node("2", 2)

g.add_line("1", "2", 3)
g.add_line("2", "1", 4)


for n in g.nodes:
    print(
        f"Node {n} with value {g.nodes[n].val} connects to nodes with value: ", end=""
    )
    for l in g.nodes[n].lines:
        print(f"{l.to.val} by line with value {l.val}", end=", ")
    print()
