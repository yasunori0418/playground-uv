from typing import Iterator, List
import pytest


def all_patterns(nums: List[int]) -> Iterator[List[int]]:
    nums.sort()
    for one in range(len(nums) - 3):
        for two in range(one + 1, len(nums) - 2):
            for three in range(two + 1, len(nums) - 1):
                for four in range(three + 1, len(nums)):
                    yield [nums[one], nums[two], nums[three], nums[four]]


assert list(all_patterns([1, 2, 3, 4, 5, 6, 7, 8])) == [
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
]


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
        if len(nums) <= 3:
            return []
        ans = []
        nums.sort()
        for n in all_patterns(nums):
            if sum(n) == target:
                if len(ans) >= 1 and n in ans:
                    continue
                ans.append(n)
        return ans


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
        pytest.param([1, 2, 3, 4, 5, 6, 7, 8], 12, [[1, 2, 3, 6], [1, 2, 4, 5]]),
        pytest.param(
            [
                -444,
                -400,
                -398,
                -387,
                -372,
                -347,
                -340,
                -337,
                -330,
                -326,
                -326,
                -308,
                -304,
                -295,
                -270,
                -228,
                -224,
                -213,
                -196,
                -192,
                -186,
                -118,
                -103,
                -92,
                -89,
                -42,
                -31,
                -28,
                -20,
                -19,
                -8,
                1,
                1,
                9,
                48,
                49,
                74,
                88,
                90,
                135,
                152,
                160,
                170,
                181,
                181,
                202,
                238,
                254,
                271,
                272,
                274,
                285,
                287,
                302,
                314,
                319,
                342,
                373,
                373,
                392,
                400,
                453,
                482,
            ],
            -4402,
            [],
        ),
    ],
)
def test_four_sum(nums: List[int], target: int, expected: List[List[int]]):
    assert Solution().fourSum(nums, target) == expected
