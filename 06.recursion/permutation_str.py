# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

"""
编程列出一个任意长度字符串的全字符排序情况，原始字符串中没有重复字符
例如：
原始字符串是"abc"：
打印所有的排列permutation情况：
"abc" "acb" "bac" "bca" "cab" "cba"
"""


def permutationStr(str):
    result = []

    def permutation(chars, begin):
        if begin == len(chars):
            result.append("".join(chars))
            return
        for j in range(begin, len(chars)):
            chars[begin], chars[j] = chars[j], chars[begin]
            permutation(chars, begin + 1)
            chars[begin], chars[j] = chars[j], chars[begin]

    permutation(list(str), 0)
    return result


print(permutationStr("abcd"))
