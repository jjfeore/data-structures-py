"""Test the challenge1.py module."""


import pytest


def test_challenge():
    """."""
    from linked_list import LinkedList
    from challenge1 import check_for_loop
    the_list = LinkedList()
    the_list.push(3)
    the_list.push('hello')
    the_list.push(5)
    the_list.push(6)
    the_list.head.next.next.next = the_list.head.next
    assert check_for_loop(the_list) == True



def test_challenge_2():
    """."""
    from linked_list import LinkedList
    from challenge1 import check_for_loop
    the_list = LinkedList()
    the_list.push(3)
    the_list.push('hello')
    the_list.push(5)
    the_list.push(6)
    assert check_for_loop(the_list) == False
