import copy as cp
import sys
from typing import Annotated


class OneWayListNode:
    value: Annotated[int, 'значение, хранящееся в узле']

    def __init__(self, value: int):
        """
        Конструктор объекта узла
        """
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        """
        Строковое представление узла
        """
        return f'Value: {self.value}'


class Stack:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, value: int):
        node = OneWayListNode(value)
        temp = self.head
        self.head = node
        self.head.next = temp
        self._size += 1
        return self

    def pop(self) -> OneWayListNode:
        item = self.head
        if self.head.next:
            self.head = self.head.next
        self._size -= 1
        return item

    def peek(self) -> int:
        return self.head.value

    def isEmpty(self) -> int:
        return self._size == 0

    def __repr__(self):
        temp = self.head
        res = ''
        while temp:
            res += f'{temp.value} -> '
            temp = temp.next
        res += 'NULL'
        return res


class OneWayLinkedList:
    head: Annotated[OneWayListNode, 'Вершина списка']
    tail: Annotated[OneWayListNode, 'Конец списка']
    _size: Annotated[int, 'Длина списка']

    def __init__(self):
        """
        Конструктор
        """
        self.head = None  # вершина списка
        self.tail = None
        self._size = 0

    def pushFront(self, value: int):
        """
        Добавление элемента в начало связного списка
        """
        node = OneWayListNode(value)
        if not self.size():
            self.head = node
            self.tail = node
            self._size = 1
            return self
        temp = self.head
        self.head = node
        self.head.next = temp
        self._size += 1
        return self

    def pushBack(self, value: int):
        """
        Добавление элемента в конец связного списка
        """
        node = OneWayListNode(value)
        if not self.size():
            self.head = node
            self.tail = node
            self._size += 1
            return self
        self.tail.next = node
        self.tail = node
        self._size += 1
        return self

    def reverse(self):
        """
        Реверсирование списка
        """
        stack = Stack()
        temp = self.head
        while temp:
            stack.push(temp.value)
            temp = temp.next
        temp = self.head
        while temp:
            value = stack.pop().value
            temp.value = value
            temp = temp.next
        return self

    def size(self) -> int:
        """
        Размер списка
        """
        return self._size

    def pop(self) -> OneWayListNode:
        """
        Удаление первого элемента списка
        """
        temp = self.head
        self.head = temp.next
        self._size -= 1
        return temp

    def __swap(
        self,
        first_node: OneWayListNode,
        second_node: OneWayListNode
    ) -> None:
        """
        Поменять местами два элемента
        """
        first_node.value, second_node.value = (
            second_node.value,
            first_node.value
        )

    def isSorted(self) -> bool:
        """
        Отсортирован ли список
        """
        temp = self.head
        while temp.next:
            if temp.value > temp.next.value:
                return False
            temp = temp.next
        return True

    def sort(self) -> None:
        """
        Сортировка элементов списка
        """
        temp = self.head
        for i in range(self.size()):
            for j in range(i, self.size() - 1):
                print(j)
                if temp.value > temp.next.value:
                    tmp = temp.value
                    temp.value = temp.next.value
                    temp.next.value = tmp
                temp = temp.next
                print(temp)

    def copy(self):
        """
        Копирование значений списка в другой список
        """
        new_list = OneWayLinkedList()
        temp = self.head
        while temp:
            new_list.addElementBack(cp.copy(temp))
            temp = temp.next
        return new_list

    def __repr__(self) -> str:
        """
        Строковое представление списка
        """
        res = ''
        temp = self.head
        while temp:
            res += f'{temp.value} -> '
            temp = temp.next
        res += 'NULL'
        return res

    def find(self, value) -> bool:
        """
        Поиск элемента в списке
        """
        if not self._size:
            return False
        temp = self.head
        while temp:
            if temp.value == value:
                return True
            temp = temp.next
        return False

    def findMax(self):
        """
        Поиск максимального элемента в списке
        """
        if not self._size:
            return None
        temp = self.head
        target = -sys.maxsize - 1
        while temp:
            if temp.value > target:
                target = temp.value
            temp = temp.next
        return target

    def findMin(self):
        """
        Поиск минимального элемента в списке
        """
        if not self._size:
            return None
        temp = self.head
        target = sys.maxsize - 1
        while temp:
            if temp.value < target:
                target = temp.value
            temp = temp.next
        return target

    def extend(self, *args):
        """
        Расширение списка множеством значений
        """
        for arg in args:
            node = OneWayListNode(arg)
            self.addElementBack(node)
        return self

    def merge(self, other_list):
        """
        Слияние двух списков
        """
        self.tail.next = other_list.head
        return self

    def hasCycle(self):
        """
        Есть ли цикл в списке
        """
        pass


if __name__ == '__main__':
    ls = OneWayLinkedList()
    ls.pushFront(1).pushFront(2).pushFront(3)
    ls.sort()
    print(ls)
