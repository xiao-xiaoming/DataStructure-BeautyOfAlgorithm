# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import random


def partition(arr, p, r):
    # 随机选取基准值, 并将基准值替换到数组第一个元素
    q = random.randint(p, r)
    arr[p], arr[q] = arr[q], arr[p]
    pivot = arr[p]
    while p < r:
        # 从右向左查找比基准值小的位置
        while p < r and arr[r] >= pivot: r -= 1
        arr[p] = arr[r]
        # 从左向右查找比基准值大的位置
        while p < r and arr[p] <= pivot: p += 1
        arr[r] = arr[p]
    arr[p] = pivot
    return p


def kth_smallest(arr: list, k: int):
    if len(arr) < k: return -1
    q = partition(arr, 0, len(arr) - 1)
    while q != k - 1:
        if q < k - 1:
            q = partition(arr, q + 1, len(arr) - 1)
        else:
            q = partition(arr, 0, q - 1)
    return arr[q]
