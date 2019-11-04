# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import math

from Heap import Heap


class PercentileNumber:
    def __init__(self, percentile=0.5):
        self.min_heap = Heap(type="min")
        self.max_heap = Heap(type="max")
        self.count = 0
        self.percentile = percentile

    def insert(self, data):
        self.count += 1
        if self.count == 1:
            self.max_heap.insert(data)
            return
        max_count = math.ceil(self.count * self.percentile)
        if data <= self.max_heap.get_top():
            self.max_heap.insert(data)
        else:
            self.min_heap.insert(data)
        if max_count > len(self.max_heap):
            self.max_heap.insert(self.min_heap.remove_top())
        elif max_count < len(self.max_heap):
            self.min_heap.insert(self.max_heap.remove_top())

    def get_percentile_number(self):
        return self.max_heap.get_top()


number = PercentileNumber(percentile=0.5)
for i in range(1, 101):
    number.insert(i)
    print("%s:%s" % (i, number.get_percentile_number()), end=",")
