#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List


def yh_triangle(nums: List[List[int]]) -> int:
    n = len(nums)  # 层数
    memo = [0] * n
    memo[0] = nums[0][0]
    for i in range(1, n):
        for j in range(i, -1, -1):
            if j == i:
                memo[j] = memo[j - 1] + nums[i][j]
            elif j == 0:
                memo[j] += nums[i][j]
            else:
                memo[j] = min(memo[j - 1] + nums[i][j], memo[j] + nums[i][j])
    return min(memo)


def yh_triangle_bottom_up(nums: List[List[int]]) -> int:
    n = len(nums)
    memo = nums[-1].copy()
    for i in range(n - 1, 0, -1):
        for j in range(i):
            memo[j] = min(memo[j] + nums[i - 1][j], memo[j + 1] + nums[i - 1][j])
    return memo[0]


if __name__ == '__main__':
    nums = [[3], [2, 6], [5, 4, 2], [6, 0, 3, 2], [3, 2, 1, 8, 4]]
    for num in nums:
        print(num)
    print(yh_triangle(nums))
    print(yh_triangle_bottom_up(nums))
