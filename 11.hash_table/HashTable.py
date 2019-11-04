# -*- coding: utf-8 -*-
import random
from typing import List, Optional

__author__ = 'xiaoxiaoming'


class Entry:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next


class HashTable:
    def __init__(self):
        self.DEFAULT_INITAL_CAPACITY = 8  # 散列表默认长度
        self.LOAD_FACTOR = 0.75  # 装载因子
        self.size = 0  # 实际元素数量
        self.use = 0  # 散列表索引数量
        self.table: List[Optional[Entry]] = [None] * self.DEFAULT_INITAL_CAPACITY  # 初始化散列表数组

    def hash(self, key) -> int:
        """散列函数"""
        if key is None:
            return 0
        else:
            h = hash(key)
            return (h ^ (h >> 16)) & (len(self.table) - 1)

    def put(self, key, value):
        index: int = self.hash(key)
        # 位位置未被引用，创建哨兵节点
        if self.table[index] is None:
            self.table[index] = Entry(None, None, None)
        p: Entry = self.table[index]
        # 新增节点
        if p.next is None:
            p.next = Entry(key, value, None)
            self.size += 1
            self.use += 1
            if self.use >= len(self.table) * self.LOAD_FACTOR:
                self.resize()
        else:  # 链表法解决散列冲突
            while True:
                p = p.next
                # key相同，覆盖旧的数据
                if p.key == key:
                    p.value = value
                    return
                if p.next is None:
                    break
            self.table[index].next = Entry(key, value, self.table[index].next)
            self.size += 1

    def resize(self):
        old_table: List[Entry] = self.table
        self.table = [None] * (len(old_table) << 1)
        self.use = 0
        for e in old_table:
            p: Entry = e
            if p is None or p.next is None: continue
            while p.next:
                p = p.next
                index: int = self.hash(p.key)
                if self.table[index] is None:
                    # 创建哨兵节点
                    self.table[index] = Entry(None, None, None)
                    self.use += 1
                self.table[index].next = Entry(p.key, p.value, self.table[index].next)

    def remove(self, key):
        index = self.hash(key)
        e = self.table[index]
        if e is None or e.next is None: return
        while True:
            pre = e
            e = e.next
            if key == e.key:
                pre.next = e.next
                self.size -= 1
                return
            if e.next is None: break

    def get(self, key):
        index = self.hash(key)
        e: Entry = self.table[index]
        if e is None or e.next is None: return None
        while e.next:
            e = e.next
            if key == e.key: return e.value
        return None

    def __repr__(self):
        result = []
        for p in self.table:
            if p is None or p.next is None: continue
            while p.next:
                p = p.next
                result.append("%s:%s" % (p.key, p.value))
        return "{%s}" % ", ".join(result)


if __name__ == "__main__":
    map = HashTable()
    for i in range(100):
        map.put(random.randrange(1, 101), i)
    print(map.get(67))
    print(map)
    for i in range(5, 96):
        map.remove(i)
    print(map)
