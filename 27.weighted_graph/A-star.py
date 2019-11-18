# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

from typing import List, Optional
import heapq
from collections import deque


class Edge:
    def __init__(self, sid: int, tid: int, w: int) -> None:
        self.sid = sid
        self.tid = tid
        self.w = w


class Vertex:
    def __init__(self, id: int, x: int, y: int) -> None:
        self.id = id  # 顶点编号 ID
        # 顶点在地图中的坐标（x, y）
        self.x = x
        self.y = y
        self.f = float("inf")
        self.dist = float("inf")  # 从起始顶点，到这个顶点的距离，也就是 g(i)

    def __gt__(self, other) -> bool:
        return self.f > other.f


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


def print_path(predecessor, s, t):
    result = deque()
    while t != s:
        result.appendleft(str(t))
        t = predecessor[t]
    result.appendleft(str(s))
    print(" -> ".join(result))


def hManhattan(v1: Vertex, v2: Vertex) -> int:
    return abs(v1.x - v2.x) + abs(v1.y - v2.y)


class Graph:
    def __init__(self, vertex_count: int):
        self.adj = [deque() for _ in range(vertex_count)]
        self.vertexes: List[Optional[Vertex]] = [None] * vertex_count

    def add_vertex(self, id: int, x: int, y: int):
        self.vertexes[id] = Vertex(id, x, y)

    def add_edge(self, s: int, t: int, w: int, two_way: bool = True):
        self.adj[s].append(Edge(s, t, w))
        if two_way: self.adj[t].append(Edge(t, s, w))

    def astar(self, s: int, t: int):
        v = len(self.adj)
        predecessor = [0] * v
        queue = VertexPriorityQueue()
        inqueue = [False] * v
        self.vertexes[s].dist = 0
        self.vertexes[s].f = 0
        queue.add(self.vertexes[s])
        inqueue[s] = True

        while not queue.is_empty():
            min_vertex: Vertex = queue.poll()
            for e in self.adj[min_vertex.id]:
                next_vertex = self.vertexes[e.tid]
                if min_vertex.dist + e.w < next_vertex.dist:
                    next_vertex.dist = min_vertex.dist + e.w
                    next_vertex.f = next_vertex.dist + hManhattan(next_vertex, self.vertexes[t])
                    predecessor[next_vertex.id] = min_vertex.id
                    if inqueue[next_vertex.id]:
                        queue.update(next_vertex)
                    else:
                        queue.add(next_vertex)
                        inqueue[next_vertex.id] = True
                if next_vertex.id == t: break
        print_path(predecessor, s, t)
        return self.vertexes[t].dist


if __name__ == '__main__':
    g = Graph(14)
    g.add_vertex(0, 320, 630)
    g.add_vertex(1, 300, 630)
    g.add_vertex(2, 280, 625)
    g.add_vertex(3, 270, 630)
    g.add_vertex(4, 320, 700)
    g.add_vertex(5, 360, 620)
    g.add_vertex(6, 320, 590)
    g.add_vertex(7, 370, 580)
    g.add_vertex(8, 350, 730)
    g.add_vertex(9, 390, 690)
    g.add_vertex(10, 400, 620)
    g.add_vertex(11, 400, 580)
    g.add_vertex(12, 270, 670)
    g.add_vertex(13, 270, 600)
    g.add_edge(0, 1, 20)
    g.add_edge(0, 4, 60)
    g.add_edge(0, 5, 60)
    g.add_edge(0, 6, 60)
    g.add_edge(1, 2, 20)
    g.add_edge(2, 3, 10)
    g.add_edge(3, 12, 40)
    g.add_edge(3, 13, 50)
    g.add_edge(12, 4, 40)
    g.add_edge(13, 6, 50)
    g.add_edge(4, 8, 50)
    g.add_edge(8, 5, 70)
    g.add_edge(8, 9, 50)
    g.add_edge(5, 9, 80)
    g.add_edge(5, 10, 50)
    g.add_edge(9, 10, 60)
    g.add_edge(6, 7, 70)
    g.add_edge(7, 11, 50)
    g.add_edge(11, 10, 60)
    print(g.astar(0, 10))
