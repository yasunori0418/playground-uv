from typing import List
from deepdiff import DeepDiff
import pytest


class Solution:
    """18. 4Sum
    Given an array `nums` of `n` integers, return an array of all the unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:
    `n`個の整数の配列`nums`を指定すると、次のようなすべての一意の4つ組`[nums[a], nums[b], nums[c], nums[d]]`の配列を返します。
    - `0 <= a, b, c, d < n`
    - `a`, `b`, `c`, and `d` are distinct.
    - `nums[a] + nums[b] + nums[c] + nums[d] == target`
    You may return the answer in any order.
    回答は任意の順序で返すことができます。
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        pass


@pytest.mark.parametrize(
    [
        "nums",
        "target",
        "expected",
    ],
    [
        pytest.param(
            [1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        ),
        pytest.param([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
    ],
)
def test_four_sum(nums: List[int], target: int, expected: List[List[int]]):
    assert not DeepDiff(Solution().fourSum(nums, target), expected, ignore_order=True)
