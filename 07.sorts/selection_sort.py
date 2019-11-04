# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

from typing import List


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if (arr[min] > arr[j]): min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

arr = [3, 4, 2, 1, 5, 6, 7, 8]
selection_sort(arr)
print(arr)
