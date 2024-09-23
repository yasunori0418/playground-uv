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
        if nums[0] == 0 and [nums[0]] == list(set(nums)):
            return [[0, 0, 0]]
        ans = []
        nums = sorted(nums)
        for i in range(1, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[0] + nums[i] + nums[j] == 0:
                    ans.append(sorted([nums[0], nums[i], nums[j]]))
        return ans


# assert Solution().threeSum([-1, 0, 1, 0]) == [[-1, 0, 1]]
# assert Solution().threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
# assert Solution().threeSum([1, 1, 1]) == []
# assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]
# assert Solution().threeSum([-1, 1, 0]) == [[-1, 0, 1]]
# assert Solution().threeSum([0, 0, 0]) == [[0, 0, 0]]
# assert Solution().threeSum([0, 1, 1]) == []


# def bisect_three_sum(nums: List[int]) -> List[List[int]]:
#     if nums[0] == 0 and [nums[0]] == list(set(nums)):
#         return [[0, 0, 0]]
#     ans = []
#     nums = sorted(nums)
#     start = 0
#     first = 1
#     last = len(nums) - 1
#     while True:
#         if first == last:
#             first += 1
#             last = len(nums) - 1
#         if first == len(nums) - 1:
#             break
#         if nums[start] + nums[first] + nums[last] == 0:
#             ans.append([nums[start], nums[first], nums[last]])
#         last -= 1
#     return ans


# assert bisect_three_sum([-1, 0, 1, 0]) == [[-1, 0, 1]]
# assert bisect_three_sum([0, 0, 0, 0]) == [[0, 0, 0]]
# assert bisect_three_sum([1, 1, 1]) == []
# assert bisect_three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]
# assert bisect_three_sum([-1, 1, 0]) == [[-1, 0, 1]]
# assert bisect_three_sum([0, 0, 0]) == [[0, 0, 0]]
# assert bisect_three_sum([0, 1, 1]) == []


class SolutionAns:
    """いろいろやって答えられなくて、見付けてきた答え"""
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return res


assert SolutionAns().threeSum([-1, 0, 1, 0]) == [[-1, 0, 1]]
assert SolutionAns().threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
assert SolutionAns().threeSum([1, 1, 1]) == []
assert SolutionAns().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert SolutionAns().threeSum([-1, 1, 0]) == [[-1, 0, 1]]
assert SolutionAns().threeSum([0, 0, 0]) == [[0, 0, 0]]
assert SolutionAns().threeSum([0, 1, 1]) == []
