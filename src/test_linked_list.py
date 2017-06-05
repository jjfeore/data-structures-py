"""Test the linked_list.py module."""


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
    ([5, 3, 17], [5, 3, 17]),
    ('monkies', 'monkies')
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
    ([1, 2, 3, 4], 4),
    ([5, 3, 17], 3)
]


TEST_REM = [
    ([1, 2, 3, 4, 5], 4, [1, 2, 3, 5]),
    ((17, 5, 100, 700, 2), 2, (17, 5, 100, 700)),
    ('String', 'r', 'Sting'),
    ([5, 3, 17], 3, [5, 17])
]


TEST_DISP = [
    ([1], '(1)'),
    ((17, 5, 100), '(100, 5, 17)'),
    ('Sea', '(a, e, S)'),
    ([5, 3, 17], '(17, 3, 5)')
]


@pytest.fixture
def new_empty_list():
    """Make a new empty list."""
    from linked_list import LinkedList
    return LinkedList()


def test_linked_list_head(new_empty_list):
    """Test our linked list head."""
    assert hasattr(new_empty_list, 'head')


def test_linked_list_none():
    """When a new list is created with no iterable, head should be None."""
    from linked_list import LinkedList
    test_list = LinkedList()
    assert test_list.head is None


@pytest.mark.parametrize('iterable, result', TEST_ITER)
def test_linked_list_iterable(iterable, result):
    """When a new list is created with an iterable, head should be last element of the iterable."""
    from linked_list import LinkedList
    test_list = LinkedList(iterable)
    assert test_list.head.val == result


@pytest.mark.parametrize('val', TEST_PUSH)
def test_linked_list_push(val):
    """When a value is pushed to a linked list, the head value should equal that value."""
    from linked_list import LinkedList
    test_list = LinkedList()
    test_list.push(val)
    assert test_list.head.val == val


@pytest.mark.parametrize('val1, val2, val3', TEST_PUSH_MULT)
def test_linked_list_push_mult(val1, val2, val3):
    """Push three values and check to see that they're in the list."""
    from linked_list import LinkedList
    test_list = LinkedList()
    test_list.push(val1)
    test_list.push(val2)
    test_list.push(val3)
    assert test_list.head.val == val3
    assert test_list.head.next.val == val2
    assert test_list.head.next.next.val == val1


@pytest.mark.parametrize('val1, val2, val3', TEST_PUSH_MULT)
def test_linked_list_pop(val1, val2, val3):
    """Push three values into a list, pop them and check the values."""
    from linked_list import LinkedList
    test_list = LinkedList()
    test_list.push(val1)
    test_list.push(val2)
    test_list.push(val3)
    assert test_list.pop() == val3
    assert test_list.pop() == val2
    assert test_list.pop() == val1


def test_linked_list_pop_empty():
    """Create an empty DLL and attempt to pop value."""
    from linked_list import LinkedList
    test_list = LinkedList()
    with pytest.raises(IndexError):
        test_list.pop()


@pytest.mark.parametrize('iterable, result', TEST_LEN)
def test_linked_list_len(iterable, result):
    """Push an iterable to the list, and then test the size/len of the list."""
    from linked_list import LinkedList
    test_list = LinkedList(iterable)
    assert test_list.size() == result
    assert len(test_list) == result


def test_linked_list_search():
    """Create a new linked list, search it, and confirm we receive the right values."""
    from linked_list import LinkedList
    test_list = LinkedList([17, 3, 5, 19, 8])
    empty_list = LinkedList()
    assert test_list.search(5) is test_list.head.next.next
    assert test_list.search(19) is test_list.head.next
    assert test_list.search(3) is test_list.head.next.next.next
    assert test_list.search(17) is test_list.head.next.next.next.next
    assert empty_list.search(100) is None
    assert test_list.search(100) is None


@pytest.mark.parametrize('iter1, search, result', TEST_REM)
def test_linked_list_remove(iter1, search, result):
    """Create a linked list, remove nodes from it, and make sure it removes the node."""
    from linked_list import LinkedList
    test_list = LinkedList(iter1)
    test_list.remove(test_list.search(search))
    res_list = LinkedList(result)
    curr = test_list.head
    res_curr = res_list.head
    while curr:
        assert curr.val == res_curr.val
        curr = curr.next
        res_curr = res_curr.next


def test_linked_list_remove_empty():
    """Create an empty link list and attempt to remove node."""
    from linked_list import LinkedList
    from linked_list import Node
    test_list = LinkedList()
    with pytest.raises(IndexError):
        test_list.remove(Node(5, None))


def test_linked_list_remove_invalid():
    """Create an empty link list and attempt to remove node."""
    from linked_list import LinkedList
    from linked_list import Node
    test_list = LinkedList()
    test_list.push(7)
    with pytest.raises(IndexError):
        test_list.remove(Node(5, None))


@pytest.mark.parametrize('iterable, result', TEST_DISP)
def test_linked_list_display(iterable, result):
    """Create a list, display it, and check the return."""
    from linked_list import LinkedList
    test_list = LinkedList(iterable)
    assert test_list.display() == result


def test_linked_list_display_empty():
    """Create a list, display it, and check the return."""
    from linked_list import LinkedList
    test_list = LinkedList()
    assert test_list.display() == '()'
