from typing import Iterator, List
import pytest
import itertools


def all_patterns2(nums: List[int], target: int) -> Iterator[List[int]]:
    nums.sort()
    nl = len(nums)
    for one in range(nl - 3):
        if sum([nums[one], nums[one + 1], nums[one + 2], nums[one + 3]]) > target:
            break
        if one > 0 and nums[one] == nums[one - 1]:
            continue
        if sum([nums[one], nums[nl - 1], nums[nl - 2], nums[nl - 3]]) < target:
            continue

        for two in range(one + 1, nl - 2):
            if sum([nums[one], nums[two], nums[two + 1], nums[two + 2]]) > target:
                break
            if sum([nums[one], nums[two], nums[nl - 1], nums[nl - 1]]) < target:
                continue
            if two > one + 1 and nums[two] == nums[two - 1]:
                continue

            left = two + 1
            right = nl - 1
            while True:
                yield [nums[one], nums[two], nums[left], nums[right]]


def all_patterns(nums: List[int]) -> Iterator[List[int]]:
    nums.sort()
    for one in range(len(nums) - 3):
        for two in range(one + 1, len(nums) - 2):
            for three in range(two + 1, len(nums) - 1):
                for four in range(three + 1, len(nums)):
                    yield [nums[one], nums[two], nums[three], nums[four]]


assert list(itertools.combinations([1, 2, 3, 4, 5, 6, 7, 8], 4)) == [
    (1, 2, 3, 4),
    (1, 2, 3, 5),
    (1, 2, 3, 6),
    (1, 2, 3, 7),
    (1, 2, 3, 8),
    (1, 2, 4, 5),
    (1, 2, 4, 6),
    (1, 2, 4, 7),
    (1, 2, 4, 8),
    (1, 2, 5, 6),
    (1, 2, 5, 7),
    (1, 2, 5, 8),
    (1, 2, 6, 7),
    (1, 2, 6, 8),
    (1, 2, 7, 8),
    (1, 3, 4, 5),
    (1, 3, 4, 6),
    (1, 3, 4, 7),
    (1, 3, 4, 8),
    (1, 3, 5, 6),
    (1, 3, 5, 7),
    (1, 3, 5, 8),
    (1, 3, 6, 7),
    (1, 3, 6, 8),
    (1, 3, 7, 8),
    (1, 4, 5, 6),
    (1, 4, 5, 7),
    (1, 4, 5, 8),
    (1, 4, 6, 7),
    (1, 4, 6, 8),
    (1, 4, 7, 8),
    (1, 5, 6, 7),
    (1, 5, 6, 8),
    (1, 5, 7, 8),
    (1, 6, 7, 8),
    (2, 3, 4, 5),
    (2, 3, 4, 6),
    (2, 3, 4, 7),
    (2, 3, 4, 8),
    (2, 3, 5, 6),
    (2, 3, 5, 7),
    (2, 3, 5, 8),
    (2, 3, 6, 7),
    (2, 3, 6, 8),
    (2, 3, 7, 8),
    (2, 4, 5, 6),
    (2, 4, 5, 7),
    (2, 4, 5, 8),
    (2, 4, 6, 7),
    (2, 4, 6, 8),
    (2, 4, 7, 8),
    (2, 5, 6, 7),
    (2, 5, 6, 8),
    (2, 5, 7, 8),
    (2, 6, 7, 8),
    (3, 4, 5, 6),
    (3, 4, 5, 7),
    (3, 4, 5, 8),
    (3, 4, 6, 7),
    (3, 4, 6, 8),
    (3, 4, 7, 8),
    (3, 5, 6, 7),
    (3, 5, 6, 8),
    (3, 5, 7, 8),
    (3, 6, 7, 8),
    (4, 5, 6, 7),
    (4, 5, 6, 8),
    (4, 5, 7, 8),
    (4, 6, 7, 8),
    (5, 6, 7, 8),
]

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

    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
        """timelimitには勝てなかった
        :refer: https://leetcode.com/problems/4sum/solutions/5822917/optimal-solution-for-4sum-problem-using-two-pointer-technique-and-early-exits/
        """
        nums.sort()  # Sort the array first
        n = len(nums)
        result = []

        # Iterate over the first two numbers
        for i in range(n - 3):
            # Early exit if the smallest sum exceeds the target
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break

            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Early exit if the largest possible sum is less than the target
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Early exit for the second number
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break

                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue

                # Now use two pointers for the remaining two numbers
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        # Skip duplicates for the third number
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        # Skip duplicates for the fourth number
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result


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
        pytest.param(
            [
                91277418,
                66271374,
                38763793,
                4092006,
                11415077,
                60468277,
                1122637,
                72398035,
                -62267800,
                22082642,
                60359529,
                -16540633,
                92671879,
                -64462734,
                -55855043,
                -40899846,
                88007957,
                -57387813,
                -49552230,
                -96789394,
                18318594,
                -3246760,
                -44346548,
                -21370279,
                42493875,
                25185969,
                83216261,
                -70078020,
                -53687927,
                -76072023,
                -65863359,
                -61708176,
                -29175835,
                85675811,
                -80575807,
                -92211746,
                44755622,
                -23368379,
                23619674,
                -749263,
                -40707953,
                -68966953,
                72694581,
                -52328726,
                -78618474,
                40958224,
                -2921736,
                -55902268,
                -74278762,
                63342010,
                29076029,
                58781716,
                56045007,
                -67966567,
                -79405127,
                -45778231,
                -47167435,
                1586413,
                -58822903,
                -51277270,
                87348634,
                -86955956,
                -47418266,
                74884315,
                -36952674,
                -29067969,
                -98812826,
                -44893101,
                -22516153,
                -34522513,
                34091871,
                -79583480,
                47562301,
                6154068,
                87601405,
                -48859327,
                -2183204,
                17736781,
                31189878,
                -23814871,
                -35880166,
                39204002,
                93248899,
                -42067196,
                -49473145,
                -75235452,
                -61923200,
                64824322,
                -88505198,
                20903451,
                -80926102,
                56089387,
                -58094433,
                37743524,
                -71480010,
                -14975982,
                19473982,
                47085913,
                -90793462,
                -33520678,
                70775566,
                -76347995,
                -16091435,
                94700640,
                17183454,
                85735982,
                90399615,
                -86251609,
                -68167910,
                -95327478,
                90586275,
                -99524469,
                16999817,
                27815883,
                -88279865,
                53092631,
                75125438,
                44270568,
                -23129316,
                -846252,
                -59608044,
                90938699,
                80923976,
                3534451,
                6218186,
                41256179,
                -9165388,
                -11897463,
                92423776,
                -38991231,
                -6082654,
                92275443,
                74040861,
                77457712,
                -80549965,
                -42515693,
                69918944,
                -95198414,
                15677446,
                -52451179,
                -50111167,
                -23732840,
                39520751,
                -90474508,
                -27860023,
                65164540,
                26582346,
                -20183515,
                99018741,
                -2826130,
                -28461563,
                -24759460,
                -83828963,
                -1739800,
                71207113,
                26434787,
                52931083,
                -33111208,
                38314304,
                -29429107,
                -5567826,
                -5149750,
                9582750,
                85289753,
                75490866,
                -93202942,
                -85974081,
                7365682,
                -42953023,
                21825824,
                68329208,
                -87994788,
                3460985,
                18744871,
                -49724457,
                -12982362,
                -47800372,
                39958829,
                -95981751,
                -71017359,
                -18397211,
                27941418,
                -34699076,
                74174334,
                96928957,
                44328607,
                49293516,
                -39034828,
                5945763,
                -47046163,
                10986423,
                63478877,
                30677010,
                -21202664,
                -86235407,
                3164123,
                8956697,
                -9003909,
                -18929014,
                -73824245,
            ],
            -236727523,
            [
                [-79583480, -70078020, -65863359, -21202664],
                [-76072023, -59608044, -58094433, -42953023],
            ],
        ),
    ],
)
def test_four_sum(nums: List[int], target: int, expected: List[List[int]]):
    assert Solution().fourSum(nums, target) == expected
