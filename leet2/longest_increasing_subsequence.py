"""300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/description/
Given an integer array nums, return the length of the longest strictly increasing subsequence.
整数配列 nums を指定すると、厳密に増加する最長のサブシーケンスの長さを返します。
"""


def solve(nums: list[int]) -> int:
    if not nums:
        return 0
    nums_len = len(nums)
    dp = [1] * nums_len
    for i in range(1, nums_len):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


assert solve([10, 9, 2, 5, 3, 7, 101, 18]) == 4
assert solve([0,1,0,3,2,3]) == 4
assert solve([7,7,7,7,7,7,7]) == 1
