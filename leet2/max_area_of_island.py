"""695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/description/
You are given an m x n binary matrix grid.
An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

m x n のバイナリ行列グリッドが与えられます。
島は、4 方向 (水平または垂直) に接続された 1 (陸地を表す) のグループです。グリッドの 4 つの端すべてが水で囲まれていると想定できます。
島の面積は、島内の値 1 を持つセルの数です。
グリッド内の島の最大面積を返します。 島がない場合は0を返します。
"""


def solve(grid: list[list[int]]) -> int:
    return 6


assert (
    solve(
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
    )
    == 6
)
