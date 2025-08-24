from __future__ import annotations
from collections.abc import Hashable
from typing import Iterable, List, Tuple
from dataclasses import dataclass

from interface import DictInterface
from utils import get_prime_number


prime_gen = iter(get_prime_number())


@dataclass
class Node:
    """Class for hash-table data structure
    """
    key: int
    value: int
    next: Node = None


class LinkedListHashTable(DictInterface):
    """
    Hash table with list method for collusion resolving
    """

    def __init__(
        self,
    ):
        """
        Class initializer

        Attributes
        ----------
        size_table :
            Current size of hash-table.

        values :
            Hash-table implementation of size <self.size_table>.
            Contains pairs <key, List[Node]>.

        size :
            Amount of keys in current hash-table
        """
        self.size_table = next(prime_gen)
        self.values: List[Node] = [None] * self.size_table
        self.size = 0

    def bulk(self, data: Iterable[Tuple[int, int]]) -> None:
        """Inserts pairs <int,int> into hash-table.

        Args:
            data (Iterable[Tuple[int, int]]): _description_

        Raises:
            ValueError: _description_
        """
        for key, value in data:
            if not isinstance(key, Hashable):
                raise ValueError
            self.insert(key, value)

    def insert(self, key: int, value: int):
        """Inserts pair <int, int>

        Args:
            key (_type_): _description_
            value (_type_): _description_

        Raises:
            KeyError: _description_
        """
        if not isinstance(key, Hashable):
            raise KeyError
        index = self._hash_function(key)

        if not self.values[index]:
            self.values[index] = Node(key, value)
            self.size += 1
        else:
            current = self.values[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.values[index]
            self.values[index] = new_node
            self.size += 1

        full_factor = self.get_full_factor()
        if full_factor > 0.75:
            self._rehashing()

    def get_full_factor(self):
        return sum(1 for value in self.values if value) / self.size_table

    def _rehashing(self):
        """Algorithm for rehashing when table becomes filled with values.
        """
        current_pairs = [pair for pair in self.values if pair]
        self.size_table = next(prime_gen)
        self.values = [None] * self.size_table
        for pair in current_pairs:
            self.insert(pair.key, pair.value)

    def remove(self, key) -> None:
        """Removes one pair <key, value>.

        Args:
            key (_type_): key value

        Raises:
            KeyError: if key isn`t present in the table
        """
        index = self._hash_function(key)

        previous = None
        current = self.values[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.values[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

        raise KeyError

    def find(self, key: int) -> int:
        """Searches for key in hash-table

        Args:
            key (int): key value

        Raises:
            KeyError: if key is not present in hash-table,
            function raises KeyError

        Returns:
            int: value associated with key
        """
        index = self._hash_function(key)

        current = self.values[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError

    def __contains__(self, key: int) -> bool:
        """Overriden built-in method. Check for key
        being present in hash-table.

        Args:
            key (int): key value

        Returns:
            bool: returns True if key is present, overwise returns False
        """
        try:
            self.find(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: int):
        """Gets value by key.

        Args:
            key (int): key value

        Raises:
            KeyError: if key is not present in hash-table,
            function raises KeyError

        Returns:
            int: value associated with key
        """
        value = self.find(key)
        return value

    def __setitem__(self, key: int, value: int):
        """Sets value for key

        Args:
            key (int): key
            value (int): value
        """
        self.insert(key, value)

    def __repr__(self) -> str:
        """Returns representation for instance

        Returns:
            str: representation
        """
        _repr = ''
        for index, current in enumerate(self.values):
            if self.values[index]:
                _repr += f'{index} -> [ '
                while current:
                    _repr += f'{current.value}, '
                    current = current.next
                _repr += ']\n'
        return _repr

    def _hash_function(self, key: int) -> int:
        """Hash function. Returns remainder of division of
        key by size if hash table.

        Args:
            key (int): key value

        Returns:
            int: hash function value
        """
        return key % self.size_table
