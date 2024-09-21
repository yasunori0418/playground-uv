class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 1:
            return s


assert Solution().convert("A", 1) == "A"


def gen_patterns(string: str, numRows):
    pass


assert gen_patterns("PAYPALISHIRING", 3) == [
    ["P", " ", "A", " ", "H", " ", "N"],
    ["A", "P", "L", "S", "I", "I", "G"],
    ["Y", " ", "I", " ", "R", " ", " "],
]


assert gen_patterns("PAYPALISHIRING", 4) == [
    ["P", " ", " ", "I", " ", " ", "N"],
    ["A", " ", "L", "S", " ", "I", "G"],
    ["Y", "A", " ", "H", "R", " ", " "],
    ["P", " ", " ", "I", " ", " ", " "],
]


assert gen_patterns("PAYPALISHIRING", 5) == [
    ["P", " ", " ", " ", "H", " "],
    ["A", " ", " ", "S", "I", " "],
    ["Y", " ", "I", " ", "R", " "],
    ["P", "L", " ", " ", "I", "G"],
    ["A", " ", " ", " ", "N", " "],
]


# assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
# assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
# assert Solution().convert("PAYPALISHIRING", 5) == "PHASIYIRPLIGAN"
