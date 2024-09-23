def probrem():
    print(coins(input(), input(), input(), input()))


def coins(input1: str, input2: str, input3: str, input4: str) -> int:
    A = int(input1)
    B = int(input2)
    C = int(input3)
    total = int(input4)
    ans = 0
    for i in range(A + 1):
        for j in range(B + 1):
            for k in range(C + 1):
                buf = i * 500 + j * 100 + k * 50
                if buf == total:
                    ans += 1
    return ans


assert coins("2", "2", "2", "100") == 2
assert coins("5", "1", "0", "150") == 0
assert coins("30", "40", "50", "6000") == 213
