# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

from collections import deque
from typing import Optional, List
import pygraphviz


class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, val_list=None):
        if val_list is None:
            val_list = []
        self.tree: Optional[TreeNode] = None
        for n in val_list:
            self.insert(n)

    def find(self, data):
        p = self.tree
        while p and p.data != data:
            p = p.left if data < p.data else p.right
        return p

    def insert(self, data):
        if not self.tree:
            self.tree = TreeNode(data)
            return
        pp = None
        p = self.tree
        while p:
            pp = p
            p = p.left if p.data > data else p.right
        if pp.data > data:
            pp.left = TreeNode(data)
        else:
            pp.right = TreeNode(data)

    def delete(self, data):
        p: Optional[TreeNode] = self.tree  # p指向要删除的节点，初始化指向根节点
        pp: Optional[TreeNode] = None  # pp记录的是p的父节点
        while p and p.data != data:
            pp = p
            p = p.right if p.data < data else p.left
        if not p: return  # 没有找到

        if p.left and p.right:  # 查找右子树中最小节点
            min_p = p.right  # 记录右子树的最小节点
            min_pp = p  # minPP表示minP的父节点
            while min_p.left:
                min_pp = min_p
                min_p = min_p.left
            p.data = min_p.data  # 替换数据
            p, pp = min_p, min_pp  # p指向要删除的min_p
        #  删除节点是叶子节点或者仅有一个子节点
        child: Optional[TreeNode] = p.left if p.left else p.right
        if not pp:
            self.tree = child  # 删除的是根节点
        elif pp.left == p:
            pp.left = child
        else:
            pp.right = child

    def find_min(self) -> Optional[TreeNode]:
        if self.tree is None: return None
        p = self.tree
        while p.left:
            p = p.left
        return p

    def find_max(self) -> Optional[TreeNode]:
        if self.tree is None: return None
        p = self.tree
        while p.right:
            p = p.right
        return p

    def _in_order(self, root: Optional[TreeNode]):
        if root:
            yield from self._in_order(root.left)
            yield root.data
            yield from self._in_order(root.right)

    def in_order(self) -> list:
        if self.tree is None:
            return []
        return list(self._in_order(self.tree))

    def __repr__(self):
        return str(self.in_order())

    def __iter__(self):
        return self._in_order(self.tree)

    def draw_tree(self, img_name="binary_search_tree.png"):
        if not self.tree:
            return
        tree = pygraphviz.AGraph(directed=True, strict=True)

        queue = deque([self.tree])
        num = 0
        while queue:
            e = queue.popleft()
            for c in [e.left, e.right]:
                if c:
                    queue.append(c)
                    tree.add_edge(e.data, c.data)
                else:
                    num += 1
                    tree.add_node("nil%s" % num, label="Null")
                    tree.add_edge(e.data, "nil%s" % num)

        tree.graph_attr['epsilon'] = '0.01'
        tree.layout('dot')
        # tree.write("%s.dot" % img_name)
        tree.draw(img_name)


if __name__ == '__main__':
    nums = [4, 2, 10, 6, 1, 7, 3]
    bst = BinarySearchTree(nums)
    print(bst)
    # 插入
    bst.insert(5)
    print(bst)
    bst.draw_tree()

    print(bst.find(2).data)

    # 删除
    bst.delete(6)
    print(bst)
    bst.delete(4)
    print(bst)
    # min max
    print(bst.find_max().data)
    print(bst.find_min().data)
