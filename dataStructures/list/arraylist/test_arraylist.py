from arraylist import ArrayList


def test_vector_initialisation():
    vector = ArrayList()
    assert vector


def test_vector_add():
    vector = ArrayList()
    vector.add(1, 0)
    assert vector.array == [1, None]
    vector.add(2, 1)
    assert vector.array == [1, 2]
    vector.add(3, 2)
    assert vector.array == [1, 2, 3, None, None, None]


def test_vector_remove():
    vector = ArrayList()
    vector.add(1, 0)
    vector.add(2, 1)
    vector.remove(0)
    assert vector.array == [2, None]


def test_vector_get():
    vector = ArrayList()
    vector.add(1, 0)
    vector.add(2, 1)
    vector.add(3, 2)
    assert vector.get(0) == 1
    assert vector.get(1) == 2
    assert vector.get(2) == 3


def test_vector_ensure_capacity():
    vector = ArrayList()
    vector.add(1, 0)
    assert vector._capacity == 2
    vector.add(2, 1)
    vector.add(3, 2)
    assert vector._capacity == 6


def test_vector_size():
    vector = ArrayList()
    vector.add(1, 0)
    vector.add(2, 1)
    assert vector.size() == 2


def test_vector_is_empty():
    vector = ArrayList()
    assert vector.is_empty() is False
    vector.add(0, 1)
    assert vector.is_empty() is True
