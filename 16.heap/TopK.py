# -*- coding: utf-8 -*-
from typing import Optional

__author__ = 'xiaoxiaoming'

from Heap import Heap


class TopK:
    def __init__(self, arr: Optional[list] = None, k: int = 10, sort_key=lambda x: x):
        self.k = k
        self.sort_key = sort_key
        self.min_heap = Heap(type="min", sort_key=sort_key)
        if arr:
            for e in arr:
                self.insert(e)

    def insert(self, data):
        if self.min_heap.index == self.k:
            if self.sort_key(data) > self.sort_key(self.min_heap.get_top()):
                self.min_heap.update_top(data)
        else:
            self.min_heap.insert(data)

    def __repr__(self):
        return str(self.min_heap.get_all())


a = [0, 6, 3, 4, 0, 9, 2, 7, 5, -2, 8, 1, 6, 10]
top3 = TopK(arr=a, k=3)
print(top3)
top3.insert(34)
print(top3)
