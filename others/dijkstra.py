from typing import List, Generator
from heap import PriorityQueue

class Graph:
    def __init__(self, vertex_count: int):
        self.adj = [[] for _ in range(vertex_count)]
    
    def add_edge(self, s: int, t: int, w: int) -> None:
        edge = Edge(s, t, w)
        self.adj[s].append(edge)
    
    def __len__(self) -> int:
        return len(self.adj)
    
class Vertex:
    def __init__(self, v: int, dist: int):
        self.id = v
        self.dist = dist
    
    def __gt__(self, other) -> bool:
        return self.dist > other.dist
    
    def __repr__(self) -> str:
        return str((self.id, self.dist))

class Edge:
    def __init__(self, source: int, target: int, weight: int):
        self.s = source
        self.t = target
        self.w = weight

def dijkstra(g: Graph, s: int, t: int) -> int:
    size = len(g)
    in_queue = [False] * size
    vertices = [Vertex(v, float('inf')) for v in range(size)]
    predecessor = [-1] * size

    vertices[s].dist = 0
    pq = PriorityQueue()
    pq.put(vertices[s])
    in_queue[s] = True

    while pq:
        v = pq.get()
        if v.id == t:
            break
        
        for edge in g.adj[v.id]:
            if v.dist + edge.w < vertices[edge.t].dist:
                vertices[edge.t].dist = v.dist + edge.w
                predecessor[edge.t] = v.id
                if in_queue[edge.t]:
                    pq.heapup(vertices[edge.t])
                else:
                    pq.put(vertices[edge.t])
                    in_queue[edge.t] == True
    
    for n in print_path(s, t, predecessor):
        if n == t:
            print(t)
        else:
            print(n, end=' ->')
    
    return vertices[t].dist

def print_path(s: int, t: int, p: List[int]) -> Generator[int, None, None]:
    if t == s:
        yield s
    else:
        yield from print_path(s, p[t], p)
        yield t

if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 4, 15)
    g.add_edge(1, 2, 15)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 5, 5)
    g.add_edge(3, 2, 1)
    g.add_edge(3, 5, 12)
    g.add_edge(4, 5, 10)
    print(dijkstra(g, 0, 5))