"""Test the dqueue.py module."""

import pytest


@pytest.fixture
def new_pri_que():
    """Init a new pque."""
    from priorityq import Priorityq
    return Priorityq()


def test_pri_que_raises_valerror_on_bad_priority(new_pri_que):
    """Insert a value with a too-low priority. It should raise an error."""
    with pytest.raises(ValueError):
        new_pri_que.insert(5, -1)


def test_pri_que_raises_typeerror_on_priority_as_non_int(new_pri_que):
    """Insert a value with a too-low priority. It should raise an error."""
    with pytest.raises(TypeError):
        new_pri_que.insert(5, "hello")


def test_pri_que_insert_no_pri(new_pri_que):
    """Insert a single value and make sure it's in the pque."""
    new_pri_que.insert(5)
    assert new_pri_que.prq[0] == [5, 0]


def test_pri_que_insert_multiple_no_pri(new_pri_que):
    """Insert multiple values with no priority. Should not alter queue."""
    new_pri_que.insert(5)
    new_pri_que.insert(8)
    new_pri_que.insert(3)
    new_pri_que.insert(100)
    new_pri_que.insert(700)
    new_pri_que.insert(-1)
    assert new_pri_que.prq[0] == [5, 0]


def test_pri_que_insert_multiple_with_pris(new_pri_que):
    """Insert values with priorty and make sure the queue adjusts."""
    new_pri_que.insert(5, 8)
    new_pri_que.insert(8, 1)
    new_pri_que.insert("a string", 9)
    new_pri_que.insert(100)
    new_pri_que.insert(700, 2)
    new_pri_que.insert(-1, 0)
    assert new_pri_que.prq[0] == ["a string", 9]
    new_pri_que.insert(300, 10)
    assert new_pri_que.prq[0] == [300, 10]
    new_pri_que.insert(3, 17)
    assert new_pri_que.prq[0] == [3, 17]


def test_pri_que_pop(new_pri_que):
    """Check that pop returns the right value and moves the next highest val up."""
    assert new_pri_que.pop() is None
    new_pri_que.insert(5, 8)
    new_pri_que.insert(8, 1)
    new_pri_que.insert("a string", 9)
    new_pri_que.insert(100)
    new_pri_que.insert(700, 2)
    new_pri_que.insert(-1, 0)
    new_pri_que.insert(300, 10)
    new_pri_que.insert(3, 17)
    assert new_pri_que.prq[0] == [3, 17]
    assert new_pri_que.pop() == 3
    assert new_pri_que.prq[0] == [300, 10]
    assert new_pri_que.pop() == 300


def test_pri_que_peek(new_pri_que):
    """Insert multiple values and make sure peek works at each point."""
    assert new_pri_que.peek() is None
    new_pri_que.insert(100)
    assert new_pri_que.peek() == 100
    new_pri_que.insert(7, 1)
    assert new_pri_que.peek() == 7
    new_pri_que.insert(300, 8)
    assert new_pri_que.peek() == 300
    new_pri_que.insert(500)
    assert new_pri_que.peek() == 300
