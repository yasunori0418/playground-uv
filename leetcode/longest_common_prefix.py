class Solution:
    """14. Longest Common Prefix
        Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string `""`.

        文字列の配列の中から最も長い共通プレフィックス文字列を検索する関数を作成します。
        共通のプレフィックスがない場合は、空の文字列 `""` を返します。
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pass


assert Solution().longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert Solution().longestCommonPrefix(["dog","racecar","car"]) == ""
