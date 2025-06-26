import random


LENGTH = 100
MIN_VALUE = 1
MAX_VALUE = 50

numbers = [random.randint(MIN_VALUE, MAX_VALUE) for index in range(LENGTH)]
numbers.sort()
numbers = list(set(numbers))
print(numbers)


def binary_search(lst: list, item: int):
    low = 0
    high = len(lst) - 1
    iteration_counter = 1
    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        print(f'LOW= {low}, HIGH= {high}, ITERATION= {iteration_counter}')
        iteration_counter += 1
        if guess == item:
            return mid
        if item < guess:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(binary_search(numbers, 4))
print(binary_search(numbers, 20))
print(binary_search(numbers, 31))
