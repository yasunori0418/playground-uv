"""200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

「1」(陸地) と「0」(水) の地図を表す m x n 2D バイナリ グリッドを指定すると、島の数を返します。
島は水に囲まれており、隣接する土地を水平または垂直に接続して形成されます。
グリッドの 4 つの端すべてが水で囲まれていると考えることができます。
"""


def solve(grid: list[list[str]]) -> int:
    result = 0
    rows = len(grid)
    cols = len(grid[0])

    def dfs(r, c):
        # 各グリッド内を探索していき、範囲から出たり、探索対象ではなくなったら終了する
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                # 2重ループ内に再帰関数だからめちゃくちゃ計算量が大きくなると思ったけど、
                # ChatGPTに聞いてみたらこれはO(r * c)分で済むらしい
                # dfs関数自体が探索対象を潰していくから、らしい
                dfs(r, c)
                result += 1
    return result


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

    assert (
        solve(
            [
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "1", "1"],
                ["1", "1", "0", "0", "1"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 2
    )

    assert (
        solve(
            [
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "1"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )
