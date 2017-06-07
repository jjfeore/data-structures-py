"""Binary Heap Data Structure."""
import collections


class Biheap:
    """Instantiate a binary heap and its methods."""

    def __init__(self, iter=None):
        self.heap = []
        if isinstance(iter, collections.Iterable):
            for item in iter:
                self.push(item)

    def push(self, val):
        """Add a value to our heap."""
        self.heap.append(val)
        pos = len(self.heap) - 1
        if len(self.heap) > 1:
            if pos % 2 == 1:
                parent = pos // 2
            else:
                parent = (pos // 2) - 1
            while self.heap[parent] > self.heap[pos]:
                tmp = self.heap[parent]
                self.heap[parent] = self.heap[pos]
                self.heap[pos] = tmp
                pos = parent
                if pos % 2 == 1:
                    parent = pos // 2
                else:
                    parent = (pos // 2) - 1

    def pop(self):
        """Remove the value that is at the top of the heap."""
        top = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        pos = 0
        if len(self.heap) > 1:
            left = (pos * 2) + 1
            right = (pos * 2) + 2
            while self.heap[left] > self.heap[pos] or self.heap[right] > self.heap[pos]:
                if self.heap[left] > self.heap[pos]:
                    tmp = self.heap[left]
                    self.heap[left] = self.heap[pos]
                    self.heap[pos] = tmp
                    pos = left
                    left = (pos * 2) + 1
                    right = (pos * 2) + 2
                elif self.heap[right] > self.heap[pos]:
                    tmp = self.heap[right]
                    self.heap[right] = self.heap[pos]
                    self.heap[pos] = tmp
                    pos = right
                    left = (pos * 2) + 1
                    right = (pos * 2) + 2
        return top
