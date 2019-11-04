# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'


# 桶排序
def quick_user_sort_by_age(user_list: list, fn=lambda x: int(x)):
    n = len(user_list)
    if n <= 1: return user_list
    # 便于获得指定数值的在有序数组中对应的存储位置
    buckets = []
    for i in range(121):
        buckets.append([])
    for data in user_list:
        buckets[fn(data)].append(data)
    k = 0
    for bucket in buckets:
        for data in bucket:
            user_list[k] = data
            k += 1
