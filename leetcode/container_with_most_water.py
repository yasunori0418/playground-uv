from typing import List


class Solution:
    """11. Container With Most Water
    You are given an integer array height of length n.
    There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.

    ---

    長さ n の整数配列の高さが与えられます。
    i 番目の線の 2 つの端点が (i, 0) と (i, height[i]) になるように n 本の垂直線が描かれています。
    コンテナに最も多くの水が含まれるように、X 軸とともにコンテナを形成する 2 本の線を見つけます。
    コンテナに保存できる水の最大量を返します。
    容器を傾けないでください。

    """

    def maxArea(self, height: List[int]) -> int:
        pass


assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert Solution().maxArea([1, 5, 4, 3]) == 6
assert Solution().maxArea([3, 1, 2, 4, 5]) == 12
assert Solution().maxArea([1, 1]) == 1
