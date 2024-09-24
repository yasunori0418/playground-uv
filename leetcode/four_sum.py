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
def condition(nums: List[int], target: int) -> bool:
    return sum(nums) == target


assert condition([-2, -1, 1, 2], 0)
assert condition([-2, 0, 0, 2], 0)
assert condition([-1, 0, 0, 1], 0)
assert not condition([-1, 0, 0, 2], 0)


def all_patterns(nums: List[int]) -> Iterator[List[int]]:
    nums.sort()
    for one in range(len(nums) - 3):
        for two in range(one + 1, len(nums) - 2):
            for three in range(two + 1, len(nums) - 1):
                for four in range(three + 1, len(nums)):
                    yield [nums[one], nums[two], nums[three], nums[four]]


assert not DeepDiff(
    list(all_patterns([1, 2, 3, 4, 5, 6, 7, 8])),
    [
        [1, 2, 3, 4],
        [1, 2, 3, 5],
        [1, 2, 3, 6],
        [1, 2, 3, 7],
        [1, 2, 3, 8],
        [1, 2, 4, 5],
        [1, 2, 4, 6],
        [1, 2, 4, 7],
        [1, 2, 4, 8],
        [1, 2, 5, 6],
        [1, 2, 5, 7],
        [1, 2, 5, 8],
        [1, 2, 6, 7],
        [1, 2, 6, 8],
        [1, 2, 7, 8],
        [1, 3, 4, 5],
        [1, 3, 4, 6],
        [1, 3, 4, 7],
        [1, 3, 4, 8],
        [1, 3, 5, 6],
        [1, 3, 5, 7],
        [1, 3, 5, 8],
        [1, 3, 6, 7],
        [1, 3, 6, 8],
        [1, 3, 7, 8],
        [1, 4, 5, 6],
        [1, 4, 5, 7],
        [1, 4, 5, 8],
        [1, 4, 6, 7],
        [1, 4, 6, 8],
        [1, 4, 7, 8],
        [1, 5, 6, 7],
        [1, 5, 6, 8],
        [1, 5, 7, 8],
        [1, 6, 7, 8],
        [2, 3, 4, 5],
        [2, 3, 4, 6],
        [2, 3, 4, 7],
        [2, 3, 4, 8],
        [2, 3, 5, 6],
        [2, 3, 5, 7],
        [2, 3, 5, 8],
        [2, 3, 6, 7],
        [2, 3, 6, 8],
        [2, 3, 7, 8],
        [2, 4, 5, 6],
        [2, 4, 5, 7],
        [2, 4, 5, 8],
        [2, 4, 6, 7],
        [2, 4, 6, 8],
        [2, 4, 7, 8],
        [2, 5, 6, 7],
        [2, 5, 6, 8],
        [2, 5, 7, 8],
        [2, 6, 7, 8],
        [3, 4, 5, 6],
        [3, 4, 5, 7],
        [3, 4, 5, 8],
        [3, 4, 6, 7],
        [3, 4, 6, 8],
        [3, 4, 7, 8],
        [3, 5, 6, 7],
        [3, 5, 6, 8],
        [3, 5, 7, 8],
        [3, 6, 7, 8],
        [4, 5, 6, 7],
        [4, 5, 6, 8],
        [4, 5, 7, 8],
        [4, 6, 7, 8],
        [5, 6, 7, 8],
    ],
    ignore_order=True,
)


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
