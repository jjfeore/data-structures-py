"""Test the dll.py module."""


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
def new_dll():
    """Init a new doubly linked list."""
    from dll import DLinkedList
    return DLinkedList()


def test_stack_none(new_dll):
    """When a new stack is created with no iterable, head should be None."""
    assert new_dll.head is None
    assert new_dll.tail is None
    assert new_dll.length == 0


@pytest.mark.parametrize('val1, val2, val3', TEST_PUSH_MULT)
def test_stack_push_mult(val1, val2, val3, new_dll):
    """Push three values and check to see that they're in the DLL."""
    new_dll.push(val1)
    new_dll.push(val2)
    new_dll.push(val3)
    assert new_dll.head.val == val3
    assert new_dll.head.next.val == val2
    assert new_dll.head.next.next.val == val1


@pytest.mark.parametrize('val1, val2, val3', TEST_PUSH_MULT)
def test_stack_pop(val1, val2, val3, new_dll):
    """Push three values into a DLL, pop them and check the values."""
    new_dll.push(val1)
    new_dll.push(val2)
    new_dll.push(val3)
    assert new_dll.pop() == val3
    assert new_dll.pop() == val2
    assert new_dll.pop() == val1


@pytest.mark.parametrize('val1, val2, val3', TEST_PUSH_MULT)
def test_stack_append(val1, val2, val3, new_dll):
    """Append 3 values and check that they're in the DLL."""
    new_dll.append(val1)
    new_dll.append(val2)
    new_dll.append(val3)
    assert new_dll.tail.val == val3
    assert new_dll.tail.prev.val == val2
    assert new_dll.head.val == val1


@pytest.mark.parametrize('val1, val2, val3', TEST_PUSH_MULT)
def test_stack_shift(val1, val2, val3, new_dll):
    """Append 3 values and check that the right vals shift out."""
    new_dll.append(val1)
    new_dll.append(val2)
    new_dll.append(val3)
    assert new_dll.shift() == val3
    assert new_dll.shift() == val2
    assert new_dll.shift() == val1


@pytest.mark.parametrize('iterable, result', TEST_LEN)
def test_dll_len(iterable, result, new_dll):
    """Test the size/len of the list."""
    for idx in range(len(iterable)):
        new_dll.append(iterable[idx])
    assert len(new_dll) == result


@pytest.mark.parametrize('val1, val2, val3', TEST_PUSH_MULT)
def test_stack_remove(val1, val2, val3, new_dll):
    """Append 3 values and check that the right vals shift out."""
    new_dll.append(val1)
    new_dll.append(val2)
    new_dll.append(val3)
    new_dll.remove(val1)
    assert new_dll.head.val == val2
    assert new_dll.tail.val == val3
