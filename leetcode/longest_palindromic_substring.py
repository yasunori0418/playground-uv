from deepdiff import DeepDiff


class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass


def allPatterns(s):
    for i in range(len(s)):
        for j in range(i, len(s)):
            yield s[i : j + 1]


assert not DeepDiff(
    list(allPatterns("babad")),
    [
        "b",
        "a",
        "b",
        "a",
        "d",
        "ba",
        "ab",
        "ba",
        "ad",
        "bab",
        "aba",
        "bad",
        "baba",
        "abad",
        "babad",
    ],
    ignore_order=True,
)
