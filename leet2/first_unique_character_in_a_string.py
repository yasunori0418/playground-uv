class Solution:
    def firstUniqChar(self, s: str) -> int:
        return solve(s)


def solve(s) -> int:
    hash_map = {}
    for char in s:
        if char in hash_map:
            hash_map[char] += 1
        else:
            hash_map[char] = 1
    for i in range(len(s)):
        if hash_map[s[i]] == 1:
            return i
    return -1


def test_solve():
    assert solve("leetcode") == 0
    assert solve("loveleetcode") == 2
    assert solve("aabb") == -1
