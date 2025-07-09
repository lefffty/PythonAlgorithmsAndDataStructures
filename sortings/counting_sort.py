def counting_sort(values: list, max_value: int, min_value: int):
    counters = {}
    result = []
    for num in range(min_value, max_value + 1):
        counters[num] = 0
    for value in values:
        counters[value] += 1
    for key in sorted(counters.keys()):
        while counters[key]:
            result.append(key)
            counters[key] -= 1
    return result


values = [1, 4, 2, 1, 2, 3, 4, 2, 3, 1, 4, 2, 4, 2]
print(counting_sort(values, max(values), min(values)))
