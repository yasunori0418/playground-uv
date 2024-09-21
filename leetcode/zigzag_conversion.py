class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 1:
            return s


assert Solution().convert("A", 1) == "A"


def gen_patterns(string: str, numRows):
    pass


assert gen_patterns("PAYPALISHIRING", 3) == [
    ["P", "A", "Y"],
    [" ", "P", " "],
    ["A", "L", "I"],
    [" ", "S", " "],
    ["H", "I", "R"],
    [" ", "I", " "],
    ["N", "G", " "],
]


assert gen_patterns("PAYPALISHIRING", 4) == [
    ["P", "A", "Y", "P"],
    [" ", " ", "A", " "],
    [" ", "L", " ", " "],
    ["I", "S", "H", "I"],
    [" ", " ", "R", " "],
    [" ", "I", " ", " "],
    ["N", "G", " ", " "],
]


assert gen_patterns("PAYPALISHIRING", 5) == [
    ["P", "A", "Y", "P", "A"],
    [" ", " ", " ", "L", " "],
    [" ", " ", "I", " ", " "],
    [" ", "S", " ", " ", " "],
    ["H", "I", "R", "I", "N"],
    [" ", " ", " ", "G", " "],
]


# assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
# assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
# assert Solution().convert("PAYPALISHIRING", 5) == "PHASIYIRPLIGAN"
