"""Test the dqueue.py module."""

import pytest


TEST_INSERT = [
    (1, 1),
    (800, 800),
    ('String', 'String'),
    ([5, 3, 17], [5, 3, 17])
]


TEST_INSERT_MULT = [
    (1, 2, 3),
    (800, 'String', 5),
    ('String', ['list'], 17),
    ([5, 3, 17], [5, 'list two'], ['another string'])
]


TEST_LEN = [
    ([1], 1),
    ((17, 5, 100), 3),
    ('String', 6),
    ([5, 3, 17], 3)
]


@pytest.fixture
def new_pri_que():
    """Init a new dqueue."""
    from priorityq import Priorityq
    return Priorityq()


@pytest.mark.parametrize('val1, val2, val3', TEST_INSERT_MULT)
def test_pri_que_insert_mult(val1, val2, val3, new_pri_que):
    """Append three values and check to see that they're in the Dqueue."""
    new_pri_que.insert(val1)
    new_pri_que.insert(val2)
    new_pri_que.insert(val3)
    assert new_pri_que.prq[0] == [val1]
    assert new_pri_que.prq[1] == [val2]
    assert new_pri_que.prq[2] == [val3]


# @pytest.mark.parametrize('val1, val2, val3', TEST_INSERT_MULT)
# def test_pri_que_pop(val1, val2, val3, new_pri_que):
#     """Append 3 values, check that pop gets the val at the end of the dque."""
#     new_pri_que.insert(val1)
#     new_pri_que.insert(val2)
#     new_pri_que.insert(val3)
#     assert new_pri_que.pop() == val3
#     assert new_pri_que.pop() == val2
#     assert new_pri_que.pop() == val1


@pytest.mark.parametrize('val1, val2, val3', TEST_INSERT_MULT)
def test_pri_que_peek(val1, val2, val3, new_pri_que):
    """Append 3 values and confirm that peek sees the end of the dque."""
    new_pri_que.insert(val1)
    new_pri_que.insert(val2)
    assert new_pri_que.peek() == val1
    new_pri_que.insert(val3)
    assert new_pri_que.peek() == val1
