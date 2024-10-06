"""62. Unique Paths
There is a robot on an m x n grid.
The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

m x n のグリッド上にロボットがあります。
ロボットは最初は左上隅 (つまり、grid[0][0]) に配置されます。
ロボットは右下隅 (つまり、grid[m - 1][n - 1]) に移動しようとします。
ロボットは、いかなる時点でも下または右のいずれかにしか移動できません。
2 つの整数 m と n を指定すると、ロボットが右下隅に到達するために通る可能性のある一意のパスの数を返します。
テストケースは、答えが`2 * (10**9)`以下になるように生成されます。
"""


def solve(m, n):
    # DPテーブルの初期化
    dp = [[1] * n for _ in range(m)]

    # DPテーブルの更新
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


def solve2(m, n):
    from math import comb

    return comb(m + n - 2, m - 1)


assert solve(3, 7) == 28
