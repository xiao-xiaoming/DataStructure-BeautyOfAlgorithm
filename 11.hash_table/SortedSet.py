# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import random
from typing import List, Optional


class SNode(object):
    def __init__(self, key=None, value=None, level=1):
        self.key = key
        self.value = value
        self.level = level
        self.prevs = [None] * level  # 双向跳表多层前驱索引
        self.nexts = [None] * level  # 双向跳表多层后驱索引


class SortedSet:
    def __init__(self):
        self.__MAX_LEVEL = 16  # 索引层的最大深度
        self.SKIPLIST_P = 0.5  # 索引生成层数的随机因子
        self._level_count = 1  # 跳表的深度
        self.table = {}  # 散列表存储key

        self._head = SNode(level=self.__MAX_LEVEL)  # 跳表的哨兵节点

    def put(self, key, value):
        """添加数据"""
        node: SNode = self.table.get(key)
        if node is None:
            new_node = self.skip_list_insert(key, value)
            self.table[key] = new_node
        else:
            self.skip_list_delete(node)
            node.value = value
            self.skip_list_insert_node(node)

    def get(self, key):
        """获取节点数据"""
        node: SNode = self.table.get(key)
        if node is None: return None
        return node.value

    def get_value_range(self, start, end):
        """获取节点数据"""
        result = []
        node: SNode = self.skip_list_find(start)
        if node is None or node.value < start: return None
        while node and node.value <= end:
            result.append((node.nexts[0].key, node.nexts[0].value))
            node = node.nexts[0]
        return result

    def get_value_rank(self, x, y):
        """获取节点数据"""
        result = []
        p: SNode = self._head
        for i in range(1,y+1):
            p = p.nexts[0]
            if(i>=x):
                result.append((p.nexts[0].key, p.nexts[0].value))
        return result

    def remove(self, key):
        """移除节点数据"""
        node = self.table.get(key)
        if node is None: return
        self.skip_list_delete(node)
        del self.table[key]

    def skip_list_find(self, val) -> Optional[SNode]:
        """查找第一个大于等于指定值的节点并返回"""
        p = self._head
        # 从索引的顶层, 逐层定位要查找的值
        # 索引层上下是对应的, 下层的起点是上一个索引层中小于插入值的最大值对应的节点
        for i in range(self._level_count - 1, -1, -1):
            # 同一索引层内, 查找小于插入值的最大值对应的节点
            while p.nexts[i] and p.nexts[i].value < val:
                p = p.nexts[i]
        return p.nexts[0]

    def skip_list_insert(self, key, value) -> SNode:
        '''向跳表插入节点'''
        new_node: SNode = self.creat_snode(key, value)
        self.skip_list_insert_node(new_node)
        return new_node

    def skip_list_insert_node(self, node: SNode):
        level = node.level
        # cache用来缓存对应索引层中小于插入值的最大节点
        cache = [None] * level
        # 在低于随机高度的每一个索引层寻找小于插入值的节点
        p = self._head
        # 缓存每一个索引层定位小于插入值的节点
        for i in range(level - 1, -1, -1):
            while p.nexts[i] and p.nexts[i].value < node.value:
                p = p.nexts[i]
            cache[i] = p
        # 在小于高度的每个索引层中插入新结点
        for i in range(level):
            node.prevs[i] = cache[i]
            node.nexts[i] = cache[i].nexts[i]
            cache[i].nexts[i] = node

    def creat_snode(self, key, value) -> SNode:
        level = self.random_level()
        # 更新跳表索引层数
        if self._level_count < level: self._level_count = level
        node = SNode(key, value, level)  # 申请新结点
        return node

    def skip_list_delete(self, node: SNode):
        for i in range(node.level - 1, -1, -1):
            node.prevs[i] = node.nexts[i]

    def random_level(self):
        """产生随机的索引层级"""
        level = 1
        while random.random() < self.SKIPLIST_P and level < self.__MAX_LEVEL:
            level += 1
        return level

    def __repr__(self):
        return str(self.table)


