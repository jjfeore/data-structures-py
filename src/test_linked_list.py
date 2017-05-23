"""Test the linked_list.py module."""


import pytest


TEST_DISPLAY = [
    (3, '(3)'),
    (None, ''),
    ('List can take a string too!', '(List can take a string too!)'),
    ([5, 3, 17], '(17) -> (3) -> (5)')
]


@pytest.mark.parametrize('list, result', TEST_DISPLAY)
def test_display(list, result):
    """Initialize a list, print it, and confirm that the result matches."""
    from linked_list import LinkedList
    assert LinkedList(list).display() == result
