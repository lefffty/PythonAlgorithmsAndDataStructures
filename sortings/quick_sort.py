def quicksort(array: list):
    if len(array) < 2:
        return array
    pivot = array[0]
    less_numbers = [item for item in array if item < pivot]
    greater_numbers = [item for item in array if item > pivot]
    return quicksort(less_numbers) + pivot + quicksort(greater_numbers)


print(quicksort([10, 5, 2, 3]))
