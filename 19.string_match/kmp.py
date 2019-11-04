# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

"""
操作流程：
- 假设现在主串 M 匹配到 i 位置，模式串 P 匹配到 j 位置
- 如果 j = -1，或者当前字符匹配成功（即 M[i] == P[j] ），都令 i++，j++，继续匹配下一个字符；
- 如果 j != -1，且当前字符匹配失败（即 M[i] != P[j] ），则令 i 不变，j = next[j]。
   匹配失败时，模式串 P相对于主串 M 向右移动了 j - next [j] 位
- 换言之，将模式串 P 失配位置的 next 数组的值对应的模式串 P 的索引位置移动到失配处
"""


def kmp(main: str, pattern: str):
    """kmp字符串匹配"""
    n, m = len(main), len(pattern)

    if m == 0:
        return 0
    if n <= m:
        return 0 if main == pattern else -1

    # 求解next数组
    next = get_next(pattern)

    i, j = 0, 0
    while i < n and j < m:
        if j == -1 or main[i] == pattern[j]:
            i += 1
            j += 1
        else:  # j!=-1 and main[i]!=pattern[j]
            j = next[j]
    if j == m:
        return i - j
    else:
        return -1


def get_next(pattern):
    """next数组生成"""
    m = len(pattern)
    next = [-1] * m
    i, j = 0, -1
    while i < m - 1:
        if j == -1 or pattern[i] == pattern[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]
    return next


# def get_maxL(pattern):
#     m = len(pattern)
#     maxL = 0
#     max_l_arr = [0] * m
#     for i in range(1, m):
#         if pattern[maxL] != pattern[i]:
#             maxL = 0
#         if pattern[maxL] == pattern[i]:
#             maxL += 1
#         max_l_arr[i] = maxL
#     return max_l_arr


def get_next_arr(pattern):
    m = len(pattern)
    maxL = 0
    next = [0] * m
    next[0] = -1
    for i in range(1, m - 1):
        if pattern[maxL] != pattern[i]:
            maxL = 0
        if pattern[maxL] == pattern[i]:
            maxL += 1
        next[i + 1] = maxL
    return next


if __name__ == '__main__':
    m_str = "aabbbbaaabbababbabbbabaaabb"
    p_str = "abbabbbabaa"

    print('--- search ---')
    print('[Built-in Functions] result:', m_str.find(p_str))
    print('[kmp] result:', kmp(m_str, p_str))

    print(get_next("abaabcac"))
    print(get_next_arr("abaabcac"))
    print(get_next("ababacd"))
    print(get_next_arr("ababacd"))
    print(get_next("abbabbbabaa"))
    print(get_next_arr("abbabbbabaa"))
