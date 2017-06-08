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
        if x not in self.graph:
            self.graph[x] = []

    def add_edge(self, val1, val2):
        """Add an edge between two values."""
        if val1 not in self.graph:
            self.graph[val1] = []
        if val2 not in self.graph:
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

    def depth_first_traversal(self, val, visited=[]):
        """Perform a full depth-first traversal of the graph."""
        if val in self.graph:
            visited.append(val)
        else:
            raise ValueError('Specified value is not a node in the graph')
        for neighbor in self.graph[val]:
            if neighbor not in visited:
                visited.extend(self.depth_first_traversal(neighbor, visited))
        clean_vis = []
        for value in visited:
            if value not in clean_vis:
                clean_vis.append(value)
        return clean_vis

    def breadth_first_traversal(self, val):
        """Perform a full breadth-first traversal of the graph."""
        if val in self.graph:
            visited = [val]
        else:
            raise ValueError('Specified value is not a node in the graph')
        for node in visited:
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.append(neighbor)
        return visited


if __name__ == '__main__':
    test = Graph()
    test.add_node('top1')
    test.add_node('mid1')
    test.add_node('mid2')
    test.add_node('third1')
    test.add_node('third2')
    test.add_node('third3')
    test.add_node('third4')
    test.add_node('third5')
    test.add_node('btm1')
    test.add_node('btm2')
    test.add_node('btm3')
    test.add_node('btm4')
    test.add_node('btm5')
    test.add_node('btm6')
    test.add_node('btm7')
    test.add_edge('top1', 'mid1')
    test.add_edge('top1', 'mid2')
    test.add_edge('mid1', 'third1')
    test.add_edge('mid1', 'third2')
    test.add_edge('mid1', 'top1')
    test.add_edge('mid1', 'third3')
    test.add_edge('mid2', 'third4')
    test.add_edge('mid2', 'third5')
    test.add_edge('third1', 'btm1')
    test.add_edge('third1', 'btm2')
    test.add_edge('third2', 'btm3')
    test.add_edge('third3', 'btm4')
    test.add_edge('third3', 'btm5')
    test.add_edge('third5', 'btm6')
    test.add_edge('third5', 'btm7')
    print('DFT: {}'.format(test.depth_first_traversal('top1')))
    print('BFT: {}'.format(test.breadth_first_traversal('top1')))
