# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'


class Heap:
    def __init__(self, heap_arr=None, type="max", sort_key=lambda x: x):
        if type == "min":
            self.cmp = lambda x, y: sort_key(x) < sort_key(y)
        else:
            self.cmp = lambda x, y: sort_key(x) > sort_key(y)

        if heap_arr is None:
            heap_arr = []
        self.heap_arr = heap_arr  # 从下标0开始存储数据
        self.index = len(heap_arr) - 1  # 堆中最后一个元素的下标
        self.rebuild_heap()

    def __len__(self):
        return self.index + 1

    def rebuild_heap(self):
        """堆的构建角标从0开始，
            0
            1 2
            3 4 5 6
            7 8 9 10 11 12 13 14
            最后一层叶子节点不需要进行堆化，故只要不是满二叉树，i//2就能从上层开始
            """
        for i in range((self.index - 1) >> 1, -1, -1):
            # 从数组最后一个元素开始依次从上往下堆化
            self.heapify_up_to_down(self.index, i)

    def sort(self):
        for k in range(self.index, -1, -1):
            self.heap_arr[0], self.heap_arr[k] = self.heap_arr[k], self.heap_arr[0]
            self.heapify_up_to_down(k - 1, 0)

    def insert(self, data):
        self.index += 1
        if self.index == len(self.heap_arr):
            self.heap_arr.append(data)
        else:
            self.heap_arr[self.index] = data
        self.heapify_down_to_top(self.index)

    def heapify_down_to_top(self, i):
        """自下往上堆化"""
        while ((i - 1) >> 1) >= 0 and self.cmp(self.heap_arr[i], self.heap_arr[(i - 1) >> 1]):
            # 交换下标为 i 和 父节点 i-1/2 的两个元素
            j = (i - 1) >> 1
            self.heap_arr[i], self.heap_arr[j] = self.heap_arr[j], self.heap_arr[i]
            i = (i - 1) >> 1

    def heapify_up_to_down(self, n: int, i: int):
        """自上往下堆化"""
        pos = i
        while True:
            if i * 2 + 1 <= n and self.cmp(self.heap_arr[i * 2 + 1], self.heap_arr[i]):
                pos = i * 2 + 1
            if i * 2 + 2 <= n and self.cmp(self.heap_arr[i * 2 + 2], self.heap_arr[pos]):
                pos = i * 2 + 2
            if pos == i:
                break
            self.heap_arr[i], self.heap_arr[pos] = self.heap_arr[pos], self.heap_arr[i]
            i = pos

    def update_top(self, data):
        self.heap_arr[0] = data
        self.heapify_up_to_down(self.index, 0)

    def remove_top(self):
        if self.index == -1:
            return
        tmp = self.heap_arr[0]
        self.heap_arr[0] = self.heap_arr[self.index]
        self.index -= 1
        self.heapify_up_to_down(self.index, 0)
        return tmp

    def get_top(self):
        if self.index == -1: return None
        return self.heap_arr[0]

    def get_all(self):
        return self.heap_arr[:self.index + 1]

    def __repr__(self):
        return str(self.heap_arr[:self.index + 1])


if __name__ == "__main__":
    # 数组的第一个元素不存储数据
    a = [6, 3, 4, 0, 9, 2, 7, 5, -2, 8, 1, 6, 10]
    heap = Heap(a, type="max")
    heap.sort()
    print(heap.get_all())
    heap = Heap(a, type="min")
    heap.sort()
    print(heap.get_all())
    heap = Heap(type="min")
    k = 3
    for e in a:
        if heap.index == k:
            if e > heap.get_top():
                heap.update_top(e)
        else:
            heap.insert(e)
    print(heap.get_all())
