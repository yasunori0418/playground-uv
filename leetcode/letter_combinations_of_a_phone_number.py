from typing import List


class Solution:
    """17. Letter Combinations of a Phone Number
    Given a string containing digits from 2-9 inclusive,
    return all possible letter combinations that the number could represent. Return the answer in any order.
    A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

    2 ～ 9 の数字を含む文字列を指定すると、
    数値が表すことができるすべての文字の組み合わせを返します。任意の順序で答えを返します。
    (電話のボタンと同様に) 数字と文字のマッピングを以下に示します。
    1 はどの文字にもマップされないことに注意してください。
    """

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0 or digits == "":
            return []
        ans = []
        nums = list(digits)
        digit_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        # 1
        if len(nums) == 1:
            for i in digit_map[nums[0]]:
                ans.append(i)
        # 2
        if len(nums) == 2:
            for i in digit_map[nums[0]]:
                for j in digit_map[nums[1]]:
                    ans.append(i + j)
        # 3
        if len(nums) == 3:
            for i in digit_map[nums[0]]:
                for j in digit_map[nums[1]]:
                    for k in digit_map[nums[2]]:
                        ans.append(i + j + k)
        # 4
        if len(nums) == 4:
            for i in digit_map[nums[0]]:
                for j in digit_map[nums[1]]:
                    for k in digit_map[nums[2]]:
                        for m in digit_map[nums[3]]:
                            ans.append(i + j + k + m)
        return ans


class Solution2:
    def letterCombinations(
        self, digits: str, element: int = 0, ans: List[str] = []
    ) -> List[str]:
        if len(digits) <= element:
            return ans
        digit_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        new_ans = []
        if len(ans) == 0:
            for j in digit_map[digits[element]]:
                new_ans.append(j)
        else:
            for i in ans:
                for j in digit_map[digits[element]]:
                    new_ans.append(i + j)
        return self.letterCombinations(digits, element + 1, new_ans)


assert Solution2().letterCombinations("2") == ["a", "b", "c"]
assert Solution2().letterCombinations("23") == [
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
assert Solution2().letterCombinations("234") == [
    "adg",
    "adh",
    "adi",
    "aeg",
    "aeh",
    "aei",
    "afg",
    "afh",
    "afi",
    "bdg",
    "bdh",
    "bdi",
    "beg",
    "beh",
    "bei",
    "bfg",
    "bfh",
    "bfi",
    "cdg",
    "cdh",
    "cdi",
    "ceg",
    "ceh",
    "cei",
    "cfg",
    "cfh",
    "cfi",
]
assert Solution2().letterCombinations("2345") == [
    "adgj",
    "adgk",
    "adgl",
    "adhj",
    "adhk",
    "adhl",
    "adij",
    "adik",
    "adil",
    "aegj",
    "aegk",
    "aegl",
    "aehj",
    "aehk",
    "aehl",
    "aeij",
    "aeik",
    "aeil",
    "afgj",
    "afgk",
    "afgl",
    "afhj",
    "afhk",
    "afhl",
    "afij",
    "afik",
    "afil",
    "bdgj",
    "bdgk",
    "bdgl",
    "bdhj",
    "bdhk",
    "bdhl",
    "bdij",
    "bdik",
    "bdil",
    "begj",
    "begk",
    "begl",
    "behj",
    "behk",
    "behl",
    "beij",
    "beik",
    "beil",
    "bfgj",
    "bfgk",
    "bfgl",
    "bfhj",
    "bfhk",
    "bfhl",
    "bfij",
    "bfik",
    "bfil",
    "cdgj",
    "cdgk",
    "cdgl",
    "cdhj",
    "cdhk",
    "cdhl",
    "cdij",
    "cdik",
    "cdil",
    "cegj",
    "cegk",
    "cegl",
    "cehj",
    "cehk",
    "cehl",
    "ceij",
    "ceik",
    "ceil",
    "cfgj",
    "cfgk",
    "cfgl",
    "cfhj",
    "cfhk",
    "cfhl",
    "cfij",
    "cfik",
    "cfil",
]

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
assert Solution().letterCombinations("") == []
assert Solution().letterCombinations("2") == ["a", "b", "c"]
assert Solution().letterCombinations("234") == [
    "adg",
    "adh",
    "adi",
    "aeg",
    "aeh",
    "aei",
    "afg",
    "afh",
    "afi",
    "bdg",
    "bdh",
    "bdi",
    "beg",
    "beh",
    "bei",
    "bfg",
    "bfh",
    "bfi",
    "cdg",
    "cdh",
    "cdi",
    "ceg",
    "ceh",
    "cei",
    "cfg",
    "cfh",
    "cfi",
]
assert Solution().letterCombinations("2345") == [
    "adgj",
    "adgk",
    "adgl",
    "adhj",
    "adhk",
    "adhl",
    "adij",
    "adik",
    "adil",
    "aegj",
    "aegk",
    "aegl",
    "aehj",
    "aehk",
    "aehl",
    "aeij",
    "aeik",
    "aeil",
    "afgj",
    "afgk",
    "afgl",
    "afhj",
    "afhk",
    "afhl",
    "afij",
    "afik",
    "afil",
    "bdgj",
    "bdgk",
    "bdgl",
    "bdhj",
    "bdhk",
    "bdhl",
    "bdij",
    "bdik",
    "bdil",
    "begj",
    "begk",
    "begl",
    "behj",
    "behk",
    "behl",
    "beij",
    "beik",
    "beil",
    "bfgj",
    "bfgk",
    "bfgl",
    "bfhj",
    "bfhk",
    "bfhl",
    "bfij",
    "bfik",
    "bfil",
    "cdgj",
    "cdgk",
    "cdgl",
    "cdhj",
    "cdhk",
    "cdhl",
    "cdij",
    "cdik",
    "cdil",
    "cegj",
    "cegk",
    "cegl",
    "cehj",
    "cehk",
    "cehl",
    "ceij",
    "ceik",
    "ceil",
    "cfgj",
    "cfgk",
    "cfgl",
    "cfhj",
    "cfhk",
    "cfhl",
    "cfij",
    "cfik",
    "cfil",
]
