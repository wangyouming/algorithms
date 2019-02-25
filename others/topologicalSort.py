from collections import deque
from itertools import filterfalse
from typing import List

class Graph:
    def __init__(self, num_vertices: int):
        self._num_vertices = num_vertices
        self._adjacency: List[List[int]]  = [[] for _ in range(num_vertices)]
    
    def add_edge(self, s: int, t: int) -> None:
        self._adjacency[s].append(t)

    def tsort_kahn(self) -> None:
        in_degree = [0] * self._num_vertices
        for v in range(self._num_vertices):
            for neighbor in self._adjacency[v]:
                in_degree[neighbor] += 1
        q = deque(filterfalse(lambda x: in_degree[x], range(self._num_vertices)))
        while q:
            v = q.popleft()
            for neighbor in self._adjacency[v]:
                in_degree[neighbor] -= 1
                if not in_degree[neighbor]:
                    q.append(neighbor)
            print("{}{}".format(v, " -> " if q else '\n'), end="")

    def tsort_dfs(self) -> None:
        inverse_adjacency = [[] for _ in range(self._num_vertices)]
        for v in range(self._num_vertices):
            for neighbor in self._adjacency[v]:
                inverse_adjacency[neighbor].append(v)
        visited = [False] * self._num_vertices
        not_visited_count = self._num_vertices

        def dfs(vertex: int) -> None:
            nonlocal not_visited_count
            for v in inverse_adjacency[vertex]:
                if not visited[v]:
                    visited[v] = True
                    not_visited_count -= 1
                    dfs(v)
            print("{}{}".format(vertex, " -> " if not_visited_count else "\n"), end="")
        
        for v in range(self._num_vertices):
            if not visited[v]:
                visited[v] = True
                not_visited_count -= 1
                dfs(v)

if __name__ == '__main__':
    graph = Graph(4)
    graph.add_edge(1, 0)
    graph.add_edge(2, 1)
    graph.add_edge(1, 3)
    graph.tsort_kahn()
    graph.tsort_dfs()