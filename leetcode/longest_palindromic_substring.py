from deepdiff import DeepDiff


class Solution:
    """
    Given a string s, return the longest palindromic substring in s.
    文字列 s が与えられると、 s 内の最長の回文部分文字列を返します。
    """

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
assert not DeepDiff(
    list(allPatterns("cbbd")),
    [
        "c",
        "b",
        "b",
        "d",
        "cb",
        "bb",
        "bd",
        "cbb",
        "bbd",
        "cbbd",
    ],
    ignore_order=True,
)
