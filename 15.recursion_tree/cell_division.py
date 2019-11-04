# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

"""
1个细胞的生命周期是3小时，1小时分裂一次。求n小时后，容器内有多少细胞？时间复杂度是多少？
 """


def cell_division(n: int):
    if n <= 0: return 1
    if n == 1: return 2
    if n == 2: return 4
    if n == 3: return 7
    return 2 * cell_division(n - 1) - cell_division(n - 4)


for i in range(10):
    print("f(%s)=%s" % (i, cell_division(i)))
