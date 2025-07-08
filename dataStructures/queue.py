class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        """
        Конструктор
        """
        self.__head = None
        self.__tail = None
        self.__size = 0

    def size(self) -> int:
        """
        Длина очереди
        """
        return self.__size

    def enqueue(self, value):
        """
        Добавить элемент в очереди
        """
        node = Node(value)
        if self.isEmpty():
            self.__head = node
            self.__tail = node
            self.__size += 1
            return self
        temp = self.__tail
        self.__tail = node
        self.__tail.prev = temp
        temp.next = self.__tail
        self.__size += 1
        return self

    def dequeue(self) -> Node:
        """
        Удалить элемент из очереди
        """
        item = self.__head
        self.__head = self.__head.next
        self.__size -= 1
        return item

    def isEmpty(self) -> bool:
        """
        Пустой ли список
        """
        return self.__size == 0

    def __repr__(self):
        temp = self.__head
        res = 'NULL -> '
        while temp:
            res += f'{temp.value} -> '
            temp = temp.next
        res += 'NULL'
        return res


class Deque:
    def __init__(self):
        pass


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.dequeue()
    q.dequeue()
    print(q)

