from deck_sort import deck_sort

DECK = ['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K']


def test_deck_sort():
    """Test that deck_sort will properly sort a deck of cards"""
    assert deck_sort(DECK) == ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']