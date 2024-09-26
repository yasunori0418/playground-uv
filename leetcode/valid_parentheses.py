import pytest


class Solution:
    """20. Valid Parentheses
    Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

    An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

    文字 `'('`、`')'`、`'{'`、`'}'`、`'['`、および `']'` だけを含む文字列`s`がある場合、入力文字列が 有効。
    入力文字列は次の場合に有効です。
    1. 開いた括弧は同じ種類の括弧で閉じなければなりません。
    2. 開き括弧は正しい順序で閉じなければなりません。
    3. すべての閉じ括弧には、同じタイプの対応する開き括弧があります。
    """

    def isValid(self, s: str) -> bool:
        pass


@pytest.mark.parametrize(
    [
        "s",
        "expected",
    ],
    [
        pytest.param("()", True),
        pytest.param("()[]{}", True),
        pytest.param("(]", False),
        pytest.param("([])", True),
    ],
)
def test_valid_parentheses(s: str, expected: bool):
    assert Solution().isValid(s) == expected
