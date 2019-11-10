# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'


def lwst_dp(a: str, b: str) -> int:
    """
    如果：a[i]!=b[j]，min_edist(i, j)=
    min(min_edist(i-1,j)+1, min_edist(i,j-1)+1, min_edist(i-1,j-1)+1)
    如果：a[i]==b[j]，min_edist(i, j)=
    min(min_edist(i-1,j)+1, min_edist(i,j-1)+1，min_edist(i-1,j-1))
    """
    n, m = len(a), len(b)
    min_edist = [[0] * m for _ in range(n)]
    ## 初始化第一个元素
    if a[0] != b[0]:
        min_edist[0][0] = 1
    # 初始化第一行
    for j in range(1, m):
        if a[0] == b[j]:
            min_edist[0][j] = j
        else:
            min_edist[0][j] = min_edist[0][j - 1] + 1
    # 初始化第一列
    for i in range(1, n):
        if a[i] == b[0]:
            min_edist[i][0] = i
        else:
            min_edist[i][0] = min_edist[i - 1][0] + 1
    for i in range(1, n):
        for j in range(1, m):
            tmp = min_edist[i - 1][j - 1]
            if a[i] != b[j]: tmp += 1
            min_edist[i][j] = min(min_edist[i - 1][j] + 1, min_edist[i][j - 1] + 1,
                                  tmp)
    print(min_edist)
    return min_edist[-1][-1]


def lcs(a: str, b: str):
    """
    如果：a[i]==b[j]，那么：max_lcs(i, j) 就等于：
    max(max_lcs(i-1,j-1)+1, max_lcs(i-1, j), max_lcs(i, j-1))；
    如果：a[i]!=b[j]，那么：max_lcs(i, j) 就等于：
    max(max_lcs(i-1,j-1), max_lcs(i-1, j), max_lcs(i, j-1))；
    """
    n, m = len(a), len(b)
    # 第0行和第0列作为哨兵元素
    max_lcs = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            max_lcs[i][j] = max(max_lcs[i - 1][j], max_lcs[i][j - 1],
                                max_lcs[i - 1][j - 1] + int(a[i - 1] == b[j - 1]))
    return max_lcs[-1][-1]


if __name__ == "__main__":
    a = "mitcmu"
    b = "mtacnu"
    print(lwst_dp(a, b))
    print(lcs(a, b))

    a = "kitten"
    b = "sitting"
    print(lwst_dp(a, b))
    print(lcs(a, b))

    a = "flaw"
    b = "lawn"
    print(lwst_dp(a, b))
    print(lcs(a, b))