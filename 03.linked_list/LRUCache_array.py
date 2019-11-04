# -*- coding: utf-8 -*-
__author__ = 'xiao-xiaoming'

import random


class LRUCache:
    '''
    通过数组array实现的简易 LRU缓存
    维护一个list，越靠近尾部表示是越早之前访问的。
    '''
    def __init__(self, capacity: int = 10):
        self.cap = capacity
        self._data = []  # 存储数据

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return str(self._data)

    def get(self, val: object) -> bool:
        """
        获取指定缓存数据
        参数：
            val:要获取的数据
        返回：
            存在于缓存中，返回True，否则返回 False。
        """
        for i in range(len(self._data)):
            if self._data[i] == val:
                self._data.insert(0, self._data.pop(i))
                return True

        # 如果此数据没有缓存在链表中
        self._data.insert(0, val)
        # 添加数据导致超过容量则要删除尾节点
        if len(self) > self.cap:
            self._data.pop(len(self)-1)
        return False


if __name__ == '__main__':
    cache = LRUCache(5)
    for n in range(40):
        i = random.randint(0, 7)
        print("cache.get(%d)" % i, cache.get(i), cache)
