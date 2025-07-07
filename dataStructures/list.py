class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f'Value: {self.value}'


class OneWayLinkedList:
    def __init__(self):
        """
        Конструктор
        """
        self.head = None
        self.tail = None
        self._size = 0

    def addElementFront(self, node: ListNode):
        """
        Добавление элемента в начало связного списка
        """
        if not self.size():  # если список пуст - инициализируем первый элемент списка
            self.head = node
            self.tail = node
            self._size = 1
            return self

        temp = self.head
        self.head = node
        self.head.next = temp
        self._size += 1
        return self

    def addElementBack(self, node: ListNode):
        """
        Добавление элемента в конец связного списка
        """
        if not self.size():  # если список пуст - инициализируем первый элемент списка
            self.head = node
            self.tail = node
            self._size += 1
            return self

        self.tail.next = node
        self.tail = node
        self._size += 1
        return self

    def size(self,) -> int:
        """
        Размер списка
        """
        return self._size

    def pop(self,) -> ListNode:
        """
        Удаление первого элемента списка
        """
        temp = self.head
        self.head = temp.next
        self._size -= 1
        return temp

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


if __name__ == '__main__':
    ls = OneWayLinkedList()
    ls.addElementBack(ListNode(1)).addElementBack(
        ListNode(2)).addElementBack(ListNode(3)).addElementBack(
        ListNode(4)).addElementBack(ListNode(5))
    ls.addElementFront(ListNode(0)).addElementFront(ListNode(-1))
    print(ls, ls.size())
    node = ls.pop()
    print(node)
    print(ls, ls.size())
