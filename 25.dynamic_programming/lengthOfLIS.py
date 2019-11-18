# -*- coding: utf-8 -*-
import bisect

__author__ = 'xiaoxiaoming'

from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1: return n
    # memo用于避免冗余计算
    memo = [[-1] * n for _ in range(n + 1)]

    def lengthOfLIS_in(nums: List[int], prev_idx: int, pos: int) -> int:
        if pos == len(nums): return 0
        cache = memo[prev_idx + 1][pos]
        if cache >= 0: return cache
        taken = 0
        if prev_idx == -1 or nums[pos] > nums[prev_idx]:
            taken = lengthOfLIS_in(nums, pos, pos + 1) + 1
        no_taken = lengthOfLIS_in(nums, prev_idx, pos + 1)
        result = max(no_taken, taken)
        memo[prev_idx + 1][pos] = result
        return result

    return lengthOfLIS_in(nums, -1, 0)


def longest_increasing_subsequence(nums: List[int]) -> int:
    """
    状态定义：dp[i]的值代表nums前i个数字的最长子序列长度。
    转移方程：设 j∈[0,i)，考虑每轮计算新dp[i]时，遍历[0,i)列表区间，做以下判断：
     1.当nums[i]>nums[j]时：nums[i]可以接在 nums[j]之后，此时最长上升子序列长度为dp[j]+1；
     2.当 nums[i]<=nums[j]时：nums[i]无法接在 nums[j]之后，此情况上升子序列不成立，跳过。
    dp[i]为情况1所有结果的最大值，若没有条件1的情况，则dp[i]=1
    具体实现时，将dp[i]所有元素置1，含义是每个元素都至少可以单独成为子序列，此时长度都为1。
    最后返回dp列表最大值，即可得到全局最长上升子序列长度。
    """
    n = len(nums)
    if n <= 1: return n
    dp = [1] * n
    result = 1
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        if dp[i] > result: result = dp[i]
    return result


def lengthOfLIS_by_binary_search(nums: [int]) -> int:
    n = len(nums)
    if n <= 1: return n
    tails, res = [0] * n, 0
    for num in nums:
        low, high = 0, res - 1
        # 在tails数组中通过二分搜索查找num的插入位置
        # 可将该问题视为二分搜索的变体三：查找第一个大于等于num的元素位置，最终low的值即为插入点位置
        while low <= high:
            mid = (low + high) >> 1
            if tails[mid] >= num:
                high = mid - 1
            else:
                low = mid + 1
        tails[low] = num
        if low == res: res += 1
    return res


def maxEnvelopes(envelopes: List[List[int]]) -> int:
    envelopes.sort(key=lambda a: (a[0], -a[1]))
    height = list(map(lambda x: x[1], envelopes))
    return lengthOfLIS_by_binary_search2(height)


def lengthOfLIS_by_binary_search2(nums: [int]) -> int:
    n = len(nums)
    if n <= 1: return n
    tails, res = [0] * n, 0
    for num in nums:
        i = bisect.bisect_left(tails, num, 0, res)
        tails[i] = num
        if i == res: res += 1
    return res


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(lengthOfLIS(nums))
    print(longest_increasing_subsequence(nums))
    print(lengthOfLIS_by_binary_search(nums))
    print(lengthOfLIS_by_binary_search2(nums))
