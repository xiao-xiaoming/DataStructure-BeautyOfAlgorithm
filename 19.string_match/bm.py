# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'
from typing import List


def bm(main: str, pattern: str) -> int:
    n, m = len(main), len(pattern)

    if n <= m:
        return 0 if main == pattern else -1

    # bc为坏字符位置表
    bc = generate_bc(pattern)
    # suffix为好后缀匹配的{u*}位置表,prefix为前缀匹配表
    suffix, prefix = generate_gs(pattern)

    i = 0  # i表示在主串中的角标
    while i <= n - m:
        j = m - 1  # j表示在模式串中的角标
        while j >= 0 and main[i + j] == pattern[j]:
            j -= 1
        # j此时表示坏字符首次出现的位置
        if j == m - 1:  # 坏字符出现在模式串尾部，使用坏字符规则
            i += j - bc[ord(main[i + j])]
        elif j == -1:  # 已经匹配成功
            return i
        else:  # 尾部是好后缀，使用好后缀规则
            k = m - 1 - j  # 好后缀的长度
            if suffix[k] != -1:  # 整个好后缀在pattern剩余字符中仍有出现
                i += j - suffix[k] + 1
            else:
                r = k
                while r > 0 and not prefix[r]:
                    r -= 1
                i += m - r
    return -1


def generate_bc(pattern) -> List[int]:
    """生成坏字符位置表"""
    bc = [-1] * 256
    for i, c in enumerate(pattern):
        bc[ord(c)] = i
    return bc


def generate_gs(pattern) -> (List[int], List[bool]):
    m = len(pattern)
    suffix = [-1] * m
    prefix = [False] * m
    for i in range(m - 1):
        k = 1  # pattern[:i+1]和pattern的公共后缀长度
        j = i
        while j >= 0 and pattern[j] == pattern[m - k]:
            suffix[k] = j
            k += 1
            j -= 1
        if j == -1: prefix[k - 1] = True
    return suffix, prefix


if __name__ == '__main__':
    print('--- search ---')
    m_str = 'dfasdeeeetewtweyyyhtruuueyytewtweyyhtrhrth'
    p_str = 'ruuueyy'
    print('[Built-in Functions] result:', m_str.find(p_str))
    print('[bm] result:', bm(m_str, p_str))

