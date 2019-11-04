# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'


def insertion_sort(arr):
    for i in range(1, len(arr)):
        value = arr[i]  # 待插入元素，arr[0:i-1]作为有序序列
        j = i - 1  # j指向有序序列的末端
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value # 插入数据