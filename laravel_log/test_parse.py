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

from .parse import PostValue
from typing import Any
import pytest


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
    assert PostValue()._extract_data(value) == expected


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
    assert PostValue()._prefix_checker(value) == expected


@pytest.mark.parametrize(
    [
        "value",
        "expected",
    ],
    [
        pytest.param(
            'a:2:{s:3:"key";s:5:"value";s:13:"arrayInString";a:3:{i:0;s:5:"item1";i:1;"item2";i:2;"item3"}}',
            {
                "index": (5, 93),
                "data": 's:3:"key";s:5:"value";s:13:"arrayInString";a:3:{i:0;s:5:"item1";i:1;"item2";i:2;"item3"}',
            },
        ),
        pytest.param(
            'a:3:{i:0;s:5:"item1";i:1;"item2";i:2;"item3"}',
            {"index": (5, 44), "data": 'i:0;s:5:"item1";i:1;"item2";i:2;"item3"'},
        ),
    ],
)
def test_extract_parent_data(value: str, expected: str):
    assert PostValue()._extract_parent_data(value) == expected


def test_str_to_list():
    assert PostValue()._str_to_list(
        'i:0;s:5:"item1";i:1;s:5:"item2";i:2;s:5:"item3";'
    ) == ["item1", "item2", "item3"]
    assert PostValue()._str_to_list("") == []


def test_str_to_dict():
    assert PostValue()._str_to_dict('s:3:"key";s:5:"value";') == {"key": "value"}
    assert PostValue()._str_to_dict(
        's:3:"key";s:5:"value";s:4:"key2";s:6:"value2";'
    ) == {"key": "value", "key2": "value2"}
    assert PostValue()._str_to_dict('s:3:"key";s:5:"value";s:4:"key2";i:5;') == {
        "key": "value",
        "key2": 5,
    }
    assert PostValue()._str_to_dict("") == {}
