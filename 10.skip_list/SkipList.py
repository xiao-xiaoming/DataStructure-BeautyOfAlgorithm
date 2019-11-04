# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import random


class SkipListNode(object):
    def __init__(self, val, max_level=1):
        self.data = val  # 节点存储的值
        self.forwards = [None] * max_level  # 节点对应索引层的深度


class SkipList(object):
    """
        跳表的一种实现方法。
        跳表中储存的是不重复的正整数。
    """

    def __init__(self):
        self.__MAX_LEVEL = 16  # 索引层的最大深度
        self.SKIPLIST_P = 0.5  # 索引生成层数的随机因子
        self._level_count = 1  # 跳表的深度
        self._head = SkipListNode(None, self.__MAX_LEVEL)  # 带头链表

    def find(self, val):
        p = self._head
        # 从索引的顶层, 逐层定位要查找的值
        # 索引层上下是对应的, 下层的起点是上一个索引层中小于插入值的最大值对应的节点
        for i in range(self._level_count - 1, -1, -1):
            # 同一索引层内, 查找小于插入值的最大值对应的节点
            while p.forwards[i] and p.forwards[i].data < val:
                p = p.forwards[i]
        if p.forwards[0] and p.forwards[0].data == val:
            return p.forwards[0]
        return None

    def insert(self, val):
        '''
        新增时, 通过随机函数获取要更新的索引层数,
        要对低于给定高度的索引层添加新结点的指针
        '''
        level = self.random_level()
        # 更新跳表索引层数
        if self._level_count < level: self._level_count = level
        new_node = SkipListNode(val, level)  # 申请新结点
        # cache用来缓存对应索引层中小于插入值的最大节点
        cache = [None] * level
        # 在低于随机高度的每一个索引层寻找小于插入值的节点
        p = self._head
        # 缓存每一个索引层定位小于插入值的节点
        for i in range(level - 1, -1, -1):
            while p.forwards[i] and p.forwards[i].data < val:
                p = p.forwards[i]
            cache[i] = p
        # 在小于高度的每个索引层中插入新结点
        for i in range(level):
            new_node.forwards[i] = cache[i].forwards[i]
            cache[i].forwards[i] = new_node

    def delete(self, val):
        '''
        删除时, 要将每个索引层中对应的节点都删掉
        '''
        # cache用来缓存对应索引层中小于插入值的最大节点
        cache = [None] * self._level_count
        p = self._head
        # 缓存每一个索引层定位小于插入值的节点
        for i in range(self._level_count - 1, -1, -1):
            while p.forwards[i] and p.forwards[i].data < val:
                p = p.forwards[i]
            cache[i] = p
        # 如果给定的值存在, 更新索引层中对应的节点
        if p.forwards[0] and p.forwards[0].data == val:
            for i in range(self._level_count):
                if cache[i].forwards[i] and cache[i].forwards[i].data == val:
                    cache[i].forwards[i] = cache[i].forwards[i].forwards[i]
        # 更新跳表的深度
        while self._level_count > 1 and self._head.forwards[self._level_count] == None:
            self._level_count -= 1

    def random_level(self):
        """
        一级索引中元素个数应该占原始数据的 SKIPLIST_P,二级索引中元素个数占SKIPLIST_P^2,三级索引SKIPLIST_P^3,一直到最顶层。
        每一层的晋升概率是 SKIPLIST_P。对于每一个新插入的节点，都需要调用 randomLevel 生成一个合理的层数。
        该 randomLevel 方法会随机生成 1~MAX_LEVEL 之间的数
        :return: 按概率返回 1-MAX_LEVEL中的一个值
        """
        level = 1
        while random.random() < self.SKIPLIST_P and level < self.__MAX_LEVEL:
            level += 1
        return level

    def __repr__(self):
        vals = []
        p = self._head
        while p.forwards[0]:
            vals.append(str(p.forwards[0].data))
            p = p.forwards[0]
        return '->'.join(vals)

    def print_all(self):
        for i in range(self._level_count - 1, -1, -1):
            p = self._head
            print("level:", i)
            while p.forwards[i]:
                print(str(p.forwards[i].data), end="->")
                p = p.forwards[i]
            print()


if __name__ == '__main__':
    sl = SkipList()
    for i in range(100):
        sl.insert(i)
    p = sl.find(7)
    print(p.data)
    sl.delete(37)
    print(sl)
    sl.delete(37.5)
    print(sl)
