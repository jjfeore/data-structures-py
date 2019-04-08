"""Testing that merge."""
import pytest
from random import randint
from merge_sort import merge2


to_sort = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
]


def test_merge_non_list_raises_error():
    """Raises error for e-merge-ncy."""
    with pytest.raises(AttributeError):
        merge2('You didn\'t say the magic word!')


def test_merge_non_int_raises_error():
    """Raises error for non-int."""
    with pytest.raises(TypeError):
        merge2([3, 4, 5, 'monkies'])


@pytest.mark.parametrize('input, output', to_sort)
def test_merge_sort_returns_ordered_list(input, output):
    """Merge sort returns an ordered list."""
    assert merge2(input) == output


def test_mergemerge2_sort_sorts_random_list():
    """Returns orderedddddd list."""
    input = [randint(0, 250) for i in range(100)]
    output = sorted(input)
    assert merge2(input) == output
