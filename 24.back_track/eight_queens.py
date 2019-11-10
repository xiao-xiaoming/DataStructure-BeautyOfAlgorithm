# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

result = [0] * 8  # 角标代表皇后所在的行数，值存储皇后所在的列
n = 0  # 第n个满足条件的情况


def print_eight_queen(result):
    print(f"----------{str(n).zfill(2)}----------")
    for column in result:
        print(f"{'*  ' * column}Q  {'*  ' * (8 - column - 1)}")


def cal8queen(row: int = 0):
    global n
    if row == 8:
        n += 1
        print_eight_queen(result)
    for column in range(8):
        # 只有在第row行column列放置不与之前已经放置的冲突时才进行放置
        if is_ok(row, column):
            result[row] = column
            cal8queen(row + 1)


def is_ok(row, column):
    """
    校验在第row行将皇后放置在第column列是否满足条件
    通过校验的条件是第row行前面所有行，都没有与当前列相同的列数，也不在当前列的对角线上
    """
    leftup, rightup = column - 1, column + 1
    for i in range(row - 1, -1, -1):
        if column == result[i] or leftup == result[i] or rightup == result[i]:
            return False
        leftup -= 1
        rightup += 1
    return True


cal8queen(0)
