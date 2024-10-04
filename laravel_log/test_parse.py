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
        pytest.param('s:11:"key_in_dict";s:13:"value_in_dict";', "key_in_dict"),
        pytest.param('x:3:"key";s:5:"value";', None),
        pytest.param('N;s:5:"value";', None),
        pytest.param('b:0;s:5:"item1";i:1;"item2";i:2;"item3"', False),
        pytest.param('b:1;s:5:"item1";i:1;"item2";i:2;"item3"', True),
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
        pytest.param('b:0:"key";s:5:"value";', "Boolean"),
        pytest.param('b:1:"key";s:5:"value";', "Boolean"),
        pytest.param('x:3:"key";s:5:"value";', None),
        pytest.param('N;s:5:"value";', "Null"),
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


@pytest.mark.parametrize(
    ["input", "expected"],
    [
        pytest.param(
            'i:0;s:5:"item1";i:1;s:5:"item2";i:2;s:5:"item3";',
            ["item1", "item2", "item3"],
        ),
        pytest.param(
            'i:0;s:5:"item1";i:1;b:1;i:2;s:5:"item3";',
            ["item1", True, "item3"],
        ),
        pytest.param(
            'i:0;s:5:"item1";i:1;b:0;i:2;s:5:"item3";',
            ["item1", False, "item3"],
        ),
        pytest.param(
            'i:0;s:5:"item1";i:1;N;i:2;s:5:"item3";',
            ["item1", None, "item3"],
        ),
        pytest.param(
            'i:0;s:5:"item1";i:1;a:1:{s:3:"key";s:5:"value";}i:2;s:5:"item3";',
            ["item1", {"key": "value"}, "item3"],
        ),
        pytest.param(
            'i:0;s:5:"item1";i:1;a:3:{i:0;s:5:"item1";i:1;s:5:"item2";i:2;s:5:"item3";}i:2;s:5:"item3";',
            ["item1", ["item1", "item2", "item3"], "item3"],
        ),
        pytest.param("", []),
    ],
)
def test_str_to_list(input, expected):
    assert PostValue()._str_to_list(input) == expected


@pytest.mark.parametrize(
    ["input", "expected"],
    [
        pytest.param('s:3:"key";s:5:"value";', {"key": "value"}),
        pytest.param('s:3:"key";b:1;', {"key": True}),
        pytest.param('s:3:"key";b:0;', {"key": False}),
        pytest.param('s:3:"key";N;', {"key": None}),
        pytest.param("", {}),
        pytest.param(
            's:3:"key";s:5:"value";s:4:"key2";s:6:"value2";',
            {"key": "value", "key2": "value2"},
        ),
        pytest.param(
            's:3:"key";s:5:"value";s:4:"key2";i:5;',
            {
                "key": "value",
                "key2": 5,
            },
        ),
        pytest.param(
            's:3:"key";s:5:"value";s:9:"dict_data";a:1:{s:11:"key_in_dict";s:13:"value_in_dict";}',
            {"key": "value", "dict_data": {"key_in_dict": "value_in_dict"}},
        ),
        pytest.param(
            's:9:"dict_data";a:3:{i:0;s:5:"item1";i:1;s:5:"item2";i:2;s:5:"item3";}s:3:"key";s:5:"value";',
            {"dict_data": ["item1", "item2", "item3"], "key": "value"},
        ),
    ],
)
def test_str_to_dict(input, expected):
    assert PostValue()._str_to_dict(input) == expected
