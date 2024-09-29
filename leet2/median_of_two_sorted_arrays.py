from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_nums = sorted(nums1 + nums2)
        nums_len = len(sorted_nums)
        median = nums_len // 2
        if nums_len % 2 == 1:
            return sorted_nums[median]
        else:
            return (sorted_nums[median - 1] + sorted_nums[median]) / 2
