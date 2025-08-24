import abc


class DictInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, key):
        pass

    @abc.abstractmethod
    def find(self, key):
        pass

    @abc.abstractmethod
    def remove(self, key):
        pass

    @abc.abstractmethod
    def _hash_function(self, data):
        pass
