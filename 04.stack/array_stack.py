# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'


class ArrayStack():
    """基于数组实现的顺序栈"""

    def __init__(self, n: int):
        self.items = [None] * n  # 数组
        self.count = 0  # 栈中元素的个数
        self.n = n  # 栈的大小

    def push(self, item) -> bool:
        # 数组空间不够了，直接返回 false，入栈失败。
        if self.count == self.n:
            return False
        # 将item放到下标为count的位置，并且count加1
        self.items[self.count] = item
        self.count += 1
        return True

    def pop(self):
        # 栈为空，则直接返回 None
        if self.count == 0:
            return None
        # 返回下标为count-1的数组元素，并且栈中元素个数count减1
        tmp = self.items[self.count - 1]
        self.count -= 1
        return tmp

    def __repr__(self):
        return str(self.items[:self.count])


stack = ArrayStack(3)
for i in range(4):
    print("stack.push(%d):" % i, stack, stack.push(i))
for i in range(4):
    print("stack.pop():", stack, stack.pop())
