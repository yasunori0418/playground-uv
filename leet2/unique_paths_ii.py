"""63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/description/
You are given an m x n integer array grid.
There is a robot initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.

m x n の整数配列グリッドが与えられます。
ロボットは最初は左上隅 (つまり、grid[0][0]) に配置されています。
ロボットは右下隅 (つまり、grid[m - 1][n - 1]) に移動しようとします。
ロボットは、いかなる時点でも下または右のいずれかにしか移動できません。
障害物とスペースはグリッド内でそれぞれ 1 または 0 としてマークされます。 ロボットが通る経路には障害物となる四角形を含めることはできません。
ロボットが右下隅に到達するために通る可能性のある一意のパスの数を返します。
テストケースは、答えが 2 * 109 以下になるように生成されます。
"""


def solve(grid: list[list[int]]) -> int:
    # DPテーブルの初期化
    if not grid or not grid[0]:
        return 0

    m = len(grid)
    n = len(grid[0])

    # DPテーブルの初期化
    dp = [[0] * n for _ in range(m)]

    # スタート地点の初期化
    dp[0][0] = 1 if grid[0][0] == 0 else 0

    # 最初の行の初期化
    for j in range(1, n):
        if grid[0][j] == 0 and dp[0][j - 1] == 1:
            dp[0][j] = 1
        else:
            dp[0][j] = 0

    # 最初の列の初期化
    for i in range(1, m):
        if grid[i][0] == 0 and dp[i - 1][0] == 1:
            dp[i][0] = 1
        else:
            dp[i][0] = 0

    # DPテーブルの更新
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            else:
                dp[i][j] = 0

    return dp[m - 1][n - 1]


assert solve([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
assert solve([[0, 1], [0, 0]]) == 1
