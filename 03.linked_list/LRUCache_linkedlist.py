# -*- coding: utf-8 -*-
__author__ = 'xiao-xiaoming'

import random


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LRUCache:
    """
    一个 LRU 缓存
    维护了一个有序单链表，越靠近链表尾部的结点是越早之前访问的。
    """

    def __init__(self, capacity: int = 10):
        self.cap = capacity
        # 哨兵节点, 本身不存储任何数据
        self.head = ListNode(None, None)
        self.length = 0

    def __len__(self):
        return self.length

    def get(self, val: object) -> bool:
        """
        获取指定缓存数据
        思路：从链表头开始顺序遍历链表：
        1. 如果此数据之前已经被缓存在链表中了，遍历得到这个数据对应的结点，并将其从原来的位置删除，然后再插入到链表的头部。
        2. 如果此数据没有在缓存链表中，则将新的数据结点插入链表的头部：
           - 如果此时缓存已满已超过容量，则将链表尾结点删除，
        参数：
            val:要获取的数据
        返回：
            存在于缓存中，返回True，否则返回 False。
        """
        prev = None  # 用于记录尾节点的前一个节点
        p = self.head
        # 如果此数据之前已经被缓存在链表中了
        while p.next:
            if p.next.val == val:
                # 将目标节点从原来的位置删除
                dest = p.next  # dest临时保存目标节点
                p.next = dest.next
                # 将目标节点插入到头部
                self.insert_to_head(self.head, dest)
                return True
            prev = p
            p = p.next

        # 如果此数据没有缓存在链表中
        self.insert_to_head(self.head, ListNode(val))
        self.length += 1
        # 添加数据导致超过容量则要删除尾节点
        if self.length > self.cap:
            prev.next = None
        return False

    @staticmethod
    def insert_to_head(head, node):
        """将指定节点插入到头部"""
        node.next = head.next
        head.next = node

    def __repr__(self):
        vals = []
        p = self.head.next
        while p:
            vals.append(str(p.val))
            p = p.next
        return '->'.join(vals)


if __name__ == '__main__':
    cache = LRUCache(4)
    for n in range(40):
        i = random.randint(0, 7)
        print("cache.get(%d)" % i, cache.get(i), cache)
