'''Binary Heap Data Structure.'''


class bi_heap:
    def __init__(self):
        self.heap = [0]
        self.currlen = 0

    def bubb_up(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                tmp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = tmp
            i = i // 2

    def push(self, j):
        self.heap.append(j)
        self.currlen = self.currlen + 1
        self.bubb_up(self.currlen)

    def bubb_dow(self, i):
        while (i * 2) <= self.currlen:
            mc = self.min_child(i)
            if self.heap[i] > self.heap[mc]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.currlen:
            return i * 2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def pop(self):
        ret_val = self.heap[1]
        self.heap[1] = self.heap[self.currlen]
        self.currlen = self.currlen - 1
        self.bubb_dow(1)
        return ret_val
