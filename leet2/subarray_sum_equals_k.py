from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        return solve(nums, k)


def solve(nums, k):
    # 辞書を初期化。キーは累積和、値はその累積和が出現した回数。
    prefix_sum_count = {0: 1}
    current_sum = 0
    result = 0

    # 配列を一つずつ走査
    for num in nums:
        # 現在の累積和を更新
        current_sum += num

        # current_sum - k が辞書に存在する場合、それは k になる部分配列があることを意味する
        if current_sum - k in prefix_sum_count:
            result += prefix_sum_count[current_sum - k]

        # 現在の累積和の出現回数を更新
        if current_sum in prefix_sum_count:
            prefix_sum_count[current_sum] += 1
        else:
            prefix_sum_count[current_sum] = 1
    return result


# solve([1, 1, 1], 2)
solve([1, 2, 3], 3)


def test_solve():
    assert solve([1, 1, 1], 2) == 2
    assert solve([1, 2, 3], 3) == 2
