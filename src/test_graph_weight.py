"""Test the graph_weighted.py module."""

import pytest


@pytest.fixture
def new_graph():
    """Init a new empty weighted graph."""
    from graph_weight import GraphWeighted
    return GraphWeighted()


@pytest.fixture
def full_graph():
    """Init a weighted graph with some shortcuts."""
    from graph_weight import GraphWeighted
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
    return test


def test_init_graph_empty(new_graph):
    """Instantiate a new weighted graph."""
    assert new_graph._graph == {}


def test_graph_add_node(new_graph):
    """Add nodes and see if they're in the weighted graph."""
    assert new_graph._graph == {}
    new_graph.add_node('test')
    assert new_graph._graph['test'] == {}
    new_graph.add_node('test2')
    assert new_graph._graph['test2'] == {}


def test_graph_nodes(new_graph):
    """Check to see if the nodes() method returns all nodes."""
    assert new_graph.nodes() == []
    new_graph.add_node('test')
    assert new_graph.nodes() == ['test']
    new_graph.add_node('test2')
    new_graph.add_node('test3')
    new_graph.add_node('test18')
    new_graph.add_node('bob')
    assert 'test2' in new_graph.nodes()
    assert 'bob' in new_graph.nodes()
    assert 'bill' not in new_graph.nodes()
    assert 'test18' in new_graph.nodes()
    assert 'test3' in new_graph.nodes()


def test_graph_edges(full_graph):
    """Check if the edge method returns all the edges w/ the right weights."""
    all_edges = full_graph.edges()
    assert ('third5', 'btm6', 33) in all_edges
    assert ('third5', 'btm7', 99) in all_edges
    assert ('third1', 'btm1', 3) in all_edges
    assert ('third1', 'btm2', 145) in all_edges
    assert ('third3', 'btm7', 4) in all_edges
    assert ('third3', 'btm4', 116) in all_edges
    assert ('third3', 'btm5', 167) in all_edges
    assert ('third2', 'btm3', 30) in all_edges
    assert ('top1', 'mid1', 78) in all_edges
    assert ('top1', 'mid2', 113) in all_edges
    assert ('mid1', 'third1', 23) in all_edges
    assert ('mid1', 'third2', 57) in all_edges
    assert ('mid1', 'top1', 16) in all_edges
    assert ('mid1', 'third3', 21) in all_edges
    assert ('mid2', 'third4', 78) in all_edges
    assert ('mid2', 'third5', 91) in all_edges


def test_graph_add_edge_raises_error(full_graph):
    """Adding an edge with an invalid weight raises an error."""
    with pytest.raises(ValueError):
        full_graph.add_edge('btm1', 'mid2', -1)


def test_graph_add_edge(full_graph):
    """Check to see if you can add edges and weights to the graph."""
    full_graph.add_edge('btm4', 'superbtm1', 53)
    full_graph.add_edge('btm5', 'superbtm2', 19)
    full_graph.add_edge('btm5', 'superbtm3', 700)
    full_graph.add_edge('not_in_graph', 'superbtm1', 18)
    all_edges = full_graph.edges()
    assert ('btm4', 'superbtm1', 53) in all_edges
    assert ('btm5', 'superbtm2', 19) in all_edges
    assert ('btm5', 'superbtm3', 700) in all_edges
    assert ('not_in_graph', 'superbtm1', 18) in all_edges


def test_graph_has_node(full_graph):
    """Check to see if the weighted graph has a node or not."""
    assert full_graph.has_node('mid1')
    assert full_graph.has_node('third5')
    assert not full_graph.has_node('third6')


def test_graph_del_node_removes_node_and_all_edges_to_it(full_graph):
    """Removing a node should also remove all edges to it."""
    full_graph.del_node('mid1')
    assert not full_graph.has_node('mid1')
    all_edges = full_graph.edges()
    assert ('top1', 'mid1', 78) not in all_edges
    assert ('mid1', 'third1', 23) not in all_edges
    assert ('mid1', 'third2', 57) not in all_edges
    assert ('mid1', 'top1', 16) not in all_edges


def test_graph_del_edge(full_graph):
    """Remove an edge and check that it isn't in the graph anymore."""
    assert ('mid1', 'top1', 16) in full_graph.edges()
    assert ('mid2', 'third4', 78) in full_graph.edges()
    full_graph.del_edge('mid1', 'top1')
    full_graph.del_edge('mid2', 'third4')
    all_edges = full_graph.edges()
    assert ('mid1', 'top1', 16) not in all_edges
    assert ('mid2', 'third4', 78) not in all_edges


def test_graph_adjacent_raises_error_on_bad_val(full_graph):
    """Trying to find if a non-existent node is adjacent to anything raises error."""
    with pytest.raises(ValueError):
        full_graph.adjacent('blah', 'top1')


def test_graph_adjacent(full_graph):
    """Check to see if several nodes are adjacent."""
    assert full_graph.adjacent('top1', 'mid1')
    assert full_graph.adjacent('mid1', 'third1')
    assert full_graph.adjacent('mid1', 'third2')
    assert full_graph.adjacent('mid1', 'third3')
    assert full_graph.adjacent('mid1', 'top1')
    assert not full_graph.adjacent('third3', 'third4')


def test_graph_neighbors_bad_key_raises_error(full_graph):
    """Getting neighbors of a non-node raises an error."""
    with pytest.raises(KeyError):
        full_graph.neighbors('blah')


def test_graph_neighbors(full_graph):
    """Check to see if all neighbors are returned."""
    mid1_neighbors = full_graph.neighbors('mid1')
    assert 'third1' in mid1_neighbors
    assert 'third2' in mid1_neighbors
    assert 'third3' in mid1_neighbors
    assert 'top1' in mid1_neighbors


def test_graph_get_node_raises_error(full_graph):
    """Passing get_node an invalid node raises a KeyError."""
    with pytest.raises(KeyError):
        full_graph.get_node('blah')


def test_graph_get_node(full_graph):
    """Passing get_node an invalid node raises a KeyError."""
    assert full_graph.get_node('top1') == {'mid1': 78, 'mid2': 113}
    assert full_graph.get_node('mid2') == {'third4': 78, 'third5': 91}


def test_graph_depth_first_with_non_key_raises_error(full_graph):
    """Traversing from a non-existent node raises an error."""
    with pytest.raises(ValueError):
        full_graph.depth_first_traversal('blah')


def test_graph_depth_first_returns_list(full_graph):
    """Check that DFT returns list of right length with correct start."""
    test = full_graph.depth_first_traversal('top1')
    assert isinstance(test, list)
    assert len(test) == 15
    assert test[0] == 'top1'


def test_graph_breadth_first_with_non_key_raises_error(full_graph):
    """Traversing from a non-existent node raises an error."""
    with pytest.raises(ValueError):
        full_graph.breadth_first_traversal('blah')


def test_graph_breadth_first_returns_list(full_graph):
    """Check that BFT returns list of right length with correct start."""
    test = full_graph.breadth_first_traversal('top1')
    assert isinstance(test, list)
    assert len(test) == 15
    assert test[0] == 'top1'


def test_graph_dijkstra(full_graph):
    """Dijkstra should return two dicts of distances and previous nodes."""
    from graph_weight import dijkstra
    dist, prev = dijkstra(full_graph, 'top1')
    assert dist == {
        'btm1': 104,
        'btm2': 246,
        'btm3': 165,
        'btm4': 215,
        'btm5': 266,
        'btm6': 237,
        'btm7': 103,
        'mid1': 78,
        'mid2': 113,
        'third1': 101,
        'third2': 135,
        'third3': 99,
        'third4': 191,
        'third5': 204,
        'top1': 0
    }
    assert prev == {
        'btm1': 'third1',
        'btm2': 'third1',
        'btm3': 'third2',
        'btm4': 'third3',
        'btm5': 'third3',
        'btm6': 'third5',
        'btm7': 'third3',
        'mid1': 'top1',
        'mid2': 'top1',
        'third1': 'mid1',
        'third2': 'mid1',
        'third3': 'mid1',
        'third4': 'mid2',
        'third5': 'mid2',
        'top1': None
    }


def test_shortest_path(full_graph):
    """Shortest path should return the shortest path w/ Dijkstra's algo."""
    from graph_weight import shortest_path
    assert shortest_path(full_graph, 'top1', 'btm7') == ['top1', 'mid1', 'third3', 'btm7']
    assert shortest_path(full_graph, 'mid2', 'btm6') == ['mid2', 'third5', 'btm6']
