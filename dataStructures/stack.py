from list import OneWayListNode, OneWayLinkedList


class Stack(OneWayLinkedList):
    def __init__(self):
        super().__init__()

    def push(self, value: int):
        node = OneWayListNode(value)
        temp = self.head
        self.head = node
        self.head.next = temp
        self._size += 1
        return self

    def pop(self) -> OneWayListNode:
        item = self.head
        self.head = self.head.next
        self._size -= 1
        return item

    def peek(self) -> int:
        return self.head.value

    def isEmpty(self) -> int:
        return self._size == 0
