from typing import Literal


class TwoWayListNode:
    def __init__(self, value: int):
        """
        Конструктор объекта узла
        """
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        """
        Строковое представление узла
        """
        return f'Value: {self.value}'


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

    def isSorted(self) -> bool:
        """
        Проверка на отсортированность списка
        """
        temp = self.head
        while temp:
            if temp.value > temp.next.value:
                return False
            temp = temp.next
        return True

    def __sort(self, order=Literal["asc", "desc"]):
        """
        """
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
