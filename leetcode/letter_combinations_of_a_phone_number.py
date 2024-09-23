from typing import List


class Solution:
    """17. Letter Combinations of a Phone Number
    Given a string containing digits from 2-9 inclusive,
    return all possible letter combinations that the number could represent. Return the answer in any order.
    A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

    2 ～ 9 の数字を含む文字列を指定すると、
    数値が表すことができるすべての文字の組み合わせを返します。任意の順序で答えを返します。
    (電話のボタンと同様に) 数字と文字のマッピングを以下に示します。  1 はどの文字にもマップされないことに注意してください。
    """

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0 or digits == "":
            return []
        ans = []
        digits_map = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }


assert Solution().letterCombinations("") == []
assert Solution().letterCombinations("2") == ["a", "b", "c"]
assert Solution().letterCombinations("23") == [
    "ad",
    "ae",
    "af",
    "bd",
    "be",
    "bf",
    "cd",
    "ce",
    "cf",
]
