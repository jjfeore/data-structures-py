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
                if pos == 0:
                    break
                elif pos % 2 == 1:
                    parent = pos // 2
                else:
                    parent = (pos // 2) - 1

    def pop(self):
        """Remove the value that is at the top of the heap."""
        if not self.heap:
            return None
        top = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        pos = 0
        if len(self.heap) > 1:
            left = (pos * 2) + 1
            right = (pos * 2) + 2
            if left > len(self.heap) - 1:
                left = pos
            if right > len(self.heap) - 1:
                right = pos
            # import pdb; pdb.set_trace()
            while self.heap[left] < self.heap[pos] or self.heap[right] < self.heap[pos]:
                if self.heap[left] < self.heap[right]:
                    small = left
                else:
                    small = right
                tmp = self.heap[small]
                self.heap[small] = self.heap[pos]
                self.heap[pos] = tmp
                pos = small
                left = (pos * 2) + 1
                right = (pos * 2) + 2
                if left > len(self.heap) - 1:
                    left = pos
                if right > len(self.heap) - 1:
                    right = pos
        return top
