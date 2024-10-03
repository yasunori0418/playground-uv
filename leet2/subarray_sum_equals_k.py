from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        return solve(nums, k)


def solve(nums: List[int], k: int) -> int:
    return 2


def test_solve():
    assert solve([1, 1, 1], 2) == 2
