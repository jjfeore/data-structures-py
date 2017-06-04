'''Binary Heap Data Structure.'''
from dll import DLinkedList


class bi_heap:
    def __init__(self):
        self.heap = [0]
        self.length = 0

    def bubb_up(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                tmp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = tmp
            i = i // 2

    def push(self):
        '''Remove the value that is at the end of the queue.'''
        return self.heap.push()

    def bubb_dow(self, i):
        while (i * 2) <= self.length:
            mc = self.min_child(i)
            if self.heap[i] > self.heap[mc]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.length:
            return i * 2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def pop(self):
        '''Remove the value that is at the end of the queue.'''
        return self.heap.pop()
