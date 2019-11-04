# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'


class ListStack():
    """基于列表实现的顺序栈"""

    def __init__(self):
        self.items = []  # 用于存储数据

    def push(self, item) -> bool:
        self.items.append(item)
        return True

    def pop(self):
        return self.items.pop()

    def __repr__(self):
        return str(self.items)


stack = ListStack()
for i in range(4):
    print("stack.push(%d):" % i, stack, stack.push(i))
for i in range(4):
    print("stack.pop():", stack, stack.pop())
