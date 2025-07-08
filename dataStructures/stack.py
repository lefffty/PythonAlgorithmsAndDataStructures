from list import OneWayListNode, OneWayLinkedList


class Stack:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, value: int):
        node = OneWayListNode(value)
        temp = self.head
        self.head = node
        if self.head.next:
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
