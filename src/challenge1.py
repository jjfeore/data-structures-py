"""Code Challenge 1."""


def check_for_loop(the_list):
    """Check for a cyclical linked list."""
    curr = the_list.head
    store_nodes = []
    while curr:
        if curr.next in store_nodes:
            return True
        store_nodes.append(curr.next)
        curr = curr.next
    return False
