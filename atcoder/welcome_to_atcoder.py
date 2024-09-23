def welcome_atcoder(input1: int, input2: str, input3: str) -> str:
    nums = [input1] + list(map(int, input2.split()))
    return f"{sum(nums)} {input3}"

assert welcome_atcoder(1, "2 3", "test") == "6 test"
assert welcome_atcoder(72, "128 256", "myonmyon") == "456 myonmyon"


# 提出用
# nums = [int(input())] + list(map(int, input().split()))
# print(f"{sum(nums)} {input()}")
