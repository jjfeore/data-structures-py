"""Test the tree.py module."""
import pytest
from BST import BinarySearchTree

a = BinarySearchTree([12, 42, 4, 87, 2, 65, 0])

b = BinarySearchTree([5, 3, 7, 2, 8, 4, 9, 1])

c = BinarySearchTree([-2, -6, 22.55, 0, -94, 2, -1])


@pytest.fixture
def bitr():  # pragma: no cover
    """Init a new Binary Tree."""
    tree = BinarySearchTree()
    return tree


@pytest.fixture
def bitr_iter():  # pragma: no cover
    """Init a new Binary tree from an iterable."""
    return a.iterable
    return b.iterable
    return c.iterable


def test_tree_empty():
    """Instantiate a new Binary tree, that should be an empty list."""
    b = BinarySearchTree([])
    assert b.size == 0


def test_type_error_insert():
    """Test for type error in insert function"""
    with pytest.raises(TypeError):
        b.insert('not a number')


def test_type_error_search():
    """Test for type error in the search function"""
    with pytest.raises(TypeError):
        b.search('still not a number')


def test_bitr_search():
    """Test the seartch function"""
    assert a.search(12).left.val == 4
    assert a.search(4).left.val == 2
    assert a.search(87).left.val == 65
    assert b.search(3).left.val == 2
    assert b.search(5).left.val == 3
    assert c.search(-2).left.val == -6
    assert c.search(0).left.val == -1
    assert c.search(-6).left.val == -94


def test_bitr_iter_in_order():
    """Test the in order funciton."""
    gena = a.in_order()
    a_list = [item for item in gena]
    assert a_list == [0, 2, 4, 12, 42, 65, 87]
    assert a_list[0] == 0
    assert a_list[1] == 2
    assert a_list[2] == 4
    assert len(a_list) == 7
    genb = b.in_order()
    b_list = [item for item in genb]
    assert b_list == [1, 2, 3, 4, 5, 7, 8, 9]
    assert b_list[0] == 1
    assert b_list[1] == 2
    assert b_list[2] == 3
    assert len(b_list) == 8
    genc = c.in_order()
    c_list = [item for item in genc]
    assert c_list == [-94, -6, -2, -1, 0, 2, 22.55]
    assert c_list[0] == -94
    assert c_list[1] == -6
    assert c_list[2] == -2
    assert len(c_list) == 7


def test_bitr_iter_pre_order():
    """Test the pre order funciton."""
    gena = a.pre_order()
    a_list = [item for item in gena]
    assert a_list == [12, 4, 2, 0, 42, 87, 65]
    assert a_list[0] == 12
    assert a_list[1] == 4
    assert a_list[6] == 65
    assert len(a_list) == 7
    genb = b.pre_order()
    b_list = [item for item in genb]
    assert b_list == [5, 3, 2, 1, 4, 7, 8, 9]
    assert b_list[0] == 5
    assert b_list[1] == 3
    assert b_list[6] == 8
    assert len(b_list) == 8
    genc = c.pre_order()
    c_list = [item for item in genc]
    assert c_list == [-2, -6, -94, 22.55, 0, -1, 2]
    assert c_list[0] == -2
    assert c_list[1] == -6
    assert c_list[6] == 2
    assert len(c_list) == 7


def test_bitr_iter_post_order():
    """Test the post order funciton."""
    gena = a.post_order()
    a_list = [item for item in gena]
    assert a_list == [0, 2, 4, 65, 87, 42, 12]
    assert a_list[0] == 0
    assert a_list[3] == 65
    assert a_list[2] == 4
    assert len(a_list) == 7
    gen = b.post_order()
    b_list = [item for item in gen]
    assert b_list == [1, 2, 4, 3, 9, 8, 7, 5]
    assert b_list[0] == 1
    assert b_list[3] == 3
    assert b_list[2] == 4
    assert len(b_list) == 8
    genc = c.post_order()
    c_list = [item for item in genc]
    assert c_list == [-94, -6, -1, 2, 0, 22.55, -2]
    assert c_list[0] == -94
    assert c_list[3] == 2
    assert c_list[2] == -1
    assert len(c_list) == 7


def test_bitr_breadth():
    """Test the breadth first traversal."""
    abf = a.breadth_first()
    assert [ab.val for ab in abf] == [12, 4, 42, 2, 87, 0, 65]
    bbf = b.breadth_first()
    assert [bb.val for bb in bbf] == [5, 3, 7, 2, 4, 8, 1, 9]
    cbf = c.breadth_first()
    assert [cb.val for cb in cbf] == [-2, -6, 22.55, -94, 0, -1, 2]


def test_bitr_insert():
    """Push the insert function."""
    a.insert(30)
    gena = a.in_order()
    a_list = [item for item in gena]
    assert a_list == [0, 2, 4, 12, 30, 42, 65, 87]
    a.insert(2.5)
    gena = a.in_order()
    a_list = [item for item in gena]
    assert a_list == [0, 2, 2.5, 4, 12, 30, 42, 65, 87]
    b.insert(1.1)
    genb = b.in_order()
    b_list = [item for item in genb]
    assert b_list == [1, 1.1, 2, 3, 4, 5, 7, 8, 9]
    b.insert(-90)
    genb = b.in_order()
    b_list = [item for item in genb]
    assert b_list == [-90, 1, 1.1, 2, 3, 4, 5, 7, 8, 9]
    c.insert(31)
    genc = c.in_order()
    c_list = [item for item in genc]
    assert c_list == [-94, -6, -2, -1, 0, 2, 22.55, 31]
    c.insert(22.54)
    genc = c.in_order()
    c_list = [item for item in genc]
    assert c_list == [-94, -6, -2, -1, 0, 2, 22.54, 22.55, 31]
