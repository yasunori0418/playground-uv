import pytest
from .two_sum import Solution


@pytest.mark.parametrize(
    [
        "input",
        "expected",
    ],
    [
        pytest.param({"nums": [2, 7, 11, 15], "target": 9}, [0, 1]),
        pytest.param({"nums": [3, 2, 4], "target": 6}, [1, 2]),
        pytest.param({"nums": [3, 3], "target": 6}, [0, 1]),
    ],
)
def test_two_sum(input, expected):
    assert Solution().twoSum(**input) == expected
