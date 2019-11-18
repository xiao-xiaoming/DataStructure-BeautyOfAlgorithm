# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import bisect
from typing import List


"""
给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。
当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
说明:
不允许旋转信封。

示例:
输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出: 3 
解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/russian-doll-envelopes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

def maxEnvelopes(envelopes: List[List[int]]) -> int:
    envelopes.sort(key=lambda a: (a[0], -a[1]))
    height = list(map(lambda x: x[1], envelopes))
    return lengthOfLIS(height)


def lengthOfLIS(nums: [int]) -> int:
    n = len(nums)
    if n <= 1: return n
    tails, res = [0] * n, 0
    for num in nums:
        i = bisect.bisect_left(tails, num, 0, res)
        tails[i] = num
        if i == res: res += 1
    return res

if __name__ == '__main__':
    print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))