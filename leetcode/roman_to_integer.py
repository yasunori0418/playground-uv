class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        for i in range(len(s)):
            if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                ans -= roman_to_int[s[i]]
            else:
                ans += roman_to_int[s[i]]
        return ans


assert Solution().romanToInt("MCMXCIV") == 1994
assert Solution().romanToInt("III") == 3
assert Solution().romanToInt("LVIII") == 58
assert Solution().romanToInt("MMMDCCXLIX") == 3749
