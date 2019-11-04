# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'


def shell_sort(arr):
    incr = len(arr) // 2
    while incr > 0:
        # i 表示待插入元素角标，arr[0:i:incr]将作为有序序列
        # 例如有序序列角标为{0，incr,2*incr,...,i-incr},待插入元素角标为i,{n*incr}
        for i in range(incr, len(arr), incr):
            key = arr[i]  # 待插入元素，arr[0:i:incr]作为有序序列
            j = i - incr  # j指向有序序列的末端
            while j >= 0 and arr[j] > key:
                arr[j + incr] = arr[j]
                j -= incr
            arr[j + incr] = key
        incr //= 2

