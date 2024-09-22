from typing import List


class Solution:
    """3Sum
    Given an integer array nums,
    return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
    Notice that the solution set must not contain duplicate triplets.

    整数配列 nums を指定すると、
    `i != j`, `i != k`, `j != k`, `nums[i] + nums[j] + nums[k] == 0` となるような三つ組 `[nums[i], nums[j], nums[k]]` をすべて返す。
    ソリューション セットには重複するトリプレットが含まれてはいけないことに注意してください。
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass


assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert Solution().threeSum([-1, 1, 0]) == [[-1, 0, 1]]
assert Solution().threeSum([0, 0, 0]) == [[0, 0, 0]]
assert Solution().threeSum([0, 1, 1]) == []
