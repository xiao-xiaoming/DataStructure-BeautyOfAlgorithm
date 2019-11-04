# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

"""
编程列出一个任意长度字符串的全字符排序情况，原始字符串中没有重复字符
例如：
原始字符串是"abc"：
打印所有的排列permutation情况：
"abc" "acb" "bac" "bca" "cab" "cba"
"""


def permutation(chars, k):
    """
    :param chars: 字符串序列
    :param k: 未处理的字符串的起始位置
    :return:
    """
    if k == len(chars) - 1:
        for i in range(len(chars)):
            print(chars[i], end="")
        print(end=",")
    for i in range(k, len(chars)):
        chars[k], chars[i] = chars[i], chars[k]
        permutation(chars, k + 1)
        chars[k], chars[i] = chars[i], chars[k]


permutation(list("abc"), 0)
