class Heap:
    def __init__(self, values: list):
        self.__values = values
        self.makeheap()

    def makeheap(self):
        for i in range(len(self.__values)):
            index = i
            while (index != 0):
                parent = (index - 1) // 2
                if (self.__values[index] <= self.__values[parent]):
                    break
                temp = self.__values[index]
                self.__values[index] = self.__values[parent]
                self.__values[parent] = temp
                index = parent

    def removeTopItem(self, ind):
        result = self.__values[0]
        self.__values[0] = self.__values[ind]
        self.__values[ind] = result
        index = 0
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            print(
                f'Ind: {ind}, Left child: {left_child},'
                f' Right child: {right_child}'
            )
            print(f'Array: {self.__values}')
            if left_child > len(self.__values):
                left_child = index
            if right_child > len(self.__values):
                right_child = index
            if self.__values[index] >= self.__values[left_child] and self.__values[index] >= self.__values[right_child]:
                break
            swap_index = left_child if self.__values[left_child] > self.__values[right_child] else right_child
            temp = self.__values[index]
            self.__values[index] = self.__values[swap_index]
            self.__values[swap_index] = temp
            index = swap_index
        return result

    def heap_sort(self):
        for i in range(len(self.__values) - 1, 0, -1):
            self.removeTopItem(i)

    def getValues(self):
        return self.__values


heap = Heap([9, 4, 3, 8, 10, 2, 5])
print(heap.getValues())
heap.heap_sort()
print(heap.getValues())
