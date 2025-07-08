import copy


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

    def addElementBack(self, node: OneWayListNode):
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
            new_list.addElementBack(copy.copy(temp))
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


if __name__ == '__main__':
    ls = OneWayLinkedList()
    ls.addElementBack(OneWayListNode(1)).addElementBack(
        OneWayListNode(2)).addElementBack(OneWayListNode(3)).addElementBack(
        OneWayListNode(4)).addElementBack(OneWayListNode(5))
    ls.addElementFront(OneWayListNode(0)).addElementFront(
        OneWayListNode(-1)).addElementFront(OneWayListNode(-2))
    print(ls, ls.size())
    new_ls = ls.copy()
    new_ls.pop()
    new_ls.pop()
    print(new_ls, new_ls.size())
