from typing import List
from statistics import median


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median(sorted_array_merge(nums1, nums2))


def sorted_array_merge(nums1: List[int], nums2: List[int]) -> List[int]:
    return sorted(nums1 + nums2)


assert sorted_array_merge([1, 3], [2]) == [1, 2, 3]
assert sorted_array_merge([1, 2], [3, 4]) == [1, 2, 3, 4]
assert Solution().findMedianSortedArrays([1, 3], [2]) == 2.0
assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
