"""A merge sort function."""
from insertion_sort import existing_set_insertion_sort as esis

from insertion_sort import insertion_sort


def merge2(numbers):
    """Merge sort, recursive."""
    if len(numbers) == 1:
        return numbers
    if len(numbers) == 2:
        if numbers[0] > numbers[1]:
            numbers[0], numbers[1] = numbers[1], numbers[0]
        return numbers
    midpnt = len(numbers) // 2
    left = merge2(numbers[:midpnt])
    right = merge2(numbers[midpnt:])

    output = []
    while left or right:
        if left and right and left[0] < right[0]:
            output.append(left.pop(0))
        elif left and right and left[0] >= right[0]:
            output.append(right.pop(0))
        elif left and not right:
            output.extend(left)
            break
        elif right and not left:
            output.extend(right)
            break

    return output


def merge_sort(numbers):
    """Sort a iterable of numbers into min first via merge sort non-recursively."""
    final = []
    compare = []
    temp = []
    hold_extra = []
    if len(numbers) == 1:
        return numbers
    elif len(numbers) == 2:
        if numbers[0] > numbers[1]:
            numbers[0], numbers[1] = numbers[1], numbers[0]
            return numbers

    elif len(numbers) == 3:
        return insertion_sort(numbers)
    if len(numbers) % 2 == 0:
        for i in range(0, len(numbers), 2):
            temp.append(numbers[i: i + 2])
        for pair in temp:
            if pair[0] > pair[1]:
                pair[0], pair[1] = pair[1], pair[0]
    else:
        for i in range(0, len(numbers) - 1, 2):
            temp.append(numbers[i: i + 2])
        for pair in temp:
            if pair[0] > pair[1]:
                pair[0], pair[1] = pair[1], pair[0]
        hold_extra.append(numbers[len(numbers) - 1])
    while 1:
        if final:
            if len(final) == 1:
                if hold_extra:
                    return esis(hold_extra, final[0])
                return final[0]
            temp = list(final)
        if len(temp) % 2 == 1:
            hold_extra.extend(temp[len(temp) - 1])
        final = []
        for i in range(0, len(temp) - 1, 2):
            t = 0
            k = 0
            while 1:
                if t >= len(temp[i]) and k >= len(temp[i + 1]):
                    final.append(compare)
                    compare = []
                    break
                elif t >= len(temp[i]):
                    compare.append(temp[i + 1][k])
                    k += 1
                elif k >= len(temp[i + 1]):
                    compare.append(temp[i][t])
                    t += 1
                elif temp[i][t] >= temp[i + 1][k]:
                    compare.append(temp[i + 1][k])
                    k += 1
                elif temp[i][t] <= temp[i + 1][k]:
                    compare.append(temp[i][t])
                    t += 1
