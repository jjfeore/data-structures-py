"""This will sort a deck of cards"""
"""['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K']"""
"""['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']"""


def deck_sort(deck):
    """This will sort a random deck of cards"""
    sorted_deck = []
    idx = 0
    for card in deck:
        while True:
            try:
                sorted = get_value(sorted_deck[idx])
                tmp = get_value(card)
                if sorted >= tmp:
                    sorted_deck.insert(idx, card)
                    idx = 0
                    break
                else:
                    idx += 1
            except IndexError:
                sorted_deck.append(card)
                idx = 0
                break
    return sorted_deck


def get_value(card):
    if card == 'A':
        return 14
    elif card == 'T':
        return 10
    elif card == 'J':
        return 11
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    else:
        return int(card)