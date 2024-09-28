from typing import Optional, List
import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: Optional[int] = 0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"val: {self.val}\nnext: {self.next}"


def gen_list_node(nums: List[int]) -> ListNode:
    node = ListNode(nums[0])
    current = node
    for n in nums[1:]:
        new_node = ListNode(n)
        current.next = new_node
        current = new_node
    return node


def node2list(head: Optional[ListNode]) -> List[int]:
    result = []
    pointer = head
    while pointer:
        result.append(pointer.val)
        pointer = pointer.next
    return result


class Solution:
    """21. Merge Two Sorted Lists
    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.

    ---

    2 つのソートされたリンク リスト list1 と list2 の先頭が与えられます。
    2 つのリストを 1 つの並べ替えられたリストにマージします。 このリストは、最初の 2 つのリストのノードを結合して作成する必要があります。
    マージされたリンク リストの先頭を返します。
    """

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """kuuさん再帰の達人じゃん！！！"""
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        else:
            return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))



@pytest.mark.parametrize(
    [
        "list1",
        "list2",
        "expected",
    ],
    [
        pytest.param(
            gen_list_node([1, 2, 4]), gen_list_node([1, 3, 4]), [1, 1, 2, 3, 4, 4]
        ),
        pytest.param(None, None, []),
        pytest.param(None, ListNode(), [0]),
    ],
)
def test_merge_two_lists(list1: ListNode, list2: ListNode, expected: List[int]):
    assert node2list(Solution().mergeTwoLists(list1, list2)) == expected
