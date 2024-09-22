class Solution:
    """Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

    The algorithm for myAtoi(string s) is as follows:

    1. Whitespace: Ignore any leading whitespace (" ").
    2. Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
    3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached.
        If no digits were read, then the result is 0.
    4. Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
        then round the integer to remain in the range.
        Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.

    Return the integer as the final result.

    ---

    文字列を 32 ビット符号付き整数に変換する myAtoi(string s) 関数を実装します。
    myAtoi(string s) のアルゴリズムは次のとおりです。
    1. ホワイトスペース: 先頭のホワイトスペース (" ") は無視します。
    2. 符号あり: 次の文字が「-」または「+」であるかどうかを確認して、陽性が存在しないと仮定して符号を決定します。
    3. 変換: 数字以外の文字が出現するか文字列の終わりに達するまで、先頭のゼロをスキップして整数を読み取ります。
        数字が読み取られなかった場合、結果は 0 になります。
    4. 丸め: 整数が 32 ビット符号付き整数の範囲 [-231, 231 - 1] の外にある場合、
        次に、範囲内に収まるように整数を四捨五入します。
        具体的には、-231 未満の整数は -231 に四捨五入し、231 - 1 より大きい整数は 231 - 1 に四捨五入する必要があります。

    最終結果として整数を返します。
    """

    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        return int(s)


assert Solution().myAtoi("") == 0
assert Solution().myAtoi("42") == 42
assert Solution().myAtoi("-042") == -42
assert Solution().myAtoi("1337c0d3") == 1337
assert Solution().myAtoi("0-1") == 0
assert Solution().myAtoi("0-1") == 0
assert Solution().myAtoi("words and 987") == 0
