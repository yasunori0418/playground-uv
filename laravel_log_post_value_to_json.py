"""
laravelのproduction.ERRORで掃き出される`@@postValues:`が人が読むにはしんどい文法のデータなので、これをjsonに変換する
`a:1:{i:0;s:4:"item"}` -> 配列
`a:1:{s:3:"key";s:5:"value";}` -> 連想配列
`s:4:"hoge"` -> 文字列
`i:0` -> 整数

`prefix:{データの長さ}:データ`というデータの連続
整数の場合は`i:{データ}`というデータ構造
prefix:
  a: 配列
  s: 文字列
  i: 整数
"""

from typing import Any, Literal, Optional, Union
import re
import pytest


class PostValue:
    PREFIX_TYPES = Literal["Array", "String", "Integer"]

    def __init__(self, value: str) -> None:
        self.value = value

    def _extract_parent_data(self, data: str) -> str:
        """dataから括弧の中の文字列を抽出する

        再帰的な括弧の文字列抽出ではなく、浅いデータ抽出
        :param: data str
        """
        open_parent_index = data.find("{") + 1
        close_parent_index = data.rfind("}")
        return data[open_parent_index:close_parent_index]

    def _prefix_checker(self, data: str) -> Optional[PREFIX_TYPES]:
        """dataの先頭文字列を識別"""
        if data[0] == "a":
            return "Array"
        elif data[0] == "s":
            return "String"
        elif data[0] == "i":
            return "Integer"
        else:
            return None

    def _extract_data(self, data: str) -> Union[str, int, None]:
        def __match_data(data: str, pattern: re.Pattern):
            match = pattern.match(data)
            if match:
                return match.group(1)

        prefix = self._prefix_checker(data)
        if prefix == "String":
            return __match_data(data, re.compile(r'^s:\d:"(.*?)";'))
        elif prefix == "Integer":
            return int(__match_data(data, re.compile(r"i:(\d*);")))
        return None

    def parse2dict(self) -> dict:
        return dict()


@pytest.mark.parametrize(
    [
        "value",
        "expected",
    ],
    [
        pytest.param('i:0;s:5:"item1";i:1;"item2";i:2;"item3"', 0),
        pytest.param('s:3:"key";s:5:"value";', "key"),
        pytest.param('n:3:"key";s:5:"value";', None),
    ],
)
def test_extract_data(value: str, expected: Any):
    assert PostValue("test")._extract_data(value) == expected


@pytest.mark.parametrize(
    [
        "value",
        "expected",
    ],
    [
        pytest.param(
            'a:3:{i:0;s:5:"item1";i:1;"item2";i:2;"item3"}',
            "Array",
        ),
        pytest.param('i:0;s:5:"item1";i:1;"item2";i:2;"item3"', "Integer"),
        pytest.param('s:3:"key";s:5:"value";', "String"),
        pytest.param('n:3:"key";s:5:"value";', None),
    ],
)
def test_prefix_checker(value: str, expected: str):
    assert PostValue("test")._prefix_checker(value) == expected


@pytest.mark.parametrize(
    [
        "value",
        "expected",
    ],
    [
        pytest.param(
            'a:2:{s:3:"key";s:5:"value";s:13:"arrayInString";a:3:{i:0;s:5:"item1";i:1;"item2";i:2;"item3"}}',
            's:3:"key";s:5:"value";s:13:"arrayInString";a:3:{i:0;s:5:"item1";i:1;"item2";i:2;"item3"}',
        ),
        pytest.param(
            'a:3:{i:0;s:5:"item1";i:1;"item2";i:2;"item3"}',
            'i:0;s:5:"item1";i:1;"item2";i:2;"item3"',
        ),
    ],
)
def test_extract_parent_data(value: str, expected: str):
    assert PostValue("test")._extract_parent_data(value) == expected


@pytest.mark.skip(reason="未実装")
@pytest.mark.parametrize(
    [
        "value",
        "expected",
    ],
    [
        pytest.param(
            'a:2:{s:3:"key";s:5:"value";s:13:"arrayInString";a:3:{i:0;s:5:"item1";i:1;"item2";i:2;"item3"}}',
            {
                "key": "value",
                "arrayInString": [
                    "item1",
                    "item2",
                    "item3",
                ],
            },
        )
    ],
)
def test_parse2dict(value: str, expected: dict):
    assert PostValue(value).parse2dict() == expected
