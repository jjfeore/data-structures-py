"""Test the que.py module."""


import pytest


TEST_ENQ = [
    (1, 2, 3),
    (800, 'String', 5),
    ('String', ['list'], 17),
    ([5, 3, 17], [5, 'list two'], 'another string')
]


TEST_LEN = [
    ([1], 1),
    ((17, 5, 100), 3),
    ('String', 6),
    ([5, 3, 17], 3)
]


@pytest.fixture
def new_que():
    """Init a new doubly linked list."""
    from que import Queue
    return Queue()


def test_que_none(new_que):
    """When a new stack is created with no iterable, head should be None."""
    assert new_que.newDLL.head is None
    assert new_que.newDLL.tail is None
    assert new_que.newDLL.length == 0


@pytest.mark.parametrize('val1, val2, val3', TEST_ENQ)
def test_stack_enq(val1, val2, val3, new_que):
    """Push three values and check to see that they're in the DLL."""
    new_que.enqueue(val1)
    new_que.enqueue(val2)
    new_que.enqueue(val3)
    assert new_que.newDLL.head.val == val3
    assert new_que.newDLL.head.next.val == val2
    assert new_que.newDLL.head.next.next.val == val1


@pytest.mark.parametrize('val1, val2, val3', TEST_ENQ)
def test_stack_deque(val1, val2, val3, new_que):
    """Append 3 values and check that the right vals shift out."""
    new_que.enqueue(val1)
    new_que.enqueue(val2)
    new_que.enqueue(val3)
    assert new_que.dequeue() == val1
    assert new_que.dequeue() == val2
    assert new_que.dequeue() == val3


@pytest.mark.parametrize('iterable, result', TEST_LEN)
def test_dll_len(iterable, result, new_que):
    """Test the size/len of the queue."""
    for idx in range(len(iterable)):
        new_que.enqueue(iterable[idx])
    assert len(new_que) == result
    assert new_que.size() == result
