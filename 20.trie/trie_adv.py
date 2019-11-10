#!/usr/bin/python
__author__ = 'xiaoxiaoming'

from collections import deque

import pygraphviz as pgv


class TrieNode:
    def __init__(self, c):
        self.data = c
        # 使用有序数组，降低空间消耗，支持更多字符
        self.children = []
        self.is_ending_char = False

    def insert_child(self, c):
        """插入一个子节点"""
        node = TrieNode(c)
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

    def has_child(self, c):
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


class Trie:
    def __init__(self, text_list=None):
        if text_list is None:
            text_list = []
        self.root = TrieNode(None)
        self.insert_list(text_list)

    def insert_list(self, text_list):
        """批量插入节点"""
        for text in text_list:
            self.insert(text)

    def insert(self, text: str):
        node = self.root
        for char in text:
            tmp = node.get_child(char)
            if tmp is None: tmp = node.insert_child(char)
            node = tmp
        node.is_ending_char = True

    def find(self, pattern: str) -> bool:
        p = self.root
        for char in pattern:
            child = p.get_child(char)
            if child is None: return False
            p = child
        return p.is_ending_char

    def draw_img(self, img_name='Trie.png'):
        """ 画出trie树 """

        tree = pgv.AGraph(directed=True, strict=True)
        nid = 0
        tree.add_node(nid, color='black', label='None')
        queue = deque([(self.root, nid)])
        while queue:
            n, pid = queue.popleft()
            for c in n.children:
                nid += 1
                queue.append((c, nid))
                color = 'red' if c.is_ending_char else 'black'
                tree.add_node(nid, color=color, label=c.data, fontcolor="white", style="filled",
                              fontname="Microsoft YaHei", shape="circle", margin=0)
                tree.add_edge(pid, nid, color="blue")

        tree.graph_attr['epsilon'] = '0.01'
        tree.layout('dot')
        tree.draw(img_name)


if __name__ == '__main__':
    string_list = ['abc', 'abd', 'abcc', 'accd', 'acml', 'P@trick', 'data', 'structure', 'algorithm']

    trie = Trie(string_list)
    trie.insert_list(string_list)
    trie.draw_img()

    print('--- search result ---')
    search_string = ['a', 'ab', 'abc', 'abcc', 'abe', 'P@trick', 'P@tric', 'Patrick']
    for ss in search_string:
        print('[pattern]: {}'.format(ss), '[result]: {}'.format(trie.find(ss)))
