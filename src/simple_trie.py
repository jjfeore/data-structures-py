"""Makes a trie tree auto complete"""


end = '$'


def make_trie(*words):
    """Makes the trie tree."""

    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[end] = end
    return root
