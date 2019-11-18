# -*- coding: utf-8 -*-
__author__ = 'xiao-xiaoming'


class Array:
    """一个包装list的简单数组，支持插入、删除、按照下标随机访问操作
    数组中的数据是任意类型的
    """

    def __init__(self, capacity: int = 10):
        """初始化方法,capacity表示数组容量"""
        self._data = []
        self._capacity = capacity

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def __repr__(self):
        return str(self._data)

    def find(self, index: int) -> object:
        '''根据索引，找到数据中的元素并返回
        参数：
            index:将要查找的数据的下标
        返回：
            如果查找成功，则返回找到的数据
            如果角标越界，则返回False
        '''
        if (index < 0 or index >= len(self)):
            return -1
        return self._data[index]

    def delete(self, index: int) -> bool:
        '''根据索引，删除数组中元素.
        参数：
            index:将要删除的数据的下标
        返回：
            如果删除成功，则返回True
            如果删除失败，则返回False
        '''
        if (index < 0 or index >= len(self)):
            return False
        self._data.pop(index)
        return True

    def insert(self, index: int, value: int) -> bool:
        '''数组插入数据操作.
        参数：
            index:将要插入的下标
            value：将要插入的数据
        返回：
            如果插入成功，则返回True
            如果插入失败，则返回False
        '''
        if index < 0 or len(self) >= self._capacity:
            return False
        else:
            self._data.insert(index, value)
            return True


if __name__ == "__main__":
    array = Array(5)
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)
    assert array.insert(0, 100) is False
    print(array)
    assert len(array) == 5
    assert array.find(1) == 5
    assert array.delete(4) is True
    print(array)
    array.insert(3, 7)
    print(array)

