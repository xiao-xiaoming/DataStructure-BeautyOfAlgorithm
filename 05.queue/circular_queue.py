# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

from typing import Optional


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity + 1
        self.items = [None] * self.capacity
        self.head = 0  # head表示队头下标
        self.tail = 0  # tail表示队尾下标

    def enqueue(self, item: str) -> bool:
        """入队"""
        if (self.tail + 1) % self.capacity == self.head:
            return False
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        return True

    def dequeue(self) -> Optional[str]:
        # 如果head == tail 表示队列为空
        if self.head == self.tail: return None
        item = self.items[self.head]
        self.head = (self.head + 1) % self.capacity
        return item

    def __repr__(self) -> str:
        if self.tail >= self.head:
            return str(self.items[self.head: self.tail])
        else:
            return str(self.items[self.head:] + self.items[:self.tail])


if __name__ == "__main__":
    q = CircularQueue(5)
    for i in range(5):
        q.enqueue(str(i))
    q.dequeue()
    q.dequeue()
    q.enqueue(str(5))
    print(q)
