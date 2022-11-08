class Graph:
    class Node:
        def __init__(self, val) -> None:
            self.val = val
            self.lines: list[Graph.Line] = []

    class Line:
        def __init__(self, val, to) -> None:
            self.val = val
            self.to: Graph.Node = to

    def __init__(self) -> None:
        self.nodes: dict[str : Graph.Node]
