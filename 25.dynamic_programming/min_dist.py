# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import sys
from typing import List


def min_dist_DP(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    states = [[0] * n for _ in range(m)]
    sum = 0
    for j in range(n):
        sum += matrix[0][j]
        states[0][j] = sum
    sum = 0
    for i in range(n):
        sum += matrix[i][0]
        states[i][0] = sum
    for i in range(1, n):
        for j in range(1, n):
            states[i][j] = matrix[i][j] + min(states[i][j - 1], states[i - 1][j])
    return states[-1][-1]


def min_dist(matrix: List[List[int]]):
    m, n = len(matrix), len(matrix[0])
    mem = [[0] * n for _ in range(m)]

    def min_dist_in(i: int, j: int):
        if i == j == 0: return matrix[0][0]
        if mem[i][j]: return mem[i][j]
        if i < 0 or j < 0: return sys.maxsize
        curr_min_dist = matrix[i][j] + min(min_dist_in(i, j - 1), min_dist_in(i - 1, j))
        mem[i][j] = curr_min_dist
        return curr_min_dist

    return min_dist_in(m - 1, n - 1)


if __name__ == "__main__":
    weights = [[1, 3, 5, 9],
               [2, 1, 3, 4],
               [5, 2, 6, 7],
               [6, 8, 4, 3]]
    print(min_dist_DP(weights))
    print(min_dist(weights))
