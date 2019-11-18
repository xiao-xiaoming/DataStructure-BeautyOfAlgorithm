# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

from collections import deque


class Graph:
    def __init__(self, v: int):
        self.v = v  # 顶点的个数
        self.adj = [deque() for _ in range(v)]  # 邻接表

    def add_edge(self, s: int, t: int) -> None:
        self.adj[s].append(t)

    def topo_sort_by_kahn(self) -> None:
        in_degree = [0] * self.v
        for i in range(self.v):
            if len(self.adj[i]):
                for w in self.adj[i]:
                    in_degree[w] += 1
        queue = deque()
        for i in range(self.v):
            if in_degree[i] == 0: queue.append(i)
        while queue:
            i = queue.popleft()
            print(f"{i} -> ", end="")
            for k in self.adj[i]:
                in_degree[k] -= 1
                if in_degree[k] == 0:
                    queue.append(k)
        print("\b\b\b\b")

    def topp_sort_by_dfs(self) -> None:
        # 先构建逆邻接表,边s->t表示s依赖于t,t先于s
        inverse_adjacency = [deque() for _ in range(self.v)]
        for i in range(self.v):
            if len(self.adj[i]):
                for w in self.adj[i]:
                    inverse_adjacency[w].append(i)
        visited = [False] * self.v

        def dfs(vertex: int) -> None:
            if len(inverse_adjacency[vertex]):
                for w in inverse_adjacency[vertex]:
                    if not visited[w]:
                        visited[w] = True
                        dfs(w)
            print(f"{vertex} -> ", end="")

        for i in range(self.v):
            if not visited[i]:
                visited[i] = True
                dfs(i)
        print("\b\b\b\b")


if __name__ == "__main__":
    dag = Graph(4)
    dag.add_edge(1, 0)
    dag.add_edge(2, 1)
    dag.add_edge(1, 3)
    dag.topo_sort_by_kahn()
    dag.topp_sort_by_dfs()
