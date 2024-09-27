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

import pytest


class PostValue:
    def __init__(self, value: str) -> None:
        self.value = value

    def _extract_parent_data(self, data: str) -> str:
        """dataから括弧の中の文字列を抽出する

        再帰的な括弧の文字列抽出ではなく、浅いデータ抽出
        :param: data str
        """
        pass

    def parse2dict(self) -> dict:
        return dict()


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
