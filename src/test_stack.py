"""Test the stack.py module."""


import pytest


TEST_ITER = [
    ([1], 1),
    ((17, 5, 100), 100),
    ('String', 'g'),
    ([5, 3, 17], 17)
]


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


def test_stack_none():
    """When a new stack is created with no iterable, head should be None."""
    from stack import Stack
    test_stack = Stack()
    assert test_stack.head is None


@pytest.mark.parametrize('iterable, result', TEST_ITER)
def test_stack_iterable(iterable, result):
    """When a new stack is created with an iterable, head should be last element of the iterable."""
    from stack import Stack
    test_stack = Stack(iterable)
    assert test_stack.head.val == result


@pytest.mark.parametrize('val', TEST_PUSH)
def test_stack_push(val):
    """When a value is pushed to a stack, the head value should equal that value."""
    from stack import Stack
    test_stack = Stack()
    test_stack.push(val)
    assert test_stack.head.val == val


@pytest.mark.parametrize('val1, val2, val3', TEST_PUSH_MULT)
def test_stack_push_mult(val1, val2, val3):
    """Push three values and check to see that they're in the stack."""
    from stack import Stack
    test_stack = Stack()
    test_stack.push(val1)
    test_stack.push(val2)
    test_stack.push(val3)
    assert test_stack.head.val == val3
    assert test_stack.head.next.val == val2
    assert test_stack.head.next.next.val == val1


@pytest.mark.parametrize('val1, val2, val3', TEST_PUSH_MULT)
def test_stack_pop(val1, val2, val3):
    """Push three values into a stack, pop them and check the values."""
    from stack import Stack
    test_stack = Stack()
    test_stack.push(val1)
    test_stack.push(val2)
    test_stack.push(val3)
    assert test_stack.pop() == val3
    assert test_stack.pop() == val2
    assert test_stack.pop() == val1


@pytest.mark.parametrize('iterable, result', TEST_LEN)
def test_linked_list_len(iterable, result):
    """Push an iterable to the stack, and then test the size/len of the list."""
    from stack import Stack
    test_stack = Stack(iterable)
    assert len(test_stack) == result
