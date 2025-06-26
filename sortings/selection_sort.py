def findSmallestItem(array: list):
    smallest = array[0]
    smallestIndex = 0
    for index in range(len(array)):
        if array[index] < smallest:
            smallest = array[index]
            smallestIndex = index
    return smallestIndex


def selectionSort(array: list):
    resultArray = []
    for index in range(len(array)):
        smallestIndex = findSmallestItem(array)
        resultArray.append(array.pop(smallestIndex))
    return resultArray


print(selectionSort([4, 3, 1, 8, 6, 4, 6, 8, 0, 4, 2, 1,]))
