'''Binary Heap Data Structure.'''

class bi_heap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)

    def pop(self)