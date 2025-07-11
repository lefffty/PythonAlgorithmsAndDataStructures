from random import randint


List = list
Int = int
Bool = bool


def linear_search(numbers: List[Int], target: Int) -> Int:
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index
    return -1


def recursive_linear_search(numbers: List[Int], target: Int, index: Int):
    if index >= len(numbers):
        return -1
    elif numbers[index] == target:
        return index
    else:
        return recursive_linear_search(numbers, target, index + 1)


def binary_search(numbers: List[Int], target: Int) -> Int:
    numbers.sort()
    low = 0
    high = len(numbers) - 1
    while (low <= high):
        mid = (high + low) // 2
        mid_value = numbers[mid]
        if mid_value == target:
            return mid
        elif mid_value > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def recursive_binary_search(numbers: List[Int], target: Int, low: Int, high: Int):
    if low > high:
        return -1
    mid = (high + low) // 2
    mid_value = numbers[mid]
    if target == mid_value:
        return mid
    elif target < mid_value:
        return recursive_binary_search(numbers, target, low, mid - 1)
    else:
        return recursive_binary_search(numbers, target, mid + 1, high)


def binary_search_first(numbers: List[Int], target: Int) -> Int:
    index = binary_search(numbers, target)
    while (numbers[index] == target):
        index -= 1
        break
    return index


def interpolation_search(numbers: List[Int], target: Int) -> Int:
    numbers.sort()
    low = 0
    high = len(numbers) - 1
    while (low <= high):
        mid = low + (high - low) * (target -
                                    numbers[low]) // (numbers[high] - numbers[low])
        if target == numbers[mid]:
            return mid
        elif target < numbers[mid]:
            high = mid
        else:
            low = mid + 1
    return -1


def interpolation_search_first(numbers: List[Int], target: Int) -> Int:
    index = interpolation_search(numbers, target)
    while True:
        if (numbers[index] != target):
            break
        index -= 1
    return index


def recursive_interpolation_search(numbers: List[Int], target: Int, low: Int, high: Int):
    if low > high:
        return -1
    if low > high:
        return -1
    mid = low + (high - low) * (target -
                                numbers[low]) // (numbers[high] - numbers[low])
    mid_value = numbers[mid]
    if target == mid_value:
        return mid
    elif target < mid_value:
        return recursive_interpolation_search(numbers, target, low, mid - 1)
    else:
        return recursive_interpolation_search(numbers, target, mid + 1, high)


numbers = [randint(0, 25) for i in range(150)]
print(sorted(numbers))
print(sorted(numbers).index(2))
print(binary_search_first(numbers, 2))
