from itertools import chain
import numpy as np

thing = [i for i in np.random.randint(1, 101, 100)]


def radix(set, curr_idx=0):
    bucket = [[] for _ in range(10)]
    place = curr_idx
    for number in set:
        try:
            value = int(str(number)[:: - 1][place])
            bucket[value].append(number)
        except:
            bucket[0].append(number)
    if len(bucket[0]) == len(set):
        return bucket[0]
    return radix(list(chain.from_iterable(bucket)), place + 1)
