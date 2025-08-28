from typing import MutableMapping, List, Tuple, Union
from collections import namedtuple, defaultdict
from dataStructures.advanced.djs import DisjointSet
from pprint import pprint
import heapq
import json


Vertex = namedtuple('Vertex', ['vertex', 'weight'])
Edge = namedtuple('Edge', ['start', 'finish', 'weight'])


def parse_adjaency_matrix_to_graph(filename: str):
    """
    """
    matrix = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            matrix.append([int(weight) for weight in line.split(' ')])
    graph: MutableMapping[str, List[Vertex]] = defaultdict(list[Vertex])
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] != 0:
                graph[chr(ord("A") + row)].append(
                    Vertex(
                        chr(ord("A") + col),
                        matrix[row][col]
                    )
                )
    return graph


def parse_list_of_edges_to_graph(filename: str) -> MutableMapping[str, List[Vertex]]:
    graph: MutableMapping[str, List[Vertex]] = defaultdict(list[Vertex])
    lines = (line for line in open('list_of_edges.txt',
             'r', encoding='utf-8').readlines())
    for line in lines:
        u, v, weight = line[1:-2].split(',')
        graph[u].append(Vertex(v, int(weight)))
    return graph


def prim_algorithm(
    graph: MutableMapping[str, List[Vertex]],
    start: str
) -> List[Edge]:
    """Prim`s algorithm for minimal spanning tree search.
    """
    if start not in graph:
        raise KeyError

    visited = set()
    min_heap: List[Tuple[float, str, str]] = []
    mst_edges = []

    visited.add(start)
    for v, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, v))

    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        if v in visited:
            continue
        visited.add(v)
        mst_edges.append(Edge(u, v, weight))
        for neighbour, weight in graph[v]:
            if neighbour not in visited:
                heapq.heappush(min_heap, (weight, v, neighbour))
    return mst_edges


def parse_edges():
    with open('cities.json', 'r', encoding='utf-8') as file:
        edges: List[MutableMapping[str, Union[str, float]]] = json.load(file)
    edges = [Edge(**edge) for edge in edges]
    return edges


def parse_edges_to_graph() -> MutableMapping[str, List[Vertex]]:
    graph: MutableMapping[str, List[Vertex]] = defaultdict(list[Vertex])
    edges = parse_edges()
    for edge in edges:
        start = edge.pop('start')
        vertex = Vertex(edge['finish'], edge['weight'])
        graph[start].append(vertex)
    return graph


def read_cities():
    return [line.strip() for line in open('cities.txt', 'r', encoding='utf-8').readlines()]


def encode_decode_cities(
    cities: List[str],
) -> Tuple[MutableMapping[str, int], MutableMapping[int, str]]:
    city_to_code = {item: code for code, item in enumerate(cities)}
    code_to_city = {code: item for code, item in enumerate(cities)}
    return city_to_code, code_to_city


def encode_cities(encoder: MutableMapping[str, int], edges: List[Edge]):
    for i in range(len(edges)):
        encoded_start = encoder[edges[i].start]
        encoded_finish = encoder[edges[i].finish]
        weight = edges[i].weight
        edges[i] = Edge(encoded_start, encoded_finish, weight)


def decode_cities(decoder: MutableMapping[int, str], edges: List[Edge]):
    for i in range(len(edges)):
        decoded_start = decoder[edges[i].start]
        decoded_finish = decoder[edges[i].finish]
        weight = edges[i].weight
        edges[i] = Edge(decoded_start, decoded_finish, weight)


def kruskal_algorithm(
    edges: List[Edge],
    num_vertices: int
) -> List[Edge]:
    mst_edges: List[Edge] = []
    djs = DisjointSet(num_vertices)

    edges.sort(key=lambda edge: edge.weight)

    for u, v, weight in edges:
        if djs.union(u, v):
            mst_edges.append(Edge(u, v, weight))
            if len(mst_edges) == num_vertices - 1:
                break

    return mst_edges


def dijkstra(
    graph: MutableMapping[str, List[Vertex]],
    source: str
) -> Tuple[MutableMapping, MutableMapping]:
    dist = {vertex: float('inf') for vertex in graph}
    prev = {vertex: None for vertex in graph}
    dist[source] = 0
    min_heap = [(0, source)]

    while min_heap:
        current_dist, u = heapq.heappop(min_heap)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            alt = current_dist + weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(min_heap, (alt, v))

    return dist, prev
