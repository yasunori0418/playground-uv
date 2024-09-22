import re


class Solution:
    """10. Regular Expression Matching
    Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).

    ---

    入力文字列 s とパターン p を指定して、「.」をサポートする正規表現マッチングを実装します。 および「*」の場合:

    '.' 任意の1文字と一致します。
    '*' 0個以上の先行要素と一致します。
    一致は入力文字列全体 (部分的ではなく) をカバーする必要があります。
    """

    def isMatch(self, s: str, p: str) -> bool:
        return bool(re.match(f"^{p}$", s))


assert not Solution().isMatch("aa", "a")
assert Solution().isMatch("aa", "a*")
assert Solution().isMatch("ab", ".*")
