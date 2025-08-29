from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import MutableMapping, List, Tuple, Generator
from collections import defaultdict, namedtuple, deque
import heapq
import os
import pprint


Vertex = namedtuple('Vertex', ['vertex', 'weight'])
Edge = namedtuple('Edge', ['start', 'finish', 'weight'])


class DisjointSet:
    """Implementation of disjoint set.
    """

    def __init__(self, _num):
        self._parent = list(range(_num))
        self._rank = [1] * _num

    def find(self, u: int) -> int:
        """Find _parent for given node

        Args:
            u (int): node

        Returns:
            int: _parent
        """
        if self._parent[u] != u:
            self._parent[u] = self.find(self._parent[u])
        return self._parent[u]

    def union(self, u: int, v: int) -> bool:
        """Checks, if two nodes are whether in the same
        set or in the different

        Args:
            u (int): first node
            v (int): second node

        Returns:
            bool: True, if two nodes were not in the same
            set, False, if two node were in the same set
        """
        uroot = self.find(u)
        vroot = self.find(v)

        if uroot == vroot:
            return False
        if self._rank[uroot] < self._rank[vroot]:
            self._parent[uroot] = vroot
        elif self._rank[uroot] > self._rank[vroot]:
            self._parent[vroot] = uroot
        else:
            self._parent[vroot] = uroot
            self._rank[uroot] += 1
        return True


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list[Vertex])
        self.directed = directed

    @property
    def vertices(self) -> List[str]:
        return list(self.graph.keys())

    @property
    def edges(self) -> set[Edge]:
        edges: set[Edge] = set()
        for u in self.graph:
            for v, weight in self.graph[u]:
                if (v, u, weight) not in edges:
                    edges.add(Edge(u, v, weight))
        return edges

    def add_edge(self, source: str, dest: str, weight: float) -> None:
        if weight < 0:
            raise ValueError
        vertex = Vertex(dest, weight)
        if source not in self.graph:
            self.graph[source].append(vertex)
        else:
            for i, vertex in enumerate(self.graph[source]):
                if self.graph[source][i].vertex == source:
                    self.graph[source][i].weight = weight
            else:
                self.graph[source].append(vertex)

    def remove_edge(self, source: str, dest: str, weight: float) -> None:
        if source not in self.graph:
            print(f'Vertex "{source}" is not present in graph!')
        else:
            target = Vertex(dest, weight)
            for index, vertex in enumerate(self.graph[source]):
                if vertex == target:
                    self.graph[source].pop(index)

    def _get_vertices_degrees(self) -> MutableMapping[str, int]:
        degrees = {source: len(self.graph[source]) for source in self.graph}
        return degrees

    def degree(self, vertex: str) -> int:
        try:
            degrees = self._get_vertices_degrees()
            return degrees[vertex]
        except KeyError:
            print(f'Vertex "{vertex}" is not present in graph!')
            return -1

    def parse_to_graph(self, filename: str, parser: GraphParser) -> None:
        parser.parse_to_graph(filename, self)

    def parse_from_graph(self, filename: str, parser: GraphParser) -> None:
        parser.parse_from_graph(filename, self)

    def prim_algorithm(self, start: str) -> List[Edge]:
        """Implementation of Prim`s algorithm

        Args:
            start (str): initial vertex name

        Returns:
            List[Edge]: list of edges in minimal spanning tree
        """
        visited = set()
        mst_edges: List[Edge] = []
        min_heap: List[Tuple[float, str, str]] = []

        visited.add(start)
        for v, weight in self.graph[start]:
            heapq.heappush(min_heap, (weight, start, v))

        while min_heap:
            weight, u, v = heapq.heappop(min_heap)

            if v in visited:
                continue

            visited.add(v)
            mst_edges.append(Edge(u, v, weight))
            for vertex, weight in self.graph[v]:
                if vertex not in visited:
                    heapq.heappush(min_heap, (weight, v, vertex))

        return mst_edges

    def _encode_vertices(
        self,
        vertices: List[str]
    ) -> Tuple[MutableMapping, MutableMapping]:
        """Creates encoder and decoder of vertices for DisjointSet

        Args:
            vertices (List[str]): list of vertices names

        Returns:
            Tuple[MutableMapping, MutableMapping]: tuple of encoder and decoder
        """
        encoder = {vertex: code for code, vertex in enumerate(vertices)}
        decoder = {code: vertex for code, vertex in enumerate(vertices)}
        return encoder, decoder

    def _get_graph_edges(self) -> List[Tuple[int, int, float]]:
        """Get graph edges

        Raises:
            ValueError: if graph was not parsed

        Returns:
            List[Tuple[int, int, float]]: list of edges
        """
        if not self.graph:
            raise ValueError
        encoder, _ = self._encode_vertices(list(self.graph.keys()))
        edges = [(encoder[u], encoder[v], weight)
                 for u, vertices in self.graph.items()
                 for v, weight in vertices]
        return edges

    def kruskal_algorithm(self) -> List[Edge]:
        """Implementation of Kruskal`s algorithm

        Returns:
            List[Edge]: list of edges in minimal spanning tree
        """
        mst_edges: List[Edge] = []
        disjoint_set = DisjointSet(len(self.graph.keys()))

        edges = self._get_graph_edges()
        edges.sort(key=lambda edge: edge[2])

        vertices = list(self.graph.keys())

        for u, v, weight in edges:
            if disjoint_set.union(u, v):
                mst_edges.append(Edge(u, v, weight))
                if len(mst_edges) == len(vertices) - 1:
                    break

        _, decoder = self._encode_vertices(vertices)

        mst_edges = [Edge(decoder[u], decoder[v], weight)
                     for u, v, weight in mst_edges]

        return mst_edges

    def dijkstra_algorithm(self, source: str) -> MutableMapping[str, float]:
        """Implementation of Dijkstra`a algorithm

        Args:
            source (str): initial vertex

        Returns:
            MutableMapping[str, float]: distance from initial to rest vertices
        """
        min_heap = [(0, source)]
        dist = {vertex: float('inf') for vertex in self.graph}
        dist[source] = 0

        while min_heap:
            current_distance, u = heapq.heappop(min_heap)

            if current_distance > dist[u]:
                continue

            for v, weight in self.graph[u]:
                alt = current_distance + weight
                if alt < dist[v]:
                    dist[v] = alt
                    heapq.heappush(min_heap, (alt, v))

        return dist

    def breadth_first_search(self, start: str) -> str:
        """Breadth first search

        Args:
            start (str): initial vertex

        Returns:
            str: string of bfs
        """
        queue = deque([start])
        ordered_visited = []
        while queue:
            vertex = queue.popleft()
            if vertex not in ordered_visited:
                ordered_visited.append(vertex)
                for v, _ in self.graph[vertex]:
                    queue.append(v)
        return ' -> '.join(ordered_visited)

    def depth_first_search(self, start: str) -> str:
        """Depth first search

        Args:
            start (str): initial vertex

        Returns:
            str: string of bfs
        """
        queue = deque([start])
        ordered_visited = []
        while queue:
            vertex = queue.popleft()
            if vertex not in ordered_visited:
                ordered_visited.append(vertex)
                for v, _ in self.graph[vertex]:
                    queue.appendleft(v)
        return ' -> '.join(ordered_visited)

    def __repr__(self) -> str:
        edges = self.edges
        return (f'Graph({[(u, v) for u, v, _ in edges]}, '
                f'edges={len(edges)}, vertices={list(self.graph.keys())})')


class GraphParser(metaclass=ABCMeta):
    file_folder = 'graph_views'

    def _read_file(
        self,
        filename: str
    ) -> Generator[str, None, None]:
        try:
            path = os.path.join(self.file_folder, filename)
            lines = (line for line in open(
                path, 'r', encoding='utf-8').readlines())
            return lines
        except FileNotFoundError:
            print('File doesn`t exist!')
            return

    @abstractmethod
    def parse_to_graph(self, filename: str, graph: Graph) -> None:
        pass

    @abstractmethod
    def parse_from_graph(self, filename: str, graph: Graph) -> None:
        pass


class AdjacencyMatrixParser(GraphParser):

    def parse_to_graph(self, filename: str, graph: Graph) -> None:
        """Parsing adjaency matrix to graph

        Args:
            filename (str): name of file
        """
        lines = self._read_file(filename)
        if lines:
            matrix = []
            for line in lines:
                matrix.append([int(weight) for weight in line.split(' ')])
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    if matrix[row][col] != 0:
                        graph.graph[chr(ord("A") + row)].append(
                            Vertex(
                                chr(ord("A") + col),
                                matrix[row][col]
                            )
                        )
        else:
            print('File is empty!')
            return

    def parse_from_graph(self, filename: str, graph: Graph):
        num_vertices = len(graph.graph.keys())
        matrix = [[0 for _ in range(num_vertices)]
                  for _ in range(num_vertices)]
        for u in graph.graph:
            for v, weight in graph.graph[u]:
                matrix[ord(u) - ord('A')][ord(v) - ord('A')] = weight
        result = ''
        for row in matrix:
            temp = ''
            for item in row:
                temp += f'{str(item)} '
            temp = temp[:-1] + '\n'
            result += temp
        result = result[:-1]
        path = os.path.join(self.file_folder, filename)
        with open(path, 'w', encoding='utf-8') as file:
            file.write(result)


class EdgeListsParser(GraphParser):
    def parse_to_graph(self, filename: str, graph: Graph) -> None:
        """Parsing list of edges to graph

        Args:
            filename (str): name of file
        """
        lines = self._read_file(filename)
        if lines:
            for line in lines:
                u, v, weight = line[1:-2].split(',')
                graph.graph[u].append(Vertex(v, int(weight)))
        else:
            print('File is empty!')
            return

    def parse_from_graph(self, filename: str, graph: Graph) -> None:
        result = ''
        template = '[{},{},{}]\n'
        for u in graph.graph:
            for v, weight in graph.graph[u]:
                result += template.format(u, v, weight)
        path = os.path.join(self.file_folder, filename)
        with open(path, 'w', encoding='utf-8') as file:
            file.write(result)


class ContiguityListsParser(GraphParser):
    def parse_to_graph(self, filename: str, graph: Graph) -> None:
        """Parsing contiguity lists to graph

        Args:
            filename (str): name of file which contains lists of contiguity
        """
        lines = self._read_file(filename)
        if lines:
            for line in lines:
                left_vertex_bound = line.find('[')
                right_vertex_bound = line.find(']')
                vertex = line[left_vertex_bound + 1: right_vertex_bound]
                edges = line[right_vertex_bound + 4:].split('->')
                for edge in edges:
                    edge = edge.strip()
                    try:
                        graph.graph[vertex].append(
                            Vertex(edge[0], float(edge[2])))
                    except ValueError:
                        raise ValueError(
                            'Edge`s weight should be integer or float')
        else:
            print('File is empty!')
            return

    def parse_from_graph(self, filename: str, graph: Graph) -> None:
        result = ''
        for u in graph.graph:
            result += (f'[{u}] -> ' +
                       ' -> '.join([f'{v}:{int(weight)}'
                                    for v, weight in graph.graph[u]]) + '\n')
        result = result[:-1]
        path = os.path.join(self.file_folder, filename)
        with open(path, 'w', encoding='utf-8') as file:
            file.write(result)


class IncidenceMatrixParser(GraphParser):
    def parse_to_graph(self, filename: str, graph: Graph) -> None:
        """Parsing incidence matrix to graph

        Args:
            filename (str): name of file
        """
        lines = self._read_file(filename)
        if lines:
            matrix = []
            for line in lines:
                matrix.append([int(weight) for weight in line.split()])
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    if matrix[row][col] != 0:
                        graph.graph[chr(ord('a') + row)].append(
                            Vertex(
                                vertex=chr(ord('a') + col),
                                weight=matrix[row][col],
                            )
                        )
        else:
            print('File is empty!')
            return

    def parse_from_graph(self, filename: str, graph: Graph) -> None:
        path = os.path.join(self.file_folder, filename)
        result = ''
        with open(path, 'w', encoding='utf-8') as file:
            file.write(result)
