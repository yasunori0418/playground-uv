"""1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
整数 nums の配列と整数 target を指定すると、合計が target になるような 2 つの数値のインデックスを返します。
各入力にはソリューションが 1 つだけ存在し、同じ要素を 2 回使用することはできないと想定できます。
回答は任意の順序で返すことができます。
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def two_sum_another(self, nums: List[int], target: int) -> List[int]:
        """
        二分探索っぽいことしようとしたけど、ソートできないからパフォーマンスチューニングにならん…
        """
        left = 0
        right = len(nums) - 1
        while True:
            if left == right:
                left += 1
                right = len(nums) - 1
                continue
            if nums[left] + nums[right] == target:
                return [left, right]
            right -= 1
