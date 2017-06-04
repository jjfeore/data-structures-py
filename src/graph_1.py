'''Implement a graph data structure'''


class Node(object):
    def __init__(self, iter):
        self.iter = iter


class Graph(object):
    '''Define graph and modules'''

    def __init__(self):
        self.node = {}

    def nodes(self):
        return self.nodes.keys()

    def edges(self):
        '''Lists the edges'''
        edges = []
        for node in self.nodes:
            for i in self.nodes[node]:
                edge = (node, i)
                if edge not in edges:
                    edges.append(edge)
        return edges

    def add_node(self, iter, x):
        """Adds a node with a iterable which is a neighbor of x"""
        node = Node(iter)
        self.nodes[node] = [x]
        self.nodes[x].append(node)

    def del_node(self, node):
        """Removes node from graph"""
        for node in self.nodes:
            if node in self.nodes[node]:
                self.nodes[node].remove(node)
        del self.nodes[node]