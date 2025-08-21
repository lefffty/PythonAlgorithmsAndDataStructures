from typing import List


def binary_search(sequence: List[int], target: int) -> bool:
    sequence.sort()
    if not sequence:
        return False
    lower = 0
    upper = len(sequence) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if sequence[mid] == target:
            return True
        elif sequence[mid] > target:
            upper = mid - 1
        else:
            lower = mid + 1
    return False


print(binary_search([4, 8, 7, 5, 1], 2))
print(binary_search([4, 8, 7, 5, 1], 5))
print(binary_search([4, 8, 7, 5, 1], 8))
print(binary_search([4, 8, 7, 5, 1], 1))
