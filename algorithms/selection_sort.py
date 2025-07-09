def selection_sort(numbers: list):
    for i in range(0, len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


print(selection_sort([9, 4, 8, 2, 4, 9, 6, 4, 7, 3, 2]))
