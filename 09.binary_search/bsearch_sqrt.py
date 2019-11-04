# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import math


def bsearch_sqrt(num: float) -> float:
    if num < 0:
        raise ValueError
    if num ** 2 == num:
        return num
    if num < 1:
        low, high = num, 1
    else:
        low, high = 0, num
    while high - low > 0.0000001:
        mid = (high + low) / 2
        mid_v2 = mid ** 2
        if mid_v2 > num:
            high = mid
        elif mid_v2 < num:
            low = mid
        elif mid_v2 == num:
            return mid
    return round((high + low) / 2, 6)


for i in range(2001):
    num = i / 1000
    print(num, math.sqrt(num), bsearch_sqrt(num))
