from collections import deque


graph = {}
graph["вы"] = ["Алиса", "Боб", "Клэр"]
graph["Боб"] = ["Анудж", "Пегги"]
graph["Алиса"] = ["Пегги"]
graph["Клэр"] = ["Том", "Джонни"]
graph["Анудж"] = []
graph["Пегги"] = []
graph["Том"] = []
graph["Джонни"] = []


def is_ahugzh(person):
    return person[-1] == 'и'


def breadth_first_search(graph, name):
    search_deque = deque()
    search_deque += graph[name]
    searched = []
    while search_deque:
        person = search_deque.popleft()
        if person not in searched:
            if is_ahugzh(person):
                return 'Продавец манго: ' + person
            else:
                search_deque += graph[person]
                searched.append(person)
    return False


print(breadth_first_search(graph, 'вы'))
