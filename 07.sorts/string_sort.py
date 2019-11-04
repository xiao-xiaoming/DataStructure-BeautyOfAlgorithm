# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'


# 桶排序
def string_sort(s: str):
    # 便于获得指定数值的在有序数组中对应的存储位置
    buckets = [[], [], []]
    i = 0
    for ch in s:
        if ch.islower():
            buckets[0].append(ch)
        elif ch.isnumeric():
            buckets[1].append(ch)
        elif ch.isupper():
            buckets[2].append(ch)
        print(ch, i)
    print(buckets)
    result = []
    for bucket in buckets:
        for data in bucket:
            result.append(data)
    return "".join(result)


print(string_sort("D，a，F，B，c，A，z"))
