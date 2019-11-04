# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

from Heap import Heap


a = [0, 6, 3, 4, 0, 9, 2, 7, 5, -2, 8, 1, 6, 10]
max_heap = Heap(a)
max_heap.sort()
print(a)
