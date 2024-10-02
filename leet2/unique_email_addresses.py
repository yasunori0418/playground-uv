from typing import List
import pytest


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        return solve(emails)


def solve(emails: List[str]) -> int:
    """ChatGPTが提示してきた答え"""
    unique_emails = set()
    for email in emails:
        local, domain = email.split("@")
        local = local.split("+")[0].replace(".", "")
        unique_emails.add(f"{local}@{domain}")
    return len(unique_emails)


def solve2(emails: List[str]) -> int:
    """あえてハッシュマップを使う方法"""
    hash_map = {}
    for email in emails:
        local, domain = email.split("@")
        local = local.split("+")[0].replace(".", "")
        hash_map.setdefault(f"{local}@{domain}", email)
    return len(hash_map.keys())


def solve3(emails: List[str]):
    """GenFさんがワンラインで答えてくれた奴"""
    len(
        set(
            ((x := e.split("@"))[0].split("+")[0].replace(".", "", -1), x[1])
            for e in emails
        )
    )
    len(
        set(
            (e.split("@")[0].split("+")[0].replace(".", ""), e.split("@")[1])
            for e in emails
        )
    )


@pytest.mark.parametrize(
    ["input", "expected"],
    [
        pytest.param(
            [
                "test.email+alex@leetcode.com",
                "test.e.mail+bob.cathy@leetcode.com",
                "testemail+david@lee.tcode.com",
            ],
            2,
        ),
        pytest.param(
            ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"],
            3,
        ),
    ],
)
def test_solve(input, expected):
    assert solve2(input) == expected
