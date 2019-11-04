# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

"""
编程列出一个任意长度字符串的全字符排列组合情况，原始字符串中没有重复字符
例如：
原始字符串是"abc"，打印得到下列所有排列组合情况
"a" "b" "c"
"ab" "bc" "ca" "ba" "cb" "ac"
"abc" "acb" "bac" "bca" "cab" "cba"

思路分析：
每行字符个数都是递增 ，下一行的字符是建立在上一行的基础上得到的
即在将第一行字符串长度限定为1，第二行为2....，
在第一行数据基础上{a,b,c}，创建第二行数据，
遍历字符串中所字符，并与第一行数据组合。注意每行字符串长度限制
1、先将原始字符串转换成字符数组ch
2、将原始字符串每个字符添加到list集合中
3、遍历list集合用每个元素str去查找是否存在数组ch中的元素，如果ch中的字符c没有被str找到则用str+c作为新集合的值返回;
4、遍历新集合重复3步骤
"""


def permComStr(chars):
    # 将一个list用chars衍生，例如列表['a', 'b', 'c']会衍生出['ab', 'ac', 'ba', 'bc', 'ca', 'cb']
    def getDeriveList(srcList):
        if len(srcList) == 0: return list(chars)
        newList = []
        for str in srcList:
            for c in chars:
                if str.skip_list_find(c) == -1:
                    newList.append(str + c)
        return newList

    # 初始化用于衍生的list
    deriveList = []
    # 共需衍生len(chars)次
    for i in range(len(chars)):
        # 衍生list
        deriveList = getDeriveList(deriveList)
        print(" ".join(deriveList))


permComStr("abcd")
