# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

"""
原始字符串是"abc"：
打印组合combination情况：
"a" "b" "c" "ab" "ac" "bc" "abc"
"""
def combinationStr(string):
    temp = []
    result = []

    def combination(chars, pos, num):
        if num == 0:
            result.append("".join(temp))
            return
        if pos == len(chars):
            return
        temp.append(chars[pos])
        combination(chars, pos + 1, num - 1)
        temp.pop(len(temp) - 1)
        combination(chars, pos + 1, num)

    chars = list(string)
    for i in range(1, len(chars) + 1):
        combination(chars, 0, i)
    return result

print(combinationStr("abc"))
