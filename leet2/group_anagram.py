from typing import List
from collections import defaultdict
from deepdiff import DeepDiff


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return solve(strs)


def solve(strs: List[str]) -> List[List[str]]:
    ## 最初のhash_map
    # hash_map = {}

    ## 気がついたらdefaultdictを触りだした
    hash_map = defaultdict(set)
    for s in strs:
        hash_key = "".join(sorted(s))

        ## 最初の方法
        # if hash_key not in hash_map:
        #     hash_map[hash_key] = []
        # hash_map[hash_key].append(s)

        ## setdefaultを使った方法
        # hash_map.setdefault(hash_key, []).append(s)

        ## 気がついたらdefaultdictを触りだした
        hash_map[hash_key].add(s)

    return [list(v) for v in hash_map.values()]


def deep_sort(solve_list: list[list[str]]) -> list[list[str]]:
    return sorted(sorted(i) for i in solve_list)


def test_solve():
    assert not DeepDiff(
        solve(["eat", "tea", "tan", "ate", "nat", "bat"]),
        [
            ["bat"],
            ["nat", "tan"],
            ["ate", "eat", "tea"],
        ],
        ignore_order=True,
    )

    assert deep_sort(solve(["eat", "tea", "tan", "ate", "nat", "bat"])) == deep_sort(
        [
            ["bat"],
            ["nat", "tan"],
            ["ate", "eat", "tea"],
        ]
    )

