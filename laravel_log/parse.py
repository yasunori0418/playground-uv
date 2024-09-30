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

from typing import Dict, Literal, Optional, Tuple, Union
import re


class PostValue:
    PREFIX_TYPES = Literal["Array", "String", "Integer"]

    def _extract_parent_data(self, data: str) -> Dict[str, Union[Tuple[int, int], str]]:
        """dataから括弧の中の文字列を抽出する

        再帰的な括弧の文字列抽出ではなく、浅いデータ抽出
        :param: data str
        """
        parent_cnt = 0
        open_parent_index = 0
        close_parent_index = 0
        for i, s in enumerate(data):
            if s not in ["{", "}"]:
                continue
            if parent_cnt == 0 and s == "{":
                open_parent_index = i + 1
                parent_cnt += 1
                continue
            if parent_cnt == 1 and s == "}":
                close_parent_index = i
                parent_cnt -= 1
                break

            if s == "{":
                parent_cnt += 1
            if s == "}":
                parent_cnt -= 1
        return {
            "index": (open_parent_index, close_parent_index),
            "data": data[open_parent_index:close_parent_index],
        }

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
            return __match_data(data, re.compile(r'^s:\d:"(.*?)"'))
        elif prefix == "Integer":
            return int(__match_data(data, re.compile(r"i:(\d*)")))
        return None

    def _str_to_dict(self, data: str) -> Optional[dict]:
        result = {}
        while data:
            _key = self._extract_data(data)
            data = data[data.find(";") + 1 :]
            result[_key] = self._extract_data(data)
            data = data[data.find(";") + 1 :]
        return result

    def _str_to_list(self, data: str) -> Optional[list]:
        result = []
        while data:
            _index = int(self._extract_data(data))
            data = data[data.find(";") + 1 :]
            result.insert(_index, self._extract_data(data))
            data = data[data.find(";") + 1 :]
        return result
