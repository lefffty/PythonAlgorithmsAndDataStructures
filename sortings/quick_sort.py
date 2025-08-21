from typing import List
import random


def quick_sort(iterable: List[int]) -> List[int]:
    size = len(iterable)
    if size <= 1:
        return iterable
    pivot = iterable[0]
    lower = [item for item in iterable[1:] if item < pivot]
    greater = [item for item in iterable[1:] if item > pivot]
    return quick_sort(lower) + [pivot] + quick_sort(greater)


SIZE = 100
LOWER_BOUND = 1
UPPER_BOUND = 100
iterable = [random.randint(1, 100) for _ in range(SIZE)]
print(quick_sort(iterable))
