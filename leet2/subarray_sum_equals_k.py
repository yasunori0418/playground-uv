from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        return solve(nums, k)


def solve(nums, k):
    # 辞書を初期化。キーは累積和、値はその累積和が出現した回数。
    # 空の配列は必ず一つは含まれるため、初期化時に0をセットしている
    prefix_sum_count = {0: 1}
    current_sum = 0
    result = 0

    # 配列を一つずつ走査
    for num in nums:
        # 現在の累積和を更新
        current_sum += num

        # current_sum - k が辞書に存在する場合、それは k になる部分配列があることを意味する
        # current_sum - kは過去の累積和として存在した
        # current_sumは現在の累積和
        # current_sum - (current_sum - k) = 3 - (3 - 1) = 3 - 2 = k
        if current_sum - k in prefix_sum_count:
            result += prefix_sum_count[current_sum - k]

        # 現在の累積和の出現回数を更新
        if current_sum in prefix_sum_count:
            prefix_sum_count[current_sum] += 1
        else:
            prefix_sum_count[current_sum] = 1
    return result


def solve2(nums, k):
    prefix_sums = [
        0,
    ]
    result = 0

    for n in nums:
        # 累積和をそれぞれの段階まで計算
        current_sum = prefix_sums[-1] + n

        # 最新の累積和を除いた各累積和をチェック
        for previous_sum in prefix_sums:
            if current_sum - previous_sum == k:
                result += 1

        prefix_sums.append(current_sum)

    return result


# solve([1, 1, 1], 2)
# solve([1, 2, 3], 3)
solve([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 4)


def test_solve():
    assert solve([1, 1, 1], 2) == 2
    assert solve([1, 2, 3], 3) == 2
