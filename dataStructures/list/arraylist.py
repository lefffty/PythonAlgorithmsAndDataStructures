from abc import ABCMeta, abstractmethod
from reprlib import repr
from time import sleep


class List(metaclass=ABCMeta):
    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def remove(self, index) -> int:
        pass

    @abstractmethod
    def get(self, index: int) -> int:
        pass

    @abstractmethod
    def add(self, data: int, index: int) -> None:
        pass


class ArrayList(List):
    def __init__(self):
        self.array = None
        self._size = 0
        self._capacity = 0

    def size(self):
        return self._size

    def add(self, data: int, index: int):
        if index > self._size + 1:
            raise ValueError
        self.ensure_capacity(self._size + 1)
        for i in reversed(range((index + 1), self._size + 1)):
            self.array[i] = self.array[i - 1]
        self.array[index] = data
        self._size += 1

    def copy(self, new_array):
        for index in range(self._size):
            new_array[index] = self.array[index]

    def ensure_capacity(self, new_size: int):
        if self._capacity < new_size:
            self._capacity = new_size * 2
            new_array = self.allocate_array(self._capacity)
            self.copy(new_array)
            self.array = new_array

    def remove(self, index):
        if index > self._size or index < 0:
            raise ValueError
        for i in range(index + 1, self._size + 1):
            self.array[i - 1] = self.array[i]
        self._size -= 1

    def get(self, index):
        return self.array[index]

    def allocate_array(self, size: int):
        return [None] * size

    def is_empty(self) -> bool:
        return self._size > 0

    def __repr__(self):
        return f'ArrayList({repr(self.array)})'
