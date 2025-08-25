from typing import MutableMapping, List
from collections import deque


graph = {
    'A': ['B', 'C'],
    'B': ['E'],
    'C': ['D'],
    'E': ['F'],
    'F': ['C']
}


def breadth_first_search(graph: MutableMapping[str, List[str]], vertex: str):
    queue = deque([vertex])
    visited = []
    while queue:
        _vertex = queue.popleft()
        if _vertex not in visited:
            visited.append(_vertex)
        if _vertex in graph.keys():
            queue += graph[_vertex]
    return visited


def depth_first_search(graph: MutableMapping[str, List[str]], vertex: str):
    queue = deque([vertex])
    visited = []
    while queue:
        _vertex = queue.popleft()
        if _vertex not in visited:
            visited.append(_vertex)
        if _vertex in graph.keys():
            queue.extendleft(graph[_vertex])
    return visited
