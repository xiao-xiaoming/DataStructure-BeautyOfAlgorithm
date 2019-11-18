# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import heapq
from collections import deque


def print_path(predecessor, s, t):
    result = deque()
    while t != s:
        result.appendleft(str(t))
        t = predecessor[t]
    result.appendleft(str(s))
    print(" -> ".join(result))


class Graph:
    def __init__(self, vertex_count: int):
        self.adj = [deque() for _ in range(vertex_count)]

    def add_edge(self, s: int, t: int, w: int):
        self.adj[s].append(Edge(s, t, w))

    def dijkstra(self, s: int, t: int):
        v = len(self.adj)
        predecessor = [0] * v
        vertexes = [Vertex(i) for i in range(v)]
        queue = VertexPriorityQueue()
        inqueue = [False] * v
        vertexes[s].dist = 0
        queue.add(vertexes[s])
        inqueue[s] = True

        while not queue.is_empty():
            min_vertex: Vertex = queue.poll()
            if min_vertex.id == t: break
            for e in self.adj[min_vertex.id]:
                next_vertex = vertexes[e.tid]
                if min_vertex.dist + e.w < next_vertex.dist:
                    next_vertex.dist = min_vertex.dist + e.w
                    predecessor[next_vertex.id] = min_vertex.id
                    if inqueue[next_vertex.id]:
                        queue.update(next_vertex)
                    else:
                        queue.add(next_vertex)
                        inqueue[next_vertex.id] = True
        print_path(predecessor, s, t)
        return vertexes[t].dist


class Edge:
    def __init__(self, sid: int, tid: int, w: int) -> None:
        self.sid = sid
        self.tid = tid
        self.w = w


class Vertex:
    def __init__(self, id: int, dist: int = float("inf")) -> None:
        self.id = id
        self.dist = dist

    def __gt__(self, other) -> bool:
        return self.dist > other.dist


class VertexPriorityQueue:
    def __init__(self) -> None:
        self.vertices = []

    def poll(self) -> Vertex:
        return heapq.heappop(self.vertices)

    def add(self, vertex: Vertex) -> None:
        heapq.heappush(self.vertices, vertex)

    def update(self, vertex: Vertex) -> None:
        for i, v in enumerate(self.vertices):
            if vertex.id == v.id:
                v.dist = vertex.dist
                heapq._siftdown(self.vertices, 0, i)
                break

    def is_empty(self) -> bool:
        return len(self.vertices) == 0


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
    print(g.dijkstra(0, 5))

    g = Graph(4)
    g.add_edge(0, 1, 18)
    g.add_edge(0, 2, 3)
    g.add_edge(2, 1, 1)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 8)
    g.add_edge(0, 3, 15)
    print(g.dijkstra(0, 3))
