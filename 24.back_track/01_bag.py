#!/usr/bin/python


max_w = 0  # 存储背包中物品总重量的最大值
# 背包选取的物品列表
picks = []
picks_with_max_value = []


def bag(i: int, cw: int, items: list, w: int):
    """
    假设背包可承受重量 100，物品重量存储在数组 a 中，那可以这样调用函数：
    bag(0, 0, a, 100)
    :param i: 当前物品的索引
    :param cw: 当前已经装进去的物品的重量和
    :param items: 每个物品的重量
    :param w: 背包容量
    :return:
    """
    global max_w
    print(i, picks, cw)
    if cw == w or i == len(items):  # cw==w 表示装满了 ;i==n 表示已经考察完所有的物品
        if cw > max_w:
            global picks_with_max_value
            max_w = cw
            picks_with_max_value = [x for x in picks if x != 0]
            print("满足：", i, picks, cw)
        return

    # 不选第i个物品
    picks[i] = 0
    bag(i + 1, cw, items, w)
    # 选第i个物品
    ncw = cw + items[i]
    if ncw <= w:  # 已经超过可以背包承受的重量的时候，就不要再装了
        picks[i] = items[i]
        bag(i + 1, ncw, items, w)


if __name__ == '__main__':
    items_info = [3, 5, 2, 4, 1, 2, 4, 9]
    picks = [0] * len(items_info)
    w = 8
    bag(0, 0, items_info, w)
    print(picks_with_max_value, max_w)
