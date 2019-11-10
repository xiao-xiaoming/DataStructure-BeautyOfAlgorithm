# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import sys, math
from typing import Tuple


def get_distance(p1: Tuple, p2: Tuple):
    distance = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    # print(p1, p2, distance)
    return distance


def min_distance_point(nums, p, r) -> list:
    if r - p < 2: return nums[p:r + 1]
    mid = (p + r) >> 1
    pots = min_distance_point(nums, p, mid) + min_distance_point(nums, mid + 1, r)
    n = len(pots)
    min_distance = sys.maxsize
    pot1, pot2 = None, None
    for i in range(n - 1):
        for j in range(i + 1, n):
            distance = get_distance(pots[i], pots[j])
            if distance < min_distance:
                min_distance = distance
                pot1, pot2 = pots[i], pots[j]
    return [pot1, pot2]


nums = [(5, 0), (4, 2), (3, 2), (3, 1), (3, 4), (3, 6), (8, 7), (2, 3), (1, 1)]
pot = min_distance_point(nums, 0, len(nums) - 1)
p1, p2 = pot
print(pot, get_distance(p1, p2))
