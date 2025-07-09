def insertion_sort(numbers: list):
    for i in range(0, len(numbers)):
        for k in range(i, 0, -1):
            if numbers[k] < numbers[k-1]:
                numbers[k], numbers[k-1] = numbers[k-1], numbers[k]
    return numbers


print(insertion_sort([2, 1, 3, 5, 6, 7, 3, 2, 8, 6, 4, 1, 1]))