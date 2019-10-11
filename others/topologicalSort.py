from collections import deque
from itertools import filterfalse
from typing import List, Tuple

class Graph:
    def __init__(self, num_vertices: int):
        self._num_vertices = num_vertices
        self._adj: List[List[int]]  = [[] for _ in range(num_vertices)]
    
    def add_edge(self, s: int, t: int) -> None:
        self._adj[s].append(t)

    def tsort_kahn(self) -> List[int]:
        in_degree = [0] * self._num_vertices
        for v in range(self._num_vertices):
            for neighbor in self._adj[v]:
                in_degree[neighbor] += 1
        q = deque(filterfalse(lambda x: in_degree[x], range(self._num_vertices)))
        topo = []
        while q:
            v = q.popleft()
            for neighbor in self._adj[v]:
                in_degree[neighbor] -= 1
                if not in_degree[neighbor]:
                    q.append(neighbor)
            topo.append(v)
        return topo

    def tsort_dfs(self) -> List[int]:
        inverse_adj = [[] for _ in range(self._num_vertices)]
        for v in range(self._num_vertices):
            for neighbor in self._adj[v]:
                inverse_adj[neighbor].append(v)
        visited = [False] * self._num_vertices
        topo = []

        def dfs(vertex: int, topo: List[int]):
            if visited[vertex]: return
            visited[vertex] = True
            for v in inverse_adj[vertex]:
                if not visited[v]:
                    dfs(v, topo)
            topo.append(vertex)
        
        for v in range(self._num_vertices):
            dfs(v, topo)

        return topo

if __name__ == '__main__':
    graph = Graph(4)
    graph.add_edge(1, 0)
    graph.add_edge(2, 1)
    graph.add_edge(1, 3)
    print(graph.tsort_kahn())
    print(graph.tsort_dfs())

    graph = Graph(2)
    graph.add_edge(0, 1)
    graph.add_edge(1, 0)
    print(graph.tsort_kahn())
    print(graph.tsort_dfs())