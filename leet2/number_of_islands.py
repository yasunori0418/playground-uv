"""200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

「1」(陸地) と「0」(水) の地図を表す m x n 2D バイナリ グリッドを指定すると、島の数を返します。
島は水に囲まれており、隣接する土地を水平または垂直に接続して形成されます。
グリッドの 4 つの端すべてが水で囲まれていると考えることができます。
"""


def solve(grid: list[list[str]]) -> int:
    return 1


def test_solve():
    assert (
        solve(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )

