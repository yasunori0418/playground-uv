"""53. Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.
A subarray is a contiguous non-empty sequence of elements within an array.
整数配列 nums を指定すると、最大の合計を持つ部分配列を見つけて、その合計を返します。
サブ配列は、配列内の連続した空ではない要素のシーケンスです。
"""


def solve(nums: list[int]) -> int:
    if not nums:
        return 0  # 配列が空の場合は0を返す

    # 初期化: 最初の要素をcurrent_sumとmax_sumに設定
    current_sum = max_sum = nums[0]

    # 配列の2番目の要素から順に処理
    for num in nums[1:]:
        # current_sumを更新: 現在の要素を新たな部分配列の開始とするか、既存に追加するか
        current_sum = max(num, current_sum + num)
        # max_sumを更新
        max_sum = max(max_sum, current_sum)

    return max_sum


assert solve([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert solve([1]) == 1
