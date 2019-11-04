# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

from typing import Optional, List


class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


# 前序遍历
def pre_order(root: Optional[TreeNode]):
    if root:
        yield root.val
        yield from pre_order(root.left)
        yield from pre_order(root.right)


# 中序遍历
def in_order(root: Optional[TreeNode]):
    if root:
        yield from in_order(root.left)
        yield root.val
        yield from in_order(root.right)


# 后序遍历
def post_order(root: Optional[TreeNode]):
    if root:
        yield from post_order(root.left)
        yield from post_order(root.right)
        yield root.val


from collections import deque


# 层级遍历
def layer_order(root: TreeNode):
    if not root: return
    queue = deque([root])
    while queue:
        e: TreeNode = queue.popleft()
        yield e.val
        if e.left: queue.append(e.left)
        if e.right: queue.append(e.right)


def level_order(root: TreeNode) -> List[List]:
    levels = []
    if not root:
        return levels
    level = 0
    queue = deque([root])
    while queue:
        levels.append([])
        for i in range(len(queue)):
            node = queue.popleft()
            levels[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1

    return levels


# 根节点高度=max(左子树高度，右子树高度)+1
def get_level(node: TreeNode) -> int:
    if node is None: return 0
    return max(get_level(node.left), get_level(node.right)) + 1


if __name__ == "__main__":
    root = TreeNode("root")

    l1 = TreeNode("l1")
    r1 = TreeNode("r1")

    l1_l2 = TreeNode("l1_l2")
    l1_r2 = TreeNode("l1_r2")
    r1_l2 = TreeNode("r1_l2")
    r1_r2 = TreeNode("r1_r2")

    l1_l2_l3 = TreeNode("l1_l2_l3")
    l1_l2_r3 = TreeNode("l1_l2_r3")
    l1_r2_l3 = TreeNode("l1_r2_l3")
    l1_r2_r3 = TreeNode("l1_r2_r3")
    r1_l2_l3 = TreeNode("r1_l2_l3")
    r1_l2_r3 = TreeNode("r1_l2_r3")
    r1_r2_l3 = TreeNode("r1_r2_l3")
    r1_r2_r3 = TreeNode("r1_r2_r3")

    root.left, root.right = l1, r1
    l1.left, l1.right = l1_l2, l1_r2
    r1.left, r1.right = r1_l2, r1_r2
    l1_l2.left, l1_l2.right = l1_l2_l3, l1_l2_r3
    l1_r2.left, l1_r2.right = l1_r2_l3, l1_r2_r3
    r1_l2.left, r1_l2.right = r1_l2_l3, r1_l2_r3
    r1_r2.left, r1_r2.right = r1_r2_l3, r1_r2_r3

    print(list(pre_order(root)))
    print(list(in_order(root)))
    print(list(post_order(root)))
    print(list(layer_order(root)))
    print(level_order(root))
    print(get_level(root))
