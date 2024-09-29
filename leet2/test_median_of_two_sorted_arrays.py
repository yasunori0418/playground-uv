from .median_of_two_sorted_arrays import Solution


def test_find_median_sorted_arrays():
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2.0
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5

