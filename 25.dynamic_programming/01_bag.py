# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

from typing import List, Tuple


def knapsack2(items_info: list, capacity: int) -> int:
    """
    固定容量的背包，计算能装进背包的物品组合的最大重量
    :param items_info: 每个物品的重量
    :param capacity: 背包容量
    :return: 最大装载重量
    """
    n = len(items_info)
    states = [False] * (capacity + 1)  # 总重量所有的可能是0~capacity，共capacity+1种情况
    states[0] = True  # 第0个物品不放入背包,此时背包重量为0
    # 第0个物品放入背包
    if items_info[0] <= capacity:
        states[items_info[0]] = True
    for i in range(1, n):
        wi = items_info[i]  # 背包中第i个物品的重量
        # 重量最大值为capacity,需确保重量j在放入wi后，总重量依然小于等于capacity
        for j in range(capacity - wi, -1, -1):
            if states[j]: states[j + wi] = True
    for i in range(capacity, -1, -1):
        if states[i]: return i
    return 0


def knapsack3(weight: list, value: list, capacity: int):
    """
    最大承重限制下，计算能装进背包的物品组合的最大价值
    :param weight:每个物品的重量
    :param value:每个物品的价值
    :param capacity:背包最大承重
    :return:最大承重限制下的最大价值
    """
    n = len(weight)
    states = [-1] * (capacity + 1)  # 总重量所有的可能是0~capacity，共capacity+1种情况
    states[0] = 0  # 第0个物品不放入背包,此时背包价值为0
    # 第0个物品放入背包
    if weight[0] <= capacity:
        states[weight[0]] = value[0]
    for i in range(1, n):
        wi = weight[i]  # 背包中第i个物品的重量
        # 重量最大值为capacity,需确保重量j在放入wi后，总重量依然小于等于capacity
        for j in range(capacity - wi, -1, -1):
            if states[j] != -1:
                v = states[j] + value[i]
                if v > states[j + wi]: states[j + wi] = v
    # 返回最大价值
    return max(states)


def knapsack3_simple(items_info: List[Tuple[int, int]], capacity: int) -> int:
    prev = [0] * (capacity + 1)
    for w, v in items_info:
        prev = [c >= w and max(prev[c], prev[c - w] + v) for c in range(capacity + 1)]
    return prev[-1]


if __name__ == '__main__':
    items_info = [2, 2, 4, 6, 3]
    capacity = 9
    print(knapsack2(items_info, capacity))

    capacity = 8
    weight = [3, 2, 1, 1, 4]
    value = [5, 2, 4, 2, 10]
    print(knapsack3(weight, value, capacity))

    items_info = [(3, 5), (2, 2), (1, 4), (1, 2), (4, 10)]
    print(knapsack3_simple(items_info, capacity))
