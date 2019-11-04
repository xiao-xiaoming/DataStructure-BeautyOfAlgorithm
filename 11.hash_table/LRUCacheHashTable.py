# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

from typing import Optional


class DNode():
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev: Optional[DNode] = None
        self.next: Optional[DNode] = None


class LRUCacheHashTable():
    def __init__(self, capacity=10):
        self.length = 0  # 链表长度
        self.capacity = capacity  # 链表容量
        self.table = {}  # 散列表存储key
        #  创建哨兵节点
        self.head_node = DNode()
        self.tail_node = DNode()
        self.head_node.next = self.tail_node
        self.tail_node.prev = self.head_node

    def put(self, key, value):
        node: DNode = self.table.get(key)
        if node is None:
            new_node = DNode(key, value)
            self.table[key] = new_node
            self.add_node(new_node)
            self.length += 1
            if self.length > self.capacity:
                tail = self.pop_tail()
                del self.table[tail.key]
                self.length -= 1
        else:
            node.value = value
            self.move_to_head(node)

    def add_node(self, new_node: DNode):
        """将新节点加到头部"""
        new_node.next = self.head_node.next
        new_node.prev = self.head_node
        self.head_node.next.prev = new_node
        self.head_node.next = new_node

    def pop_tail(self):
        """弹出尾部数据节点"""
        node = self.tail_node.prev
        self.remove_node(node)
        return node

    @staticmethod
    def remove_node(node):
        """移除节点"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node):
        """将节点移动到头部"""
        self.remove_node(node)
        self.add_node(node)

    def get(self, key):
        """获取节点数据"""
        node: DNode = self.table.get(key)
        if node is None: return None
        self.move_to_head(node)
        return node.value

    def remove(self, key):
        """移除节点数据"""
        node = self.table.get(key)
        if node is None: return
        self.remove_node(node)
        self.length -= 1

    def __repr__(self):
        p = self.head_node.next
        result = []
        while p.next:
            result.append("%s:%s" % (p.key, p.value))
            p = p.next
        return "{%s}" % ", ".join(result)


if __name__ == "__main__":
    map = LRUCacheHashTable()
    for i in range(100):
        map.put(i, 100 - i)
    print(map)
    for i in range(5, 96):
        map.remove(i)
    map.put("aa", 1)
    print(map.get(96))
    print(map)
