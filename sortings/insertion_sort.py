from typing import List, Tuple
import random


def insertion_sort(iterable: List[int]) -> Tuple[List[int], int]:
    arr = iterable.copy()
    size = len(iterable)

    if size <= 1:
        return arr, 0
    num_of_oper = 0

    for i in range(1, size):
        current = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            num_of_oper += 1
            j -= 1

        arr[j + 1] = current

    return arr, num_of_oper


_SIZE = 100
LOWER_BOUND = 1
UPPER_BOUND = 100
iterable = [random.randint(LOWER_BOUND, UPPER_BOUND) for _ in range(_SIZE)]
print(insertion_sort(iterable))
