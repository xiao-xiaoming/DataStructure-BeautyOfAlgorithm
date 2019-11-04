# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

from typing import List


def bubble_sort(arr: List[int], n: int):
    """冒泡排序，arr是数组,n表示数组长度"""
    if n <= 1: return
    for i in range(n):
        # 提前退出标志位
        flag = False
        for j in range(n - i - 1):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 交换
                flag = True  # 此次冒泡有数据交换
        if not flag: break


