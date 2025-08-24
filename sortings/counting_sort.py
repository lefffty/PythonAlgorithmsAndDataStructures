from typing import List, Tuple
from collections import defaultdict
import random


def counting_sort(iterable: List[int]) -> List[int]:
    counters: defaultdict[int, int] = defaultdict(int)
    result = []
    for item in iterable:
        counters[item] += 1
    for key in sorted(counters):
        while counters[key]:
            result.append(key)
            counters[key] -= 1
    return result


def optimized_counting_sort(iterable: List[int]) -> Tuple[List[int], int]:
    if not iterable:
        return [], 0

    min_val = min(iterable)
    max_val = max(iterable)
    range_size = max_val - min_val + 1

    if range_size > 10 ** 5:
        raise ValueError

    count = [0] * range_size
    num_of_oper = 0

    for num in iterable:
        count[num - min_val] += 1
        num_of_oper += 1

    result = []
    for i in range(range_size):
        result.extend([i + min_val] * count[i])
        num_of_oper += count[i]

    return result, num_of_oper


SIZE = 100
LOWER_BOUND = 1
UPPER_BOUND = 10
iterable = [random.randint(LOWER_BOUND, UPPER_BOUND - 1) for _ in range(SIZE)]
print(optimized_counting_sort(iterable))
