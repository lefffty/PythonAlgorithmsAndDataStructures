def bubble_sort(numbers: list):
    for i in range(0, len(numbers) - 1):
        for j in range(0, len(numbers) - 1):
            if numbers[j] >= numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


print(bubble_sort([1, 8, 6, 2, 6, 4, 0, 7, 5, 1, 3, 6, 4]))
