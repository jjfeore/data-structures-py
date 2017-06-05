"""Implement a graph data structure."""


class Graph(object):
    """Define graph and modules."""

    def __init__(self):
        """Instantiate a new graph."""
        self.graph = {}

    def nodes(self):
        """Return a list of all the nodes in the graph."""
        return list(self.graph.keys())

    def edges(self):
        """List the edges."""
        edges = []
        for node in self.graph:
            for i in self.graph[node]:
                edges.append((node, i))
        return edges

    def add_node(self, x):
        """Add a node with a iterable which is a neighbor of x."""
        if not self.graph[x]:
            self.graph[x] = []

    def add_edge(self, val1, val2):
        """Add an edge between two values."""
        if not self.graph[val1]:
            self.graph[val1] = []
        if not self.graph[val2]:
            self.graph[val2] = []
        if val2 not in self.graph[val1]:
            self.graph[val1].append(val2)

    def del_node(self, node):
        """Remove node from graph."""
        if self.graph.pop(node):
            for a_node in self.graph:
                if node in self.graph[a_node]:
                    self.graph[a_node].remove(node)

    def has_node(self, val):
        """Check to see if a specified node exists in the graph. Return a bool."""
        if val in self.graph:
            return True
        return False

    def del_edge(self, val1, val2):
        """Delete the edge between two nodes."""
        if val2 in self.graph[val1]:
            del self.graph[val1][val2]

    def adjacent(self, val1, val2):
        """Return a list ."""
        if not self.has_node(val1) or not self.has_node(val2):
            raise ValueError('Graph does not contain one of the nodes')
        if val2 in self.graph[val1]:
            return True
        else:
            return False

    def neighbors(self, val):
        """Return a list all of a node's neighbors."""
        try:
            return self.graph[val]
        except KeyError:
            raise KeyError('{} not in the graph.'.format(val))
