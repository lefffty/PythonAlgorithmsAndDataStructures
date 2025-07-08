import copy as cp
from typing import Literal
import sys


class OneWayListNode:
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


class TwoWayListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'Value: {self.value}'


class CyclicTwoWayLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def push(self, value):
        node = TwoWayListNode(value)
        if not self.__size:
            self.head = node
            self.tail = node
            self.__size += 1
            return self
        temp = self.tail
        self.tail = node
        self.tail.prev = temp
        self.tail.next = self.head
        temp.next = self.tail
        self.head.prev = self.tail
        return self

    def __repr__(self):
        visited = []
        temp = self.head
        result = '<--> '
        while temp:
            if temp in visited:
                break
            result += f'{temp.value} <--> '
            visited.append(temp)
            temp = temp.next
        return result


class TwoWayLinkedList:
    def __init__(self):
        """
        Конструктор двусвязного списка
        """
        self.head = None
        self.tail = None
        self.__size = 0

    def pushFront(self, value):
        """
        Добавление в конец
        """
        node = TwoWayListNode(value)
        if not self.__size:
            self.head = node
            self.tail = node
            self.__size += 1
            return self
        temp = self.head
        self.head = node
        self.head.prev, self.head.next = None, temp
        self.__size += 1
        return self

    def pushBack(self, value):
        """
        Добавление в начало
        """
        node = TwoWayListNode(value)
        if not self.__size:
            self.head = node
            self.tail = node
            self.__size += 1
            return self
        temp = self.tail
        self.tail = node
        temp.next = self.tail
        self.tail.prev, self.tail.next = temp, None
        self.__size += 1
        return self

    def popBack(self) -> int:
        """
        Удаление хвоста
        """
        temp = self.tail
        self.tail = temp.prev
        self.tail.next = None
        item = temp.value
        del temp
        self.__size -= 1
        return item

    def popFront(self):
        """
        Удаление вершины
        """
        temp = self.head
        self.head = temp.next
        self.head.prev = None
        item = temp.value
        del temp
        self.__size -= 1
        return item

    def popElement(self, value):
        """
        Удаление элемента по значению
        """
        temp = self.head
        while temp:
            if temp.value == value:
                match temp:
                    case self.head:
                        return self.popFront()
                    case self.tail:
                        return self.popBack()
                    case _:
                        temp.prev.next = temp.next
                        temp.next.prev = temp.prev
                        item = temp.value
                        del temp
                        self.__size -= 1
                        return item
            temp = temp.next
        return None

    def __sort(self, order=Literal["asc", "desc"]):
        pass

    # def insertNode(self, value):
    #     temp = self.tail if self.head.value < value else self.head
    #     operation_counter = 0
    #     while temp:
    #         if ''

    def __repr__(self) -> str:
        """
        Строковое представление списка
        """
        res = 'NULL <--> '
        temp = self.head
        while temp:
            res += f'{temp.value} <--> '
            temp = temp.next
        res += 'NULL'
        return res


class OneWayLinkedList:
    def __init__(self):
        """
        Конструктор
        """
        self.head = None
        self.tail = None
        self._size = 0

    def addElementFront(self, node: OneWayListNode):
        """
        Добавление элемента в начало связного списка
        """
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

    def addElementBack(self, node: OneWayListNode):
        """
        Добавление элемента в конец связного списка
        """
        if not self.size():
            self.head = node
            self.tail = node
            self._size += 1
            return self

        self.tail.next = node
        self.tail = node
        self._size += 1
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

    def __sort(self) -> None:
        """
        Сортировка элементов списка
        """
        temp = self.head
        for i in range(self.size()):
            for j in range(i+1, self.size() - 1):
                if temp.value > temp.next.value:
                    self.__swap(temp, temp.next)
                temp = temp.next

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
            arg = OneWayListNode(arg)
            self.addElementBack(arg)
        return self

    def merge(self, other_list):
        """
        Слияние двух списков
        """
        self.tail.next = other_list.head
        return self

    def reverse(self):
        """
        Реверсирование списка
        """
        pass

    def hasCycle(self):
        """
        Есть ли цикл в списке
        """
        pass


if __name__ == '__main__':
    ls = CyclicTwoWayLinkedList()
    ls.push(1).push(2).push(3).push(4).push(5).push(6)
    print(ls)
