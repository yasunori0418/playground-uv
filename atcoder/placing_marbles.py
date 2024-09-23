def placing_marbles(num: int) -> int:
    ans = 0
    for i in str(num):
        ans += int(i)
    return ans


assert placing_marbles(101) == 2
assert placing_marbles(000) == 0


# 提出用
ans = 0
for i in input():
    ans += int(i)
print(ans)
