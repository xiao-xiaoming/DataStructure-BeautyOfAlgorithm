# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'


class ListNode:
    def __init__(self, data: int, next=None):
        self._data = data
        self._next = next


class LinkedStack:
    """基于单链表实现的栈
    """

    def __init__(self):
        self._top: ListNode = None

    def push(self, value):
        # 添加元素
        new_top = ListNode(value)
        new_top._next = self._top
        self._top = new_top
        return True

    def pop(self):
        # 删除并返回栈顶元素
        value = self._top._data
        self._top = self._top._next
        return value

    def __repr__(self) -> str:
        vals = []
        p: ListNode = self._top
        while p:
            vals.append(str(p._data))
            p = p._next
        return '->'.join(vals)


if __name__ == "__main__":
    stack = LinkedStack()
    for i in range(4):
        print("stack.push(%d):" % i, stack.push(i), stack)
    for i in range(4):
        print("stack.pop():", stack.pop(), stack)
