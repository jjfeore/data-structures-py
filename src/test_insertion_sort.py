"""Test for the insertion sort."""
from insertion_sort import insertion_sort
import random


def test_insertion_sort():
    """Test that any given numerical iterable is returned as a min first list."""
    assert insertion_sort(random.sample(range(100), 100)) == list(range(100))
    assert insertion_sort(random.sample(range(100), 100)) == list(range(100))
    assert insertion_sort(random.sample(range(100), 100)) == list(range(100))
    assert insertion_sort(random.sample(range(100), 100)) == list(range(100))
    assert insertion_sort(random.sample(range(100), 100)) == list(range(100))
