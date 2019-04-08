def merge_sort(numbers):
    """Sort a iterable of numbers into min first via merge sort."""
    final = []
    compare = []
    temp = []
    if len(numbers) == 1:
        return numbers
    elif len(numbers) == 2:
        if numbers[0] > numbers[1]:
            numbers[0], numbers[1] = numbers[1], numbers[0]
            return numbers
    elif len(numbers) == 3:
        
    elif len(numbers) % 2 == 0:
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
        temp[0].append(numbers[len(numbers) - 1])
    while 1:
        if final:
            if len(final) == 1:
                return final[0]
            temp = list(final)
        print(temp)
        final = []
        if len(temp) % 2 != 0:
            temp[0].extend(temp[len(temp) - 1])
        for i in range(0, len(temp) - 1, 2):
            t = 0
            k = 0
            while 1:
                # import pdb; pdb.set_trace()
                if t >= len(temp[i]) and k >= len(temp[i + 1]):
                    if len(temp) % 2 != 0:
                        num = round(len(compare) / 2)
                        ss = compare[:num]
                        for i in range(0, len(ss) - 1, 2):
                            if ss[i] > ss[i + 1]:
                                ss[i], ss[i + 1] = ss[i + 1], ss[i]
                        final.append(ss)
                        ss = compare[num:]
                        for i in range(0, len(ss) - 1, 2):
                            if ss[i] > ss[i + 1]:
                                ss[i], ss[i + 1] = ss[i + 1], ss[i]
                        final.append(ss)
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
