def probrem():
    print(some_sums(input(), input(), input()))


def some_sums(N: str, A: str, B: str):
    total = int(N)
    min = int(A)
    max = int(B)
    ans = []
    for i in range(1, total + 1):
        buf = adder(i)
        if buf >= min and buf <= max:
            ans.append(i)
    return sum(ans)


def adder(n: int) -> int:
    buf = 0
    for i in str(n):
        buf += int(i)
    return buf


assert some_sums("20", "2", "5") == 84
assert some_sums("10", "1", "2") == 13
assert some_sums("100", "4", "16") == 4554
