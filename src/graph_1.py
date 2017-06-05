"""Implement a graph data structure."""


class Graph(object):
    """Define graph and modules."""
    def __init__(self):
        self.graph = {}

    def nodes(self):
        return list(self.graph.keys())

    def edges(self):
        """Lists the edges."""
        edges = []
        for node in self.graph:
            for i in self.graph[node]:
                edges.append((node, i))
        return edges

    def add_node(self, x):
        """Adds a node with a iterable which is a neighbor of x."""
        if not self.graph[x]:
            self.graph[x] = []

    def add_edge(self, val1, val2):
        """Adds a edge to two values."""
        if not self.graph[val1]:
            self.graph[val1] = []
        if not self.graph[val2]:
            self.graph[val2] = []
        if val2 not in self.graph[val1]:
            self.graph[val1].append(val2)

    def del_node(self, node):
        """Removes node from graph."""
        self.graph.pop(node)

    def del_edge(self, val1, val2):
        if val2 in self.graph[val1]:
            del self.graph[val1][val2]
