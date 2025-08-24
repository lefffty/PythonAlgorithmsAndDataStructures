from collections.abc import Iterable


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = True


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.is_end_of_word = True

    def insert_many(self, words: Iterable[str]):
        for word in words:
            self.insert(word)

    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True


trie = Trie()
trie.insert_many(['factor', 'Benjamin', 'format', 'thread', 'tornado'])
