# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

from typing import List


# 对每个分数进行计数
def get_counts(arr: List[int]) -> List[int]:
    counts = [0] * (max(arr) + 1)
    for num in arr:
        counts[num] += 1
    return counts


# 简单的计数排序
def counting_sort_simple(arr: List[int]):
    if len(arr) <= 1: return
    counts = get_counts(arr)
    k = 0
    for i in range(len(counts)):
        count = counts[i]
        for j in range(count):
            arr[k] = i
            k += 1


# 便于获得指定数值的在有序数组中对应的存储位置
def get_sum_counts(arr: List[int]) -> List[int]:
    counts = [0] * (max(arr) + 1)
    for num in arr:
        counts[num] += 1
    for num in range(1, len(counts)):
        counts[num] += counts[num - 1]
    return counts


# 计数排序
def counting_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    if n <= 1: return arr
    counts = get_sum_counts(arr)
    r = [0] * n
    # 遍历数组arr，对于被遍历的数据去数组C中取出对应角标的值，比如遍历到3时，从数组C中取出角标为3的值7。
    # 然后把被遍历的数据放入临时数组R角标为7-1的位置中，数组C中对应角标位置的值减1。
    for i in range(len(arr), -1, -1):
        data = arr[i]
        r[counts[data] - 1] = data
        counts[data] -= 1
    return r


if __name__ == "__main__":
    a3 = [2, 5, 3, 0, 2, 3, 0, 3]
    r = counting_sort(a3)
    print(a3)
    counting_sort_simple(a3)
    print(a3)
    print(r)
