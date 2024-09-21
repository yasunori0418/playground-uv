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
    ["N", "G"],
]


assert gen_patterns("PAYPALISHIRING", 3) == {
    1: ["P", "A", "Y"],
    2: [" ", "P", " "],
    3: ["A", "L", "I"],
    4: [" ", "S", " "],
    5: ["H", "I", "R"],
    6: [" ", "I", " "],
    7: ["N", "G"],
}


assert gen_patterns("PAYPALISHIRING", 4) == {
    1: ["P", "A", "Y", "P"],
    2: [" ", " ", "A", " "],
    3: [" ", "L", " ", " "],
    4: ["I", "S", "H", "I"],
    5: [" ", " ", "R", " "],
    6: [" ", "I", " ", " "],
    7: ["N", "G"],
}


assert gen_patterns("PAYPALISHIRING", 5) == {
    1: ["P", "A", "Y", "P", "A"],
    2: [" ", " ", " ", "L", " "],
    3: [" ", " ", "I", " ", " "],
    4: [" ", "S", " ", " ", " "],
    5: ["H", "I", "R", "I", "N"],
    6: [" ", " ", " ", "G"],
}


# assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
# assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
# assert Solution().convert("PAYPALISHIRING", 5) == "PHASIYIRPLIGAN"
