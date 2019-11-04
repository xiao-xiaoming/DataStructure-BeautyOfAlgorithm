# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'


def bf(main, pattern) -> int:
    """bf暴搜
    :param main: 主串
    :param pattern: 模式串
    :return:
    """
    n = len(main)
    m = len(pattern)

    if n <= m:
        return 0 if pattern == main else -1

    for i in range(n - m + 1):
        for j in range(m):
            if main[i + j] != pattern[j]: break
            if j == m - 1: return i
    return -1


def simple_hash(s, start, end):
    ret = 0
    for i in range(start, end + 1):
        ret += ord(s[i])
    return ret


def rk(main, pattern):
    """rk搜索算法
    :param main: 主串
    :param pattern: 模式串
    :return:
    """
    n = len(main)
    m = len(pattern)

    if n <= m:
        return 0 if pattern == main else -1

    # 子串哈希值表
    h = [0] * (n - m + 1)
    h[0] = simple_hash(main, 0, m - 1)
    for i in range(1, n - m + 1):
        h[i] = h[i - 1] - ord(main[i - 1]) + ord(main[i + m - 1])
    # 模式串哈希值
    hash_p = simple_hash(pattern, 0, m - 1)

    for i, h in enumerate(h):
        # 可能存在哈希冲突
        if h == hash_p:
            if pattern == main[i:i + m]:
                return i
    return -1


if __name__ == '__main__':
    m_str = 'thequickbrownfoxjumpsoverthelazydog'
    p_str = 'jump'
    print('[bf] result:', bf(m_str, p_str))
    print('[rk] result:', rk(m_str, p_str))
