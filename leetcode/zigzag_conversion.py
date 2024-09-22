class Solution:
    """
        refer: https://qiita.com/KueharX/items/777868c9914317a65cd2
    """
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        num = 0
        step = 0
        results = [""] * numRows
        for i in s:
            results[num] += i
            if num == 0:
                step = 1
            elif num == numRows - 1:
                step = -1
            num += step
        return "".join(results)


assert Solution().convert("A", 1) == "A"
assert Solution().convert("AB", 1) == "AB"
assert Solution().convert("ABC", 1) == "ABC"
assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert Solution().convert("PAYPALISHIRING", 5) == "PHASIYIRPLIGAN"
