from typing import List


def linear_search(sequence: List[int], target: int) -> bool:
    if not sequence:
        return False
    elif len(sequence) == 1:
        return sequence[0] == target
    else:
        for item in sequence:
            if item == target:
                return True
        return False


print(linear_search([], 4))
print(linear_search([4, 3, 1, 7, 6, 5, 9], 0))
print(linear_search([4, 3, 1, 7, 6, 5, 9], 7))
