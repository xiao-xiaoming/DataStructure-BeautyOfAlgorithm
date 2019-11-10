#!/usr/bin/python
__author__ = 'xiaoxiaoming'

from collections import deque

import pygraphviz as pgv


class ACNode:
    def __init__(self, c):
        self.data = c
        # 使用有序数组，降低空间消耗，支持更多字符
        self.children = []
        self.is_ending_char = False
        self.fail = None
        self.length = 0

    def insert_child(self, c):
        """插入一个子节点"""
        node = ACNode(c)
        idx = self.binary_search(c)
        if idx < 0: idx = -(idx + 1)
        self.children.insert(idx, node)
        return node

    def binary_search(self, c):
        """二分查找，找到有序数组的插入位置"""
        start, end = 0, len(self.children) - 1
        v = ord(c)
        while start <= end:
            mid = (start + end) >> 1
            if v == ord(self.children[mid].data):
                return mid
            elif v < ord(self.children[mid].data):
                end = mid - 1
            else:
                start = mid + 1
        return -(start + 1)  # 找不到返回插入点位置

    def has_child(self, c) -> bool:
        return self.get_child(c) is not None

    def get_child(self, c):
        """搜索子节点并返回"""
        idx = self.binary_search(c)
        if idx >= 0:
            return self.children[idx]
        else:
            return None  # 找不到返回None

    def __repr__(self):
        return 'node value: %s' % self.data + '\n' \
               + 'children:%s' % self.children


class ACTrie:
    def __init__(self, text_list=None):
        if text_list is None:
            text_list = []
        self.root = ACNode(None)
        self.insert_list(text_list)
        self.build_failure_pointer()

    def insert_list(self, text_list):
        """批量插入节点"""
        for text in text_list:
            self.insert(text)
        self.build_failure_pointer()

    def insert(self, text: str):
        node = self.root
        for char in text:
            tmp = node.get_child(char)
            if tmp is None: tmp = node.insert_child(char)
            node = tmp
        node.is_ending_char = True
        node.length = len(text)

    def find(self, pattern: str) -> bool:
        p = self.root
        for char in pattern:
            child = p.get_child(char)
            if child is None: return False
            p = child
        return p.is_ending_char

    def build_failure_pointer(self):
        queue = deque()
        queue.append(self.root)
        while queue:
            p: ACNode = queue.popleft()
            for pc in p.children:
                if pc is None:
                    continue
                if p == self.root:
                    pc.fail = self.root
                else:
                    q: ACNode = p.fail
                    while q:
                        qc = q.get_child(pc.data)
                        if qc:
                            pc.fail = qc
                            break
                        q = q.fail
                    if q is None:
                        pc.fail = self.root
                queue.append(pc)

    def match(self, text: str) -> list:
        """返回该字符串所有匹配的起始角标和字符串长度"""
        result = []
        p: ACNode = self.root
        for i, c in enumerate(text):
            p.get_child(c)
            while not p.has_child(c) and p != self.root:
                p = p.fail
            p = p.get_child(c)
            if p is None: p = self.root
            tmp = p
            while tmp != self.root:
                if tmp.is_ending_char:
                    result.append((i - tmp.length + 1, tmp.length))
                tmp = tmp.fail
        return result

    def sensitive_word_filtered(self, text: str) -> str:
        filter_range_list = self.match(text)
        str_list = list(text)
        for start, length in filter_range_list:
            for i in range(start, start + length):
                str_list[i] = "*"
        return "".join(str_list)

    def draw_img(self, img_name='ACTrie.png'):
        """ 画出trie树 """
        tree = pgv.AGraph(directed=True, strict=True)
        map = {}
        nid = 0
        tree.add_node(nid, color='black', label='None')
        map[self.root] = nid
        queue = deque([(self.root, nid)])

        while queue:
            n, pid = queue.popleft()
            for node in n.children:
                nid += 1
                queue.append((node, nid))
                map[node] = nid
                color = 'red' if node.is_ending_char else 'black'
                tree.add_node(nid, color=color, label=node.data, fontcolor="white", style="filled",
                              fontname="Microsoft YaHei", shape="circle", margin=0)
                tree.add_edge(pid, nid, color="blue")
                fail = node.fail
                if fail != self.root:
                    tree.add_edge(nid, map[fail], color="green")

        tree.graph_attr['epsilon'] = '0.01'
        tree.layout('dot')
        tree.draw(img_name)


if __name__ == '__main__':
    trie = ACTrie(['fuck', 'shit', 'hit', 'TMD', '傻叉'])
    trie.draw_img()
    m_str = 'fuck you, what is that shit, TMD你就是个傻叉傻叉傻叉叉'

    filtered = trie.sensitive_word_filtered(m_str)
    print(f'original str:{m_str}')
    print(f'after filtered:{filtered}')
