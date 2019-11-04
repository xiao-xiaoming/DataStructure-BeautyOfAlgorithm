# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import random


def partition(arr: list, p, r):
    i, pivot = p, arr[r]
    for j in range(p, r):
        if arr[j] < pivot:
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def partition_two_way(arr, p, r):
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


def quick_sort(arr, p, r):
    if p >= r: return
    q = partition(arr, p, r)
    quick_sort(arr, p, q - 1)
    quick_sort(arr, q + 1, r)


a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
quick_sort(a4, 0, len(a4) - 1)
print(a4)
