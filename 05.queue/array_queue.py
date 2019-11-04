# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

from typing import Optional


class ArrayQueue:
    """用数组实现的队列"""

    def __init__(self, capacity: int):
        self.items: list = [None] * capacity
        self.capacity = capacity
        self.head = 0  # 队头下标
        self.tail = 0  # 队尾下标

    def enqueue(self, item: str) -> bool:
        """入队"""
        if self.tail == self.capacity:
            return False
        self.items[self.tail] = item
        self.tail += 1
        return True

    def dequeue(self) -> Optional[str]:
        """出队"""
        if self.head == self.tail:
            return None
        item = self.items[self.head]
        self.head += 1
        return item

    def __repr__(self) -> str:
        return str(self.items[self.head:self.tail])


if __name__ == "__main__":
    q = ArrayQueue(10)
    for i in range(10):
        q.enqueue(str(i))
    print(q)

    for _ in range(3):
        q.dequeue()
    print(q)

    q.enqueue("7")
    q.enqueue("8")
    print(q)
