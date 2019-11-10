# -*- coding: UTF-8 -*-
__author__ = 'xiaoxiaoming'

import sys
from typing import List


def coins_dp(values: List[int], w: int) -> int:
    # memo[i]表示w为i的时候，最少需要的硬币数
    memo = [0] * (w + 1)
    # 初始化支付0元需要0个硬币
    memo[0] = 0
    # 可选硬币列表从小到大排序
    values.sort()
    for i in range(1, w + 1):
        min_num = 99999  # 假设最大金额为100000
        # 假设values的值为n1,n2,n3,...
        # 故memo[i]=min(memo[i-n1], memo[i-n2], ...) + 1
        for n in values:
            if i - n < 0: break
            if min_num > memo[i - n]:
                min_num = memo[i - n]
        memo[i] = min_num + 1
    return memo[-1]


def coins_backtracking(values: List[int], w: int):
    global min_num, min_coins_list
    min_num = sys.maxsize
    memo = set()
    coins_list = []
    min_coins_list = []

    def coins_backtracking_in(values: List[int], target: int, cur_value: int, coins_count: int):
        if cur_value == target:
            global min_num, min_coins_list
            if coins_count < min_num:
                min_num = coins_count
                min_coins_list = coins_list[:coins_count]
            return
        if (cur_value, coins_count) in memo: return
        memo.add((cur_value, coins_count))
        coins_list.append(0)
        for n in values:
            ncv = cur_value + n
            if ncv <= target:
                coins_list[coins_count] = n
                coins_backtracking_in(values, target, ncv, coins_count + 1)

    coins_backtracking_in(values, w, 0, 0)
    return min_coins_list


if __name__ == '__main__':
    values = [1, 2, 5, 10, 20, 50, 100]
    for i in range(1, 501):
        print(f"{i}-{coins_dp(values, i)}", end=",")

    print()
    target = 22
    min_coins_list = coins_backtracking(values, target)
    print(min_coins_list, len(min_coins_list))
