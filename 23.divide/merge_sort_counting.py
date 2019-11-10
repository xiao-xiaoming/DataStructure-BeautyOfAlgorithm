#!/usr/bin/python
# -*- coding: UTF-8 -*-

inversion_num = 0


def merge_sort(nums, p, r):
    if p >= r:
        return
    mid = (p + r) >> 1
    merge_sort(nums, p, mid)
    merge_sort(nums, mid + 1, r)
    merge(nums, p, mid, r)


def merge_sort_counting(nums):
    global inversion_num
    inversion_num = 0
    merge_sort(nums, 0, len(nums) - 1)


def merge(arr, p, q, r):
    global inversion_num
    i, j, k = p, q + 1, 0  # 初始化变量 i, j, k
    tmp = [0] * (r - p + 1)  # 申请一个大小跟arr[p:r+1]一样的临时数组
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            i += 1
        else:
            inversion_num += q - i + 1
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


if __name__ == '__main__':
    nums = [5, 0, 3, 1, 3, 6, 8, 7]
    merge_sort_counting(nums)
    print(f'nums  : {nums}')
    print(f'sorted: {nums}')
    print(f'inversion number: {inversion_num}')

    nums = [5, 0, 4, 2, 3, 1, 3, 3, 3, 6, 8, 7]
    merge_sort_counting(nums)
    print(f'nums  : {nums}')
    print(f'sorted: {nums}')
    print(f'inversion number: {inversion_num}')
