# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'


# 背包选取的物品列表
picks = []
picks_with_max_value = []


def bag(i: int, cw: int, items_info: list, w: int):
    """
    :param i: 当前物品的索引
    :param cw: 背包当前重量
    :param items_info: 物品的重量和价值信息
    :param w: 背包容量
    :return:
    """
    n = len(items_info)
    # 考察完所有物品，或中途已经装满
    if cw == w or i == n:
        global picks_with_max_value
        if get_value(items_info, picks) > get_value(items_info, picks_with_max_value):
            picks_with_max_value = picks.copy()
        return

    # 不选第i个物品
    picks[i] = 0
    bag(i + 1, cw, items_info, w)
    # 选第i个物品
    ncw = cw + items_info[i][0]
    if ncw <= w:  # 已经超过可以背包承受的重量的时候，就不要再装了
        picks[i] = 1
        bag(i + 1, ncw, items_info, w)


def get_value(items_info: list, items_picks: list):
    n = len(items_picks)
    if n == 0: return 0
    arr = [items_info[i][1] for i in range(n) if items_picks[i] == 1]
    return sum(arr)


if __name__ == '__main__':
    # [(weight, value), ...]
    items_info = [(3, 5), (2, 2), (1, 4), (1, 2), (4, 10)]
    w = 8
    picks = [0] * len(items_info)
    bag(0, 0, items_info, w)
    max_value_select_list = [items_info[i] for i in range(len(items_info)) if picks_with_max_value[i] == 1]
    print(max_value_select_list)
