from typing import List


def shift_only_rec(nums: List, ans: int = 0) -> int:
    def is_odd(n: List) -> bool:
        return bool(list(filter(lambda v: v % 2 == 1, n)))

    if is_odd(nums):
        return ans
    nums = list(map(lambda v: v / 2, nums))
    ans += 1
    return shift_only_rec(nums, ans)


def probrem(__input1, input2) -> int:
    nums = list(map(int, input2.split()))
    return shift_only_rec(nums)


assert probrem("3", "8 12 40") == 2
assert probrem("4", "5 6 8 10") == 0
assert probrem("6", "382253568 723152896 37802240 379425024 404894720 471526144") == 8

# 提出用
# _ = input()
# nums = list(map(int, input().split()))
# print(shift_only_rec(nums))
