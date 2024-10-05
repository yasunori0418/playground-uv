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
    max_size = 0
    rows = len(grid)
    cols = len(grid[0])

    def dfs(r, c, size=0) -> int:
        # 各グリッド内を探索していき、範囲から出たり、探索対象ではなくなったら終了する
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return size
        grid[r][c] = 0
        size += 1
        size = dfs(r + 1, c, size)
        size = dfs(r - 1, c, size)
        size = dfs(r, c + 1, size)
        size = dfs(r, c - 1, size)
        return size

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_size = max(max_size, dfs(r, c))
    return max_size


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

assert solve([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0

