from typing import MutableMapping, List, Tuple
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
        self.parent = list(range(_num))
        self.rank = [1] * _num

    def find(self, u: int) -> int:
        """Find parent for given node

        Args:
            u (int): node

        Returns:
            int: parent
        """
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

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
        if self.rank[uroot] < self.rank[vroot]:
            self.parent[uroot] = vroot
        elif self.rank[uroot] > self.rank[vroot]:
            self.parent[vroot] = uroot
        else:
            self.parent[vroot] = uroot
            self.rank[uroot] += 1
        return True


class Graph:
    def __init__(self):
        self.graph: MutableMapping[str, List[Vertex]
                                   ] = defaultdict(list[Vertex])

    def parse_contiguity_lists_to_graph(self, filename: str) -> None:
        """Parsing contiguity lists to graph

        Args:
            filename (str): name of file which contains lists of contiguity
        """
        path = os.path.join('graph_views', filename)
        lines = (line for line in open(
            path, 'r', encoding='utf-8').readlines())
        for line in lines:
            left_vertex_bound = line.find('[')
            right_vertex_bound = line.find(']')
            vertex = line[left_vertex_bound + 1: right_vertex_bound]
            edges = line[right_vertex_bound + 4:].split('->')
            for edge in edges:
                edge = edge.strip()
                self.graph[vertex].append(Vertex(edge[0], edge[2]))

    def parse_incidence_matrix_to_graph(self, filename: str) -> None:
        """Parsing incidence matrix to graph

        Args:
            filename (str): name of file
        """
        matrix = []
        path = os.path.join('graph_views', filename)
        lines = (line for line in open(
            path, 'r', encoding='utf-8').readlines())
        for line in lines:
            matrix.append([int(weight) for weight in line.split()])
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] != 0:
                    self.graph[chr(ord('a') + row)].append(
                        Vertex(
                            vertex=chr(ord('a') + col),
                            weight=matrix[row][col],
                        )
                    )

    def parse_adjaency_matrix_to_graph(self, filename: str) -> None:
        """Parsing adjaency matrix to graph

        Args:
            filename (str): name of file
        """
        path = os.path.join('graph_views', filename)
        matrix = []
        lines = (line for line in open(
            path, 'r', encoding='utf-8').readlines())
        for line in lines:
            matrix.append([int(weight) for weight in line.split(' ')])
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] != 0:
                    self.graph[chr(ord("A") + row)].append(
                        Vertex(
                            chr(ord("A") + col),
                            matrix[row][col]
                        )
                    )

    def parse_list_of_edges_to_graph(self, filename: str) -> None:
        """Parsing list of edges to graph

        Args:
            filename (str): name of file
        """
        path = os.path.join('graph_views', filename)
        lines = (line for line in open(path,
                                       'r', encoding='utf-8').readlines())
        for line in lines:
            u, v, weight = line[1:-2].split(',')
            self.graph[u].append(Vertex(v, int(weight)))

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

    def get_graph_edges(self) -> List[Tuple[int, int, float]]:
        """Get graph edges

        Raises:
            ValueError: if graph was not parsed

        Returns:
            List[Tuple[int, int, float]]: list of edges
        """
        if not graph:
            raise ValueError
        encoder, _ = self._encode_vertices(list(self.graph.keys()))
        edges = [(encoder[u], encoder[v], weight) for u, vertices in self.graph.items()
                 for v, weight in vertices]
        return edges

    def kruskal_algorithm(self) -> List[Edge]:
        """Implementation of Kruskal`s algorithm

        Returns:
            List[Edge]: list of edges in minimal spanning tree
        """
        mst_edges: List[Edge] = []
        disjoint_set = DisjointSet(len(self.graph.keys()))

        edges = self.get_graph_edges()
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


graph = Graph()
graph.parse_adjaency_matrix_to_graph('adjaency matrix.txt')
bfs = graph.breadth_first_search('A')
dfs = graph.depth_first_search('A')
pprint.pprint(bfs)
pprint.pprint(dfs)
