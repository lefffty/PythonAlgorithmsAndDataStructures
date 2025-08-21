from typing import Tuple, List
import random


def bubble_sort(iterable: list) -> Tuple[List[int], int]:
    array = iterable.copy()
    size = len(array)
    if size <= 1:
        return array, 0
    num_of_oper = 0
    swapped = True
    for i in range(size - 1):
        if not swapped:
            break

        swapped = False
        for j in range(size - 1 - i):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j+1], array[j]
                num_of_oper += 1
                swapped = True
    return array, num_of_oper


iterable = [random.randint(1, 100) for _ in range(100)]
print(bubble_sort(iterable))
