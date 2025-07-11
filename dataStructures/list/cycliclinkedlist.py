from .twowaylinkedlist import TwoWayListNode


class CyclicTwoWayLinkedList:
    def __init__(self):
        """
        Конструктор списка
        """
        self.head = None
        self.tail = None
        self.__size = 0

    def push(self, value):
        """
        Добавление в конец списка
        """
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
        """
        """
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
