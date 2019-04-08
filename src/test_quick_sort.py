"""Test that quick."""
import pytest
from random import randint
from quick_sort import quick_sort


to_sort = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
]


def test_quick_non_list_raises_error():
    """Non list raises error."""
    with pytest.raises(TypeError):
        quick_sort('You didn\'t say the magic word')


def test_quick_non_int_raises_error():
    """Non-int raises error."""
    with pytest.raises(ValueError):
        quick_sort([1, 2, 3, 4, 'monkies'])


@pytest.mark.parametrize('input, output', to_sort)
def test_quick_sort_returns_ordered_list(input, output):
    """Quick sort returns an ordered list."""
    assert quick_sort(input) == output


def test_quick_sort_sorts_random_list():
    """Quick sort returns an ordered list."""
    input = [randint(0, 250) for i in range(100)]
    output = sorted(input)
    assert quick_sort(input) == output
