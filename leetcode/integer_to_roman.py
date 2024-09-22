class Solution:
    """12. Integer to Roman
    |Symbol|Value|
    |------|-----|
    |I     |1    |
    |V     |5    |
    |X     |10   |
    |L     |50   |
    |C     |100  |
    |D     |500  |
    |M     |1000 |
    Roman numerals are formed by appending the conversions of decimal place values from highest to lowest.
    Converting a decimal place value into a Roman numeral has the following rules:

    - If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input,
        append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
    - If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol,
        for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX.
        Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
    - Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10.
        You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
    Given an integer, convert it to a Roman numeral.

    ---

    ローマ数字は、小数点以下の値の変換を最高から最低まで付加することによって形成されます。
    小数点以下の桁の値をローマ数字に変換するには、次の規則があります。

    - 値が 4 または 9 で始まらない場合は、入力から減算できる最大値の記号を選択します。
        その記号を結果に追加し、その値を減算し、余りをローマ数字に変換します。
    - 値が 4 または 9 で始まる場合は、次の記号から 1 つの記号を減算することを表す減算形式を使用します。
        たとえば、4 は 5 (V) 未満の 1 (I): IV、9 は 10 (X) 未満の 1 (I): IX です。
        次の減法形式のみが使用されます: 4 (IV)、9 (IX)、40 (XL)、90 (XC)、400 (CD)、および 900 (CM)。
    - 10 の倍数を表すために、10 の累乗 (I、X、C、M) のみを最大 3 回連続して追加できます。
        5(V)、50(L)、500(D)を複数回付加することはできません。 記号を 4 回追加する必要がある場合は、減算形式を使用します。
    整数を与えられた場合、それをローマ数字に変換します。
    """

    def intToRoman(self, num: int) -> str:
        ans = ""
        num_str = str(num)
        num_len = len(num_str)
        for i in num_str:
            if num_len == 4:
                ans += "M" * int(i)

            if num_len == 3:
                if int(i) <= 3:
                    ans += "C" * int(i)
                if int(i) >= 4:
                    if int(i) == 4:
                        ans += "CD"
                    elif int(i) == 9:
                        ans += "CM"
                    else:
                        ans += f"D{'C' * (int(i) - 5)}"

            if num_len == 2:
                if int(i) <= 3:
                    ans += "X" * int(i)
                if int(i) >= 4:
                    if int(i) == 4:
                        ans += "XL"
                    elif int(i) == 9:
                        ans += "XC"
                    else:
                        ans += f"L{'X' * (int(i) - 5)}"

            if num_len == 1:
                if int(i) <= 3:
                    ans += "I" * int(i)
                if int(i) >= 4:
                    if int(i) == 4:
                        ans += "IV"
                    elif int(i) == 9:
                        ans += "IX"
                    else:
                        ans += f"V{'I' * (int(i) - 5)}"

            num_len -= 1
        return ans


assert Solution().intToRoman(3749) == "MMMDCCXLIX"
assert Solution().intToRoman(58) == "LVIII"
assert Solution().intToRoman(1994) == "MCMXCIV"
