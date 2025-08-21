from typing import List
import random


def index_function(_min, _max, n_buckets, value):
    return int((n_buckets * (value - _min))/(_max - _min + 1))


def bucket_sort(sequence: List[int], n_buckets: int):
    _min = min(sequence)
    _max = max(sequence)
    if _min == _max:
        return
    buckets: List[List[int]] = []
    for i in range(n_buckets):
        buckets.append([])
    for item in sequence:
        index = index_function(_min, _max, n_buckets, item)
        buckets[index].append(item)
    for bucket in buckets:
        if len(bucket) <= 32:
            bucket.sort()
        else:
            bucket_sort(bucket, n_buckets)
    index = 0
    for bucket in buckets:
        for item in bucket:
            sequence[index] = item
            index += 1
    return sequence


sequence = [random.randint(1, 18) for _ in range(100)]
n_buckets = 5
print(bucket_sort(sequence, n_buckets))
