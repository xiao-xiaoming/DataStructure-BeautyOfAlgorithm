# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

from typing import Optional


class DynamicArrayQueue:
    """用数组实现的队列"""

    def __init__(self, capacity: int):
        self.items: list = [None] * capacity
        self.capacity = capacity
        self.head = 0  # 队头下标
        self.tail = 0  # 队尾下标

    def enqueue(self, item: str) -> bool:
        """入队"""
        # 表示队列末尾没有空间了
        if self.tail == self.capacity:
            if self.head == 0: return False
            # 数据搬移
            for i in range(self.head, self.tail):
                self.items[i - self.head] = self.items[i]
            # 搬移完之后重新更新 head 和 tail
            self.tail -= self.head
            self.head = 0
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
    q = DynamicArrayQueue(10)
    for i in range(10):
        q.enqueue(str(i))
    print(q)

    for _ in range(3):
        q.dequeue()
    print(q)

    q.enqueue("7")
    q.enqueue("8")
    print(q)
