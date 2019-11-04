# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import math


# m表示桶的个数
def bucket_sort(arr: list, m: int):
    if len(arr) < 2: return
    # 扫描最小值和最大值
    min, max = arr[0], arr[0]
    for i in range(0, len(arr)):
        if arr[i] < min:
            min = arr[i]
        elif arr[i] > max:
            max = arr[i]
    bucket_size = math.ceil((max - min + 1) / m)
    buckets = []
    for i in range(m):
        buckets.append([])
    # 将数组中值分配到各个桶里
    for data in arr:
        bucket_index = (data - min) // bucket_size
        buckets[bucket_index].append(data)
    # 对每个桶进行排序,时间复杂度小于O(nlogn)的排序算法都可以
    k = 0
    for bucket in buckets:
        bucket.sort()
        for data in bucket:
            arr[k] = data
            k += 1


if __name__ == "__main__":
    a3 = [2, 5, 3, 0, 2, 3, 0, 3, 0, 4, 4, 5, 1, 7, 8, 9]
    print(a3)
    bucket_sort(a3, 4)
    print(a3)
