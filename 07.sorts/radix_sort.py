# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'


def radix_sort(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    max_len = len(str(max))
    # 从个位开始（保证稳定性），对数组每一位都进行一次计数排序
    for i in range(max_len):
        exp = 10 ** i
        arr = counting_sort(arr, exp)
        print(arr)
    return arr


def counting_sort(arr, exp):
    if len(arr) <= 1: return
    # 计算每个元素的个数
    counts = [0] * 10
    for data in arr:
        counts[(data // exp) % 10] += 1
    # 计算排序后的位置
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    # 临时数组r，存储排序之后的结果
    r = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        j = (arr[i] // exp) % 10
        r[counts[j] - 1] = arr[i]
        counts[j] -= 1
    return r


if __name__ == "__main__":
    a3 = [234, 567, 123, 20, 12, 3453, 40, 93]
    print(a3)
    r = radix_sort(a3)
    print(r)
