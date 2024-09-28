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
        len_s = len(s)
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        if len_s % 2 == 1:
            return False
        if len_s == 2:
            return pairs[s[0]] == s[1]
        while s:
            close_index = s.find(pairs[s[0]])
            if close_index == -1:
                return False
            if close_index < len_s:
                s = s[0:close_index] + s[close_index+1:]
                s = s[1:]
        return True

Solution().isValid("([)]")

@pytest.mark.parametrize(
    [
        "s",
        "expected",
    ],
    [
        pytest.param("()", True),
        pytest.param("(]", False),
        pytest.param("()[]{}", True),
        pytest.param("([])", True),
        pytest.param("([)]", False),
    ],
)
def test_valid_parentheses(s: str, expected: bool):
    assert Solution().isValid(s) == expected
