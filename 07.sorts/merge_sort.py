# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import sys


def merge(arr, p, q, r):
    i, j, k = p, q + 1, 0  # 初始化变量 i, j, k
    tmp = [0] * (r - p + 1)  # 申请一个大小跟arr[p:r+1]一样的临时数组
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            i += 1
        else:
            tmp[k] = arr[j]
            j += 1
        k += 1
    # 判断哪个子数组中有剩余的数据
    start, end = i, q
    if j <= r: start, end = j, r
    # 将剩余的数据拷贝到临时数组tmp
    while start <= end:
        tmp[k] = arr[start]
        k += 1
        start += 1
    # 将tmp中的数组拷贝回 arr[p:r+1]
    arr[p: r + 1] = tmp


def merge_by_sentry(arr, p, q, r):
    n1, n2 = q - p + 1, r - q  # 表示两个子数组的长度
    # 需要一个位置存储哨兵，所以临时数组长度是 子数组长度+1
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    # 拷贝数据到临时数组 L[] 和 R[]
    for i in range(0, n1):
        L[i] = arr[p + i]
    L[n1] = sys.maxsize  # 第一个数组添加哨兵（最大值）
    for j in range(0, n2):
        R[j] = arr[q + 1 + j]
    R[n2] = sys.maxsize  # 第二个数组添加哨兵（最大值）
    # 归并临时数组到 arr[l..r]
    i, j, k = 0, 0, p  # 初始化变量 i, j, k
    while k <= r:
        # 当左边数组到达哨兵值时，i不再增加，直到右边数组读取完剩余值，同理右边数组也一样
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1


def merge_sort(arr, p, r):
    if p >= r:
        return
    q = (p + r) >> 1
    merge_sort(arr, p, q)
    merge_sort(arr, q + 1, r)
    merge(arr, p, q, r)


if __name__ == "__main__":
    # array = [3, 4, 2, 1, 5, 6, 7, 9, 10, 8]
    array = [5, 0, 4, 2, 3, 1, 3, 3, 3, 6, 8, 7]
    merge_sort(array, 0, len(array) - 1)
    print(array)
