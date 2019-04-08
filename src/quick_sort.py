"""This is an implementation of quick_sort."""


def quick_sort(numbers):
    pivot = numbers[0]
    store_index = numbers.index(pivot) + 1
    for i in numbers[1:]:
        if i < pivot:
            new_nums = [pivot]
            check_list = list(numbers[store_index:])
            count = 0
            for number in check_list:
                count += 1
                thing = check_list[count]
                print(number, thing)
                if number < pivot:
                    number, check_list[store_index] = check_list[store_index],
                    number
                    store_index += 1
                print(new_nums, check_list)
    return new_nums


def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quick_sort_of(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_of(arr, low, pi-1)
        quick_sort_of(arr, pi+1, high)
