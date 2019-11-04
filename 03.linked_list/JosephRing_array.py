# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'
"""
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到m报数），
凡报到m的人退出圈子，直到船上仅剩 r人为止,问都有哪些编号的人下船了呢？。
假设n=30，m=9，r=15
"""

n, m, r = 30, 9, 15
circle = list(range(1, n + 1))
# index+1代表当前报数的人在剩余报数人群中的编号
index = 0
result = []
while len(circle) > r:
    index += m - 1
    if (index >= len(circle)):
        index -= len(circle)
    result.append(circle.pop(index))
print("报到%d的人的出列顺序：" % m, result)
