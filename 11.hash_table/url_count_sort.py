# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

url_count_dict = {}
k = 0
with open("access.log", "r") as f:
    for line in f:
        url = line.rstrip()
        if len(url) > 0:
            value = url_count_dict.setdefault(url, 0) + 1
            url_count_dict[url] = value
            if value > k: k = value
result = []
# k不大可以使用桶排序,每个次数一个桶
if k < 10:
    buckets = []
    for i in range(k):
        buckets.append([])
    # 将数组中值分配到各个桶里
    for url, value in url_count_dict.items():
        buckets[value - 1].append(url)
    for value in range(len(buckets) - 1, -1, -1):
        for url in buckets[value]:
            result.append((url, value + 1))
else:
    result = sorted(url_count_dict.items(), key=lambda x: x[1], reverse=True)

for x in result[0:10]:
    print(x)
