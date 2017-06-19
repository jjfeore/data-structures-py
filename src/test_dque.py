"""Test the dqueue.py module."""

import pytest


TEST_PUSH = [
    (1, 1),
    (800, 800),
    ('String', 'String'),
    ([5, 3, 17], [5, 3, 17])
]


TEST_PUSH_MULT = [
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
def new_dque():
    """Init a new dqueue."""
    from dqueue import Dque
    return Dque()


def test_stack_none(new_dque):
    """Instantiate a new dqueue, head and tail should be None."""
    assert new_dque.new_dll.head is None
    assert new_dque.new_dll.tail is None
    assert new_dque.size() == 0


@pytest.mark.parametrize('val1, val2, val3', TEST_PUSH_MULT)
def test_sque_append_mult(val1, val2, val3, new_dque):
    """Append three values and check to see that they're in the Dqueue."""
    new_dque.append(val1)
    new_dque.append(val2)
    new_dque.append(val3)
    assert new_dque.new_dll.head.val == val1
    assert new_dque.new_dll.head.next.val == val2
    assert new_dque.new_dll.head.next.next.val == val3


@pytest.mark.parametrize('val1, val2, val3', TEST_PUSH_MULT)
def test_dque_pop(val1, val2, val3, new_dque):
    """Append 3 values, check that pop gets the val at the end of the dque."""
    new_dque.append(val1)
    new_dque.append(val2)
    new_dque.append(val3)
    assert new_dque.pop() == val3
    assert new_dque.pop() == val2
    assert new_dque.pop() == val1


@pytest.mark.parametrize('val1, val2, val3', TEST_PUSH_MULT)
def test_dque_appendleft(val1, val2, val3, new_dque):
    """Append 3 values, check that they're in the Dque in the right order."""
    new_dque.appendleft(val1)
    new_dque.appendleft(val2)
    new_dque.appendleft(val3)
    assert new_dque.new_dll.tail.val == val1
    assert new_dque.new_dll.tail.prev.val == val2
    assert new_dque.new_dll.head.val == val3


@pytest.mark.parametrize('val1, val2, val3', TEST_PUSH_MULT)
def test_dque_popleft(val1, val2, val3, new_dque):
    """Push into a Dque, pop them from the end and check the values."""
    new_dque.append(val1)
    new_dque.append(val2)
    new_dque.append(val3)
    assert new_dque.popleft() == val1
    assert new_dque.popleft() == val2
    assert new_dque.popleft() == val3


@pytest.mark.parametrize('val1, val2, val3', TEST_PUSH_MULT)
def test_dque_peek(val1, val2, val3, new_dque):
    """Append 3 values and confirm that peek sees the end of the dque."""
    new_dque.append(val1)
    new_dque.append(val2)
    new_dque.append(val3)
    assert new_dque.peek() == val3


@pytest.mark.parametrize('val1, val2, val3', TEST_PUSH_MULT)
def test_dque_peekleft(val1, val2, val3, new_dque):
    """Append 3 values and confirm that peekleft sees the front of the dque."""
    new_dque.append(val1)
    new_dque.append(val2)
    new_dque.append(val3)
    assert new_dque.peekleft() == val1


@pytest.mark.parametrize('iterable, result', TEST_LEN)
def test_dque_size(iterable, result, new_dque):
    """Test the size of the list."""
    for idx in range(len(iterable)):
        new_dque.append(iterable[idx])
    assert new_dque.size() == result
