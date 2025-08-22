import abc
import reprlib


class Heap(metaclass=abc.ABCMeta):
    def __init__(self):
        """
        Инициализатор кучи
        """
        self.heap = []

    def parent(self, index) -> int:
        """
        Индекс родительского элемента для данного
        """
        return (index - 1) // 2

    def left_child(self, index) -> int:
        """
        Индекс левого потомка данного узла
        """
        return 2 * index + 1

    def right_child(self, index) -> int:
        """
        Индекс правого потомка данного узла
        """
        return 2 * index + 2

    def insert(self, value):
        """
        Вставка элемента в кучу
        """
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    @abc.abstractmethod
    def _sift_up(self, index):
        """
        Отсеивание элемента
        """
        pass

    @abc.abstractmethod
    def _sift_down(self, index):
        """
        Просеивание элемента
        """
        pass

    def _extract_root(self) -> float:
        """
        Получение корня кучи
        """
        if not self.heap:
            raise IndexError
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root

    def __repr__(self):
        """
        Строковое представление кучи
        """
        return f'{self.__class__.__name__}({reprlib.repr(self.heap)})'


class BinaryMaxHeap(Heap):
    def _sift_up(self, index):
        while index != 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[index], self.heap[self.parent(
                index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def _sift_down(self, index):
        max_index = index
        left_index = self.left_child(index)
        right_index = self.right_child(index)
        size = len(self.heap)
        if left_index < size and self.heap[left_index] > self.heap[max_index]:
            max_index = left_index
        if right_index < size and self.heap[right_index] > self.heap[max_index]:
            max_index = right_index
        if index != max_index:
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            self._sift_down(max_index)


class BinaryMinHeap(Heap):
    def _sift_up(self, index):
        while index != 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[index], self.heap[self.parent(
                index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def _sift_down(self, index):
        lowest = index
        left_child = self.left_child(index)
        right_child = self.right_child(index)
        size = len(self.heap)
        if left_child < size and self.heap[left_child] < self.heap[lowest]:
            lowest = left_child
        if right_child < size and self.heap[right_child] < self.heap[lowest]:
            lowest = right_child
        if lowest != index:
            self.heap[index], self.heap[lowest] = self.heap[lowest], self.heap[index]
            self._sift_down(lowest)


items = [1, 3, 7, 9, 4, 2, 5]
max_heap = BinaryMaxHeap()
for item in items:
    max_heap.insert(item)
print(max_heap)
min_heap = BinaryMinHeap()
for item in items:
    min_heap.insert(item)
print(min_heap)
