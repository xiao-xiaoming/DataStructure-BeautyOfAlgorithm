# -*- coding: UTF-8 -*-
from collections import deque
from typing import Optional

import pygraphviz as pgv


class TreeNode:
    def __init__(self, data=None, color=None):
        self.data = data
        assert color in ['r', 'b']
        self.color = 'red' if color == 'r' else 'black'

        self.left = None
        self.right = None
        self.parent = None

    def is_black(self) -> bool:
        return self.color == 'black'

    def is_red(self) -> bool:
        return self.color == 'red'

    def set_black(self):
        self.color = 'black'

    def set_red(self):
        self.color = 'red'


class RedBlackTree:

    def __init__(self, val_list=None):
        self.tree: Optional[TreeNode] = None
        self.black_leaf = TreeNode(color='b')  # 共用的黑色叶子节点
        if val_list is None:
            val_list = []
        for n in val_list:
            self.insert(n)

    def find(self, data) -> Optional[TreeNode]:
        if self.tree is None:
            return None
        p = self.tree
        while p != self.black_leaf:
            if data < p.data:
                p = p.left
            elif data > p.data:
                p = p.right
            else:
                return p
        return None

    def insert(self, data):
        new_node = TreeNode(data, 'r')  # 新插入的节点为红色
        # 根节点
        if self.tree is None:
            self.tree = new_node
        else:
            p = self.tree  # 根节点
            while p != self.black_leaf:  # 黑色叶子节点
                pp = p  # pp表示插入点的父节点
                if data < p.data:
                    p = p.left
                elif data > p.data:
                    p = p.right
                else:
                    # raise KeyError('val:{} already exists' % data)  # 该值已存在，插入失败
                    return
            if data < pp.data:
                pp.left = new_node
            else:
                pp.right = new_node
            new_node.parent = pp
        new_node.left = new_node.right = self.black_leaf
        # 插入后调整
        self._insert_fixup(new_node)

    def _insert_fixup(self, node):
        n: TreeNode = node  # 关注节点
        while n != self.tree and n.parent.is_red():
            # 父p 叔u 祖父g
            p = self.parent(n)
            u = self.bro(p)
            g = self.parent(p)

            if u.is_red():  # case 1 叔叔节点是红色
                p.set_black()  # 父节点设置成黑色
                u.set_black()  # 叔叔节点设置成黑色
                g.set_red()  # 祖父节点设置成红色
                n = g  # 关注节点变成祖父节点
                continue
            # 往下走，说明叔叔节点是黑色
            if p == g.left:  # 父节点为祖父节点的左子结点
                if n == p.right:  # case 2 关注节点是其父节点的右子节点
                    self.rotate_l(p)  # 围绕关注节点的父节点左旋
                    n, p = p, n  # 左旋后指针交换，关注节点设置为关注节点的父节点
                # case 3 关注节点是其父节点的左子节点
                p.set_black()  # 关注节点的父节点设置为黑色
                g.set_red()  # 关注节点的祖父节点设置为红色
                self.rotate_r(g)  # 围绕关注节点的祖父节点右旋
            else:  # 父节点为祖父节点的右子结点
                if n == p.left:  # case 2 关注节点是其父节点的左子节点
                    self.rotate_r(p)  # 围绕关注节点的父节点右旋
                    n, p = p, n  # 右旋后指针交换，关注节点设置为关注节点的父节点
                # case 3 关注节点是其父节点的右子节点
                p.set_black()  # 关注节点的父节点设置为黑色
                g.set_red()  # 关注节点的祖父节点设置为红色
                self.rotate_l(g)  # 围绕关注节点的祖父节点左旋

        # 根节点强制置黑，有两种情况根节点是红色：
        # 1. 新插入时是红色
        # 2. 经过case 1调整过后变红色
        self.tree.color = 'black'

    def delete(self, data):
        n: TreeNode = self.find(data)
        if n is None:
            return
        # n的子节点个数等于2
        if self.children_count(n) == 2:
            # 寻找n的后继s
            s = n.right
            while s.left != self.black_leaf:
                s = s.left
            n.data = s.data
            # 将删除n转化为删除s
            n = s
        # n的子节点个数小于2
        if n.left == self.black_leaf:
            c = n.right
        else:
            c = n.left
        self._transplant(n, c)
        # 删除的节点是黑色，需要调整
        if n.is_black():
            self._delete_fixup(c)
        return

    def _delete_fixup(self, node):
        n = node
        while n != self.tree and n.is_black():
            p = self.parent(n)
            b = self.bro(n)
            # 左右节点对称
            if p.left == n:
                if not b.is_black():
                    b.set_black()  # case 1
                    p.set_red()  # case 1
                    self.rotate_l(p)  # case 1
                    # new bro after rotate
                    b = self.bro(n)  # case 1

                if b.left.is_black() and b.right.is_black():
                    b.set_red()  # case 2
                    n = p  # case 2
                else:
                    if b.right.is_black():
                        b.left.set_black()  # case 3
                        b.set_red()  # case 3
                        self.rotate_r(b)  # case 3
                        # new bro after rotate
                        b = self.bro(n)  # case 3

                    # 注意，因为p可能是红或黑，所以不能直接赋值颜色，只能copy
                    b.color = p.color  # case 4
                    p.set_black()  # case 4
                    b.right.set_black()  # case 4
                    self.rotate_l(p)  # case 4
                    # trick, 调整结束跳出while
                    n = self.tree  # case 4
            else:
                if not b.is_black():
                    b.set_black()  # case 1
                    p.set_red()  # case 1
                    self.rotate_r(p)  # case 1
                    # new bro after rotate
                    b = self.bro(n)  # case 1

                if b.left.is_black() and b.right.is_black():
                    b.set_red()  # case 2
                    n = p  # case 2
                else:
                    if b.left.is_black():
                        b.right.set_black()  # case 3
                        b.set_red()  # case 3
                        self.rotate_l(b)  # case 3
                        # new bro after rotate
                        b = self.bro(n)  # case 3

                    # 注意，因为p可能是红或黑，所以不能直接赋值颜色，只能copy
                    b.color = p.color  # case 4
                    p.set_black()  # case 4
                    b.left.set_black()  # case 4
                    self.rotate_r(p)  # case 4
                    # trick, 调整结束跳出while
                    n = self.tree  # case 4
        # 将n设为黑色，从上面while循环跳出，情况有两种
        # 1. n是根节点，直接无视附加的黑色
        # 2. n是红色的节点，则染黑
        n.set_black()

    def _transplant(self, n1, n2):
        """
        节点移植， n2 -> n1
        :param n1: 原节点
        :param n2: 移植节点
        :return:
        """
        if n1 == self.tree:
            if n2 != self.black_leaf:
                self.tree = n2
                n2.parent = None
            else:
                self.tree = None  # 只有删除根节点时会进来
        else:
            p = self.parent(n1)
            if p.left == n1:
                p.left = n2
            else:
                p.right = n2
            n2.parent = p

    def rotate_l(self, node):
        if node is None:
            return
        if node.right is self.black_leaf:
            return

        p = self.parent(node)
        x = node
        y = node.right

        # node为根节点时，p为None，旋转后要更新根节点指向
        if p is not None:
            if x == p.left:
                p.left = y
            else:
                p.right = y
        else:
            self.tree = y

        x.parent, y.parent = y, p

        if y.left != self.black_leaf:
            y.left.parent = x

        x.right, y.left = y.left, x

    def rotate_r(self, node):
        if node is None:
            return

        if node.left is self.black_leaf:
            return

        p = self.parent(node)
        x = node
        y = node.left

        # 同左旋
        if p is not None:
            if x == p.left:
                p.left = y
            else:
                p.right = y
        else:
            self.tree = y

        x.parent, y.parent = y, p

        if y.right is not None:
            y.right.parent = x

        x.left, y.right = y.right, x

    @staticmethod
    def bro(node):
        """
        获取兄弟节点
        """
        if node is None or node.parent is None:
            return None
        else:
            p = node.parent
            if node == p.left:
                return p.right
            else:
                return p.left

    @staticmethod
    def parent(node):
        """
        获取父节点
        """
        if node is None:
            return None
        else:
            return node.parent

    def children_count(self, node):
        """
        获取子节点个数
        """
        return 2 - [node.left, node.right].count(self.black_leaf)

    def draw_img(self, img_name='Red_Black_Tree.png'):
        """用pygraphviz画红黑树"""
        if self.tree is None:
            return

        tree = pgv.AGraph(directed=True, strict=True)

        queue = deque([self.tree])
        num = 0
        while queue:
            e = queue.popleft()
            if e != self.black_leaf:  # 黑色叶子的连线由各个节点自己画
                tree.add_node(e.data, color=e.color, fontcolor="white", style="filled",
                              fontname="Microsoft YaHei", shape="circle", margin=0)
                for c in [e.left, e.right]:
                    queue.append(c)
                    if c != self.black_leaf:
                        tree.add_edge(e.data, c.data, color="blue")
                    else:
                        num += 1
                        tree.add_node("nil%s" % num, label="Nil", color="black", fontcolor="white", style="filled",
                                      fontname="Microsoft YaHei", shape="circle", margin=0)
                        tree.add_edge(e.data, "nil%s" % num, color="blue")

        tree.graph_attr['epsilon'] = '0.01'
        tree.layout('dot')
        tree.draw(img_name)


if __name__ == '__main__':
    rbt = RedBlackTree()

    nums = list(range(1, 20))
    for num in nums:
        rbt.insert(num)

    search_num = 7
    n = rbt.find(search_num)
    if n:
        print(n.data)
    else:
        print('node {} not found'.format(search_num))

    rbt.delete(4)

    rbt.draw_img()
