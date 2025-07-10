List = list
Int = int
Bool = bool


def linear_search(numbers: List[Int], target: Int) -> Bool:
    for index in range(len(numbers)):
        if numbers[index] == target:
            return True
    return False


def binary_search(numbers: List[Int], target: Int) -> Bool:
    numbers.sort()
    low = 0
    high = len(numbers) - 1
    while (low <= high):
        mid = (high + low) // 2
        print(mid)
        mid_value = numbers[mid]
        if mid_value == target:
            return True
        elif mid_value > target:
            high = mid - 1
        else:
            low = mid + 1
    return False


def interpolation_search(numbers: List[Int], target: Int) -> Bool:
    numbers.sort()
    low = 0
    high = len(numbers) - 1
    while (low <= high):
        mid = low + (high - low) * (target -
                                    numbers[low]) // (numbers[high] - numbers[low])
        print(mid)
        if target == numbers[mid]:
            return True
        elif target < numbers[mid]:
            high = mid
        else:
            low = mid + 1
    return False


numbers = [3, 4, 1, 10, 5, 7, 8, 6, 0, 2, 11, 15, 18]
print(numbers)
print(linear_search(numbers, 5))
print(binary_search(numbers, 5))
print(interpolation_search(numbers, 5))
