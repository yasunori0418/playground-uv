class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_str = []
        max_len = len(s)
        result: int = 0
        for i in s:
            result += 1
            if i in current_str:
                break
            current_str.append(i)
        return result
