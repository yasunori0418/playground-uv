from typing import List
import pytest


class Solution:
    """22. Generate Parentheses
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    n 組のかっこが指定された場合、適切な形式のかっこのすべての組み合わせを生成する関数を作成します。
    """

    def generateParenthesis(self, n: int) -> List[str]:
        pass


@pytest.mark.parametrize(
    [
        "n",
        "expected",
    ],
    [
        pytest.param(3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        pytest.param(2, ["(())", "()()"]),
        pytest.param(1, ["()"]),
    ],
)
def test_generate_parenthesis(n: int, expected: List[str]):
    assert Solution().generateParenthesis(n) == expected
