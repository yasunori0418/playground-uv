from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return solve(nums1, nums2)


def solve(nums1: List[int], nums2: List[int]) -> List[int]:
    set1 = set(nums1)
    set2 = set(nums2)
    res = set1 & set2
    return list(res)


def solve2(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))


def solve3(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    arr1_index = 0
    arr2_index = 0
    intersection = [0]
    while arr1_index < len(arr1) and arr2_index < len(arr2):
        if arr1[arr1_index] == arr2[arr2_index]:
            if intersection[-1] != arr1[arr1_index]:
                intersection.append(arr1[arr1_index])
            arr1_index += 1
            arr2_index += 1
        elif arr1[arr1_index] < arr2[arr2_index]:
            arr1_index += 1
        else:
            arr2_index += 1
    return intersection[1:]


def test_solve():
    assert solve3([1, 2, 2, 1], [2, 2]) == [2]
    assert sorted(solve3([4, 9, 5], [9, 4, 9, 8, 4])) == sorted([9, 4])
