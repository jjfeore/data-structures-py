"""Priority Queue Data Structure."""


class Priorityq:
    def __init__(self):
        self.prq = []

    def insert(self, val, pri=0):
        """Add a value to our priority queue that has a priority."""
        self.prq.append([val, pri])
        pos = len(self.prq) - 1
        if len(self.prq) > 1 and pri > 0:
            if pos % 2 == 1:
                parent = pos // 2
            else:
                parent = (pos // 2) - 1
            while self.prq[parent][1] < self.prq[pos][1]:
                tmp = self.prq[parent]
                self.prq[parent] = self.prq[pos]
                self.prq[pos] = tmp
                pos = parent
                if pos % 2 == 1:
                    parent = pos // 2
                else:
                    parent = (pos // 2) - 1

    def pop(self):
        """Remove the value that is at the top of the prq."""
        top = self.prq[0][0]
        self.prq[0] = self.prq[-1]
        del self.prq[-1]
        pos = 0
        if len(self.prq) > 1:
            left = (pos * 2) + 1
            right = (pos * 2) + 2
            while self.prq[left][1] < self.prq[pos][1] or self.prq[right][1] < self.prq[pos][1]:
                if self.prq[left][1] < self.prq[pos][1]:
                    tmp = self.prq[left]
                    self.prq[left] = self.prq[pos]
                    self.prq[pos] = tmp
                    pos = left
                    left = (pos * 2) + 1
                    right = (pos * 2) + 2
                elif self.prq[right][1] < self.prq[pos][1]:
                    tmp = self.prq[right]
                    self.prq[right] = self.prq[pos]
                    self.prq[pos] = tmp
                    pos = right
                    left = (pos * 2) + 1
                    right = (pos * 2) + 2
        return top

    def peek(self):
        return self.prq[0][0]
