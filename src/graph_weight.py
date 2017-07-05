"""Implement a weighted-edge graph data structure."""


class GraphWeighted(object):
    """Define a weighted graph and modules."""

    def __init__(self):
        """Instantiate a new dictionary as the basis of our graph."""
        self._graph = {}

    def nodes(self):
        """Return a list of all the nodes in the graph."""
        return list(self._graph.keys())

    def edges(self):
        """List the edges and their weights."""
        edges = []
        for node in self._graph:
            for i in self._graph[node]:
                edges.append((node, i, self._graph[node][i]))
        return edges

    def add_node(self, x):
        """Add a vertex to the graph, represented by an empty dictionary."""
        if x not in self._graph:
            self._graph[x] = {}

    def add_edge(self, val1, val2, weight):
        """Add an edge between two values, with an associated weight."""
        if not isinstance(weight, int) or weight < 0:
            raise ValueError('Weight parameter must be a positive integer.')
        if val1 not in self._graph:
            self._graph[val1] = {}
        if val2 not in self._graph:
            self._graph[val2] = {}
        self._graph[val1][val2] = weight

    def del_node(self, node):
        """Remove node from graph and all edges to that node."""
        if self._graph.pop(node):
            for a_node in self._graph:
                if node in self._graph[a_node]:
                    self._graph[a_node].pop(node)

    def has_node(self, val):
        """Check to see if a specified node exists in the graph."""
        if val in self._graph:
            return True
        return False

    def del_edge(self, val1, val2):
        """Delete the edge between two nodes."""
        if val2 in self._graph[val1]:
            self._graph[val1].pop(val2)

    def adjacent(self, val1, val2):
        """Return whether or not two nodes are linked by an edge."""
        if not self.has_node(val1) or not self.has_node(val2):
            raise ValueError('_Graph does not contain one of the nodes')
        if val2 in self._graph[val1]:
            return True
        else:
            return False

    def neighbors(self, val):
        """Return a list all of a node's neighbors."""
        try:
            return list(self._graph[val].keys())
        except KeyError:
            raise KeyError('{} not in the graph.'.format(val))

    def get_node(self, val):
        """Return the node."""
        try:
            return self._graph[val]
        except KeyError:
            raise KeyError('{} not in the graph.'.format(val))

    def depth_first_traversal(self, val, visited=None):
        """Perform a full depth-first traversal of the graph."""
        if not visited:
            visited = []
        if val in self._graph:
            visited.append(val)
        else:
            raise ValueError('Specified value is not a node in the graph')
        for neighbor in self._graph[val]:
            if neighbor not in visited:
                visited.extend(self.depth_first_traversal(neighbor, visited))
        clean_vis = []
        for value in visited:
            if value not in clean_vis:
                clean_vis.append(value)
        return clean_vis

    def breadth_first_traversal(self, val):
        """Perform a full breadth-first traversal of the graph."""
        if val in self._graph:
            visited = [val]
        else:
            raise ValueError('Specified value is not a node in the graph')
        for node in visited:
            for neighbor in self._graph[node]:
                if neighbor not in visited:
                    visited.append(neighbor)
        return visited


def dijkstra(graph, start, end=None):
    gcopy = {}
    dist = {}
    prev = {}
    for node in graph.nodes():
        dist[node] = float('inf')
        prev[node] = None
        gcopy[node] = graph.get_node(node)
    dist[start] = 0
    while gcopy:
        curr = min(gcopy, key=dist.get)
        if curr == end:
            return dist, prev
        curr_list = gcopy[curr]
        gcopy.pop(curr)
        for neighbor in curr_list:
            tmp = dist[curr] + curr_list[neighbor]
            if tmp < dist[neighbor]:
                dist[neighbor] = tmp
                prev[neighbor] = curr
    return dist, prev


def shortest_path(graph, start, end):
    dist, prev = dijkstra(graph, start, end)
    path = []
    while True:
        path.append(end)
        if end == start:
            break
        end = prev[end]
    # import pdb; pdb.set_trace()
    return path[::-1]


if __name__ == '__main__':  # pragma: no cover
    test = GraphWeighted()
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
    test.add_edge('top1', 'mid1', 78)
    test.add_edge('top1', 'mid2', 113)
    test.add_edge('mid1', 'third1', 23)
    test.add_edge('mid1', 'third2', 57)
    test.add_edge('mid1', 'top1', 16)
    test.add_edge('mid1', 'third3', 21)
    test.add_edge('mid2', 'third4', 78)
    test.add_edge('mid2', 'third5', 91)
    test.add_edge('third1', 'btm1', 3)
    test.add_edge('third1', 'btm2', 145)
    test.add_edge('third2', 'btm3', 30)
    test.add_edge('third3', 'btm7', 4)
    test.add_edge('third3', 'btm4', 116)
    test.add_edge('third3', 'btm5', 167)
    test.add_edge('third5', 'btm6', 33)
    test.add_edge('third5', 'btm7', 99)
    print('DFT: {}'.format(test.depth_first_traversal('top1')))
    print('BFT: {}'.format(test.breadth_first_traversal('top1')))
    print('Edges: {}'.format(test.edges()))
    print(shortest_path(test, 'top1', 'btm7'))
