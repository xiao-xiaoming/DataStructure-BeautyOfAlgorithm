# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

from typing import Optional


class ListNode:

    def __init__(self, data: str, next=None):
        self.data = data
        self._next = next


class LinkedQueue:

    def __init__(self):
        self._head: Optional[ListNode] = None
        self._tail: Optional[ListNode] = None

    def enqueue(self, value: str):
        # 入队
        new_node = ListNode(value)
        if self._tail:
            self._tail._next = new_node
        else:
            self._head = new_node
        self._tail = new_node

    def dequeue(self) -> Optional[str]:
        """出队"""
        if self._head:
            value = self._head.data
            self._head = self._head._next
            if not self._head:
                self._tail = None
            return value

    def __repr__(self) -> str:
        values = []
        p: ListNode = self._head
        while p:
            values.append(p.data)
            p = p._next
        return "->".join(values)


if __name__ == "__main__":
    q = LinkedQueue()
    for i in range(10):
        q.enqueue(str(i))
    print(q)

    for _ in range(3):
        q.dequeue()
    print(q)

    q.enqueue("7")
    q.enqueue("8")
    print(q)
