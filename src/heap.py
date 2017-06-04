'''Binary Heap Data Structure.'''


class Bi_heap:
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

    def insert(self, j):
        self.heap.append(j)
        self.currlen = self.currlen + 1
        self.percUp(self.currlen)

    def bubb_dow(self, i):
        while (i * 2) <= self.currlen:
            mc = self.minChild(i)
            if self.heap[i] > self.heap[mc]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currlen:
            return i * 2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heap[1]
        self.heap[1] = self.heap[self.currlen]
        self.currlen = self.currlen - 1
        self.heap.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currlen = len(alist)
        self.heap = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())