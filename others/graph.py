from typing import List, Optional, Generator, IO
from queue import Queue

class Graph:
    def __init__(self, num_vertices: int):
        self._num_vertices = num_vertices
        self._adjacency = [[] for _ in range(num_vertices)]

    def add_edge(self, s: int, t: int) -> None:
        self._adjacency[s].append(t)
        self._adjacency[t].append(s)

    def _generate_path(self, s: int, t: int, prev: List[Optional[int]]) -> Generator[str, str, None]:
        if prev[t] or s != t:
            yield from self._generate_path(s, prev[t], prev)
        yield str(t)
    
    def bfs(self, s: int, t:int) -> IO[str]:
        if s == t: return
        
        visited = [False] * self._num_vertices
        visited[s] = True
        q = Queue()
        q.put(s)
        prev = [None] * self._num_vertices

        while q:
            v = q.get()
            for neighbor in self._adjacency[v]:
                if not visited[neighbor]:
                    prev[neighbor] = v
                    if neighbor == t:
                        print("->".join(self._generate_path(s, t, prev)))
                        return
                    visited[neighbor] = True
                    q.put(neighbor)
    
    def dfs(self, s: int, t: int) -> IO[str]:
        found = False
        visited = [False] * self._num_vertices
        prev= [None] * self._num_vertices

        def _dfs(from_vertex: int) -> None:
            nonlocal found
            if found: return
            visited[from_vertex] = True
            if from_vertex == t:
                found = True
                return
            for neighbor in self._adjacency[from_vertex]:
                if not visited[neighbor]:
                    prev[neighbor] = from_vertex
                    _dfs(neighbor)

        _dfs(s)
        print("->".join(self._generate_path(s, t, prev)))

if __name__ == "__main__":
    
    graph = Graph(8)

    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 7)

    graph.bfs(0, 7)
    graph.dfs(0, 7)
