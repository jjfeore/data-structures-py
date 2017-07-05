"""Test the graph_1.py module."""

import pytest


@pytest.fixture
def new_graph():
    """Init a new empty graph."""
    from graph_1 import Graph
    return Graph()


@pytest.fixture
def full_graph():
    """Init a graph with a lot of nodes, edges, and a circular edge."""
    from graph_1 import Graph
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
    return test


# def test_pri_que_raises_valerror_on_bad_priority(new_pri_que):
#     """Insert a value with a too-low priority. It should raise an error."""
#     with pytest.raises(ValueError):
#         new_pri_que.insert(5, -1)


# def test_pri_que_raises_typeerror_on_priority_as_non_int(new_pri_que):
#     """Insert a value with a too-low priority. It should raise an error."""
#     with pytest.raises(TypeError):
#         new_pri_que.insert(5, "hello")


def test_init_graph_empty(new_graph):
    """Instantiate a new graph."""
    assert new_graph.graph == {}


def test_graph_add_node(new_graph):
    """Add nodes and see if they're in the graph."""
    assert new_graph.graph == {}
    new_graph.add_node('test')
    assert new_graph.graph['test'] == []
    new_graph.add_node('test2')
    assert new_graph.graph['test2'] == []


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
    """Check to see if the edge method returns all the edges."""
    all_edges = full_graph.edges()
    assert ('third5', 'btm6') in all_edges
    assert ('third5', 'btm7') in all_edges
    assert ('third1', 'btm1') in all_edges
    assert ('third1', 'btm2') in all_edges
    assert ('third3', 'btm4') in all_edges
    assert ('third3', 'btm5') in all_edges
    assert ('third2', 'btm3') in all_edges
    assert ('top1', 'mid1') in all_edges
    assert ('top1', 'mid2') in all_edges
    assert ('mid1', 'third1') in all_edges
    assert ('mid1', 'third2') in all_edges
    assert ('mid1', 'top1') in all_edges
    assert ('mid1', 'third3') in all_edges
    assert ('mid2', 'third4') in all_edges
    assert ('mid2', 'third5') in all_edges


def test_graph_add_edge(full_graph):
    """Check to see if you can edges to the graph."""
    full_graph.add_edge('btm4', 'superbtm1')
    full_graph.add_edge('btm5', 'superbtm2')
    full_graph.add_edge('btm5', 'superbtm3')
    full_graph.add_edge('not_in_graph', 'superbtm1')
    all_edges = full_graph.edges()
    assert ('btm4', 'superbtm1') in all_edges
    assert ('btm5', 'superbtm2') in all_edges
    assert ('btm5', 'superbtm3') in all_edges
    assert ('not_in_graph', 'superbtm1') in all_edges


def test_graph_has_node(full_graph):
    """Check to see if the graph has a node or not."""
    assert full_graph.has_node('mid1')
    assert full_graph.has_node('third5')
    assert not full_graph.has_node('third6')


def test_graph_del_node_removes_node_and_all_edges_to_it(full_graph):
    """Removing a node should also remove all edges to it."""
    full_graph.del_node('mid1')
    assert not full_graph.has_node('mid1')
    all_edges = full_graph.edges()
    assert ('top1', 'mid1') not in all_edges
    assert ('mid1', 'third1') not in all_edges
    assert ('mid1', 'third2') not in all_edges
    assert ('mid1', 'top1') not in all_edges


def test_graph_del_edge(full_graph):
    """Remove an edge and check that it isn't in the graph anymore."""
    assert ('mid1', 'top1') in full_graph.edges()
    assert ('mid2', 'third4') in full_graph.edges()
    full_graph.del_edge('mid1', 'top1')
    full_graph.del_edge('mid2', 'third4')
    all_edges = full_graph.edges()
    assert ('mid1', 'top1') not in all_edges
    assert ('mid2', 'third4') not in all_edges
