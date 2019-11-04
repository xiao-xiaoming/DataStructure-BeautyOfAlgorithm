# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

"""
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到m报数），
凡报到m的人退出圈子，直到船上仅剩 r人为止,问都有哪些编号的人下船了呢？。
假设n=30，m=9，r=15
"""


class ListNode(object):
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


n, m, r = 30, 9, 15
# 开始构建环
head = ListNode(1)
p = head
for i in range(2, n + 1):
    p.next = ListNode(i)
    p = p.next
p.next = head
# 构建完成,开始报数

result = []  # 用于保存出列顺序
p = head
count = 1  # 第一个人报的数为1
while n != r:
    prev: ListNode = p
    p = p.next
    count += 1
    # 凡报到m的人退出圈子
    if count == m:
        result.append(p.val)
        prev.next = prev.next.next
        count = 0
        n -= 1
print("报到%d的人的出列顺序：" % m, result)
