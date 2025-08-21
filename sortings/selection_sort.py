from typing import List, Tuple
import random


def selection_sort(iterable: List[int]) -> Tuple[List[int], int]:
    arr = iterable.copy()
    size = len(iterable)
    if size <= 1:
        return arr, 0
    num_of_oper = 0
    for i in range(size - 1):
        min_index = i

        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            num_of_oper += 1

    return arr, num_of_oper


SIZE = 100
LOWER_BOUND = 1
UPPER_BOUND = 100
iterable = [random.randint(1, 100) for _ in range(SIZE)]
print(selection_sort(iterable))
