import pytest
from trie import TrieTree

@pytest.fixture
def trie():
    tree = TrieTree()
    return tree


def test_tree_empty():
    t = trie()
    assert t.size == 0


def test_tree_insert():
    t = trie()
    t.insert('monkey')
    assert t.letter_sets == ['monkey']
