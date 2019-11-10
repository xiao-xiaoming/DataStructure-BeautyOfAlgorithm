# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import sys


def double11advance(items_info: list, w: int):
    """
    动态规划解决双11凑单问题
    :param items_info: 每个商品价格
    :param w: 满减条件，比如 200
    :return:
    """
    n = len(items_info)
    # 超过 3 倍就没有薅羊毛的价值了
    states = [[False] * (3 * w + 1) for i in range(n)]
    states[0][0] = True
    states[0][items_info[0]] = True
    for i in range(1, n):
        for j in range(3 * w + 1):
            if states[i - 1][j]:
                # 不购买第i个商品
                states[i][j] = states[i - 1][j]
                # 购买第i个商品
                nw = j + items_info[i]
                if nw <= 3 * w:
                    states[i][nw] = True
    j = w
    while j < 3 * w + 1 and not states[n - 1][j]:
        j += 1
    # j是大于等于 w 的最小值
    if j == 3 * w + 1: return  # 没有可行解
    for i in range(n - 1, 0, -1):
        if j - items_info[i] >= 0 and states[i - 1][j - items_info[i]]:
            print(items_info[i], end=" ")
            j -= items_info[i]
    if j != 0: print(items_info[0], end="")
    print()


def double11advance2(items: list, w: int) -> list:
    global mem, min_w, picks, picks_with_min_value
    # 存储背包中物品总重量的最小值
    min_w = sys.maxsize
    # 背包选取的物品列表
    picks_with_min_value = []
    picks = [False] * len(items)
    mem = set()

    def double11advance_back_track(i: int, cp: int, items: list, p: int):
        """
        回溯算法解决双11凑单问题
        :param i: 当前商品的索引
        :param cp: 选购的商品总价格
        :param items: 每个商品的价格
        :param p: 满减条件，比如 200
        :return:
        """
        global mem, min_w, picks
        n = len(items)
        # 已经考察完所有的物品 或 选购的商品总价格已经超过之前计算情况,接下来不管选不选都不会产生最优解
        if i == n or cp >= min_w:
            if p <= cp < min_w:
                global picks_with_min_value
                min_w = cp
                picks_with_min_value = [items[i] for i in range(n) if picks[i]]
            return
        # 当前状态若已经计算则不计算，未计算则记录当前状态避免下次重复计算
        if (i, cp) in mem: return
        mem.add((i, cp))
        # 不选第i个商品
        picks[i] = False
        double11advance_back_track(i + 1, cp, items, p)
        # 选第i个商品
        picks[i] = True
        double11advance_back_track(i + 1, cp + items[i], items, p)

    double11advance_back_track(0, 0, items, w)
    return picks_with_min_value


if __name__ == '__main__':
    items_info = [2, 2, 4, 6, 3]
    print(items_info)
    capacity = 7
    double11advance(items_info, capacity)

    picks_with_min_value = double11advance2(items_info, capacity)
    print(picks_with_min_value, sum(picks_with_min_value))
