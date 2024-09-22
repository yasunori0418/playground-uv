class Solution:
    """7. Reverse Integer
    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    符号付き 32 ビット整数 x を指定すると、桁を反転した x を返します。
    x を反転すると、値が符号付き 32 ビット整数の範囲 [-231, 231 - 1] を超える場合は、0 を返します。
    """

    def reverse(self, x: int) -> int:
        abs_num = abs(x)
        reversed_num = int(str(abs_num)[::-1])
        if reversed_num >= 2_147_483_647:
            return 0
        if x < 0:
            return -reversed_num
        return reversed_num


assert Solution().reverse(120) == 21
assert Solution().reverse(123) == 321
assert Solution().reverse(-123) == -321
assert Solution().reverse(1534236469) == 0
assert Solution().reverse(-1534236469) == 0
