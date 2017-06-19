"""Test the heap.py module."""
import pytest


@pytest.fixture
def new_heap():
    """Init a new Binary Heap."""
    from heap import Biheap
    return Biheap()


@pytest.fixture
def new_heap_iter():
    """Init a new Binary Heap from an iterable."""
    from heap import Biheap
    return Biheap([3, 4, 12, 8, 5, 18])


def test_heap_empty(new_heap):
    """Instantiate a new Binary heap, that should be an empty list."""
    assert new_heap.heap == []


def test_new_heap_iter(new_heap_iter):
    """Create a Bin heap with an iterable and check it is equal."""
    assert new_heap_iter.heap == [3, 4, 12, 8, 5, 18]


def test_push_no_bubble(new_heap_iter):
    """Push with large value and no bubbling."""
    new_heap_iter.push(30)
    assert new_heap_iter.heap == [3, 4, 12, 8, 5, 18, 30]


def test_push_bubbles(new_heap_iter):
    """Push small value and see if bubbling occurs."""
    new_heap_iter.push(2)
    assert new_heap_iter.heap == [2, 4, 3, 8, 5, 18, 12]
    new_heap_iter.push(10)
    assert new_heap_iter.heap == [2, 4, 3, 8, 5, 18, 12, 10]
    new_heap_iter.push(78)
    assert new_heap_iter.heap == [2, 4, 3, 8, 5, 18, 12, 10, 78]
    new_heap_iter.push(1)
    assert new_heap_iter.heap == [1, 2, 3, 8, 4, 18, 12, 10, 78, 5]
    new_heap_iter.push(9)
    assert new_heap_iter.heap == [1, 2, 3, 8, 4, 18, 12, 10, 78, 5, 9]
    new_heap_iter.push(6)
    assert new_heap_iter.heap == [1, 2, 3, 8, 4, 6, 12, 10, 78, 5, 9, 18]


def test_pop_empty_heap(new_heap):
    """Pop on an empty heap returns None."""
    assert new_heap.pop() is None


def test_pop_bubbles(new_heap_iter):
    """Pop on a heap should still bubble."""
    assert new_heap_iter.pop() == 3
    assert new_heap_iter.heap == [4, 5, 12, 8, 18]
    assert new_heap_iter.pop() == 4
    assert new_heap_iter.heap == [5, 8, 12, 18]
    assert new_heap_iter.pop() == 5
    assert new_heap_iter.heap == [8, 18, 12]


def test_pop_short_heap(new_heap):
    new_heap.push(5)
    new_heap.push(1)
    assert new_heap.heap == [1, 5]
    assert new_heap.pop() == 1
    assert new_heap.heap == [5]
    assert new_heap.pop() == 5
    assert new_heap.heap == []
    assert new_heap.pop() is None
