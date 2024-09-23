from typing import List


class Solution:
    """16. 3Sum Closest
    Given an integer array `nums` of length `n` and an integer `target`,
    find three integers in `nums` such that the sum is closest to `target`.
    Return the sum of the three integers.
    You may assume that each input would have exactly one solution.

    ---

    長さnの整数配列numsと整数のターゲットが与えられたとき、numsの中から、和がターゲットに最も近くなるような整数を3つ求めよ。
    3つの整数の和を返せ。 各入力はちょうど1つの解を持つと仮定してもよい。
    """

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        pass


assert Solution().threeSumClosest([-1, 2, 1, -4], 1) == 2
assert Solution().threeSumClosest([0, 0, 0], 1) == 0
