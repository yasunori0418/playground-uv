import pytest
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
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


assert node2list(gen_list_node([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
assert node2list(gen_list_node([1])) == [1]
assert node2list(gen_list_node([1, 2])) == [1, 2]


def target_node(head: Optional[ListNode], n: int):
    listed_node = node2list(head)
    until_cnt = len(listed_node) - n
    prev_point = None
    if len(listed_node) == 1 or until_cnt == 1:
        return prev_point, head
    for i in range(until_cnt):
        head = head.next
        if i == until_cnt - 2:
            prev_point = head
    return prev_point, head


@pytest.mark.parametrize(
    [
        "head",
        "n",
        "expected_prev_point",
        "expected_remove_point",
    ],
    [
        pytest.param(gen_list_node([1, 2, 3, 4, 5]), 2, 3, 4),
        pytest.param(gen_list_node([1]), 1, None, 1),
        pytest.param(gen_list_node([1, 2]), 1, None, 1),
    ],
)
def test_target_node(
    head: ListNode,
    n: int,
    expected_prev_point: Optional[int],
    expected_remove_point: int,
):
    prev_pointer, remove_pointer = target_node(head, n)
    assert remove_pointer.val == expected_remove_point
    if prev_pointer:
        assert prev_pointer.val == expected_prev_point
    else:
        assert prev_pointer == expected_prev_point


class Solution:
    """19. Remove Nth Node From End of List
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    連結リストの先頭を指定すると、リストの末尾から`n`番目のノードを削除し、その先頭を返します。
    """

    def myRemoveNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        pointer = head
        listed_node = node2list(pointer)
        if len(listed_node) == 1 and n == 1:
            return head.next
        prev_pointer, remove_pointer = target_node(pointer, n)
        if prev_pointer:
            if remove_pointer.next:
                prev_pointer.next = remove_pointer.next
            else:
                prev_pointer.next = None
        else:
            head.next = None
        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """また難しく考えすぎて、敗北した…"""
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head


@pytest.mark.parametrize(
    [
        "head",
        "n",
        "expected",
    ],
    [
        pytest.param(gen_list_node([1, 2, 3, 4, 5]), 2, [1, 2, 3, 5]),
        pytest.param(gen_list_node([1]), 1, []),
        pytest.param(gen_list_node([1, 2]), 1, [1]),
    ],
)
def test_remove_nth_from_end(head: ListNode, n: int, expected: List[int]):
    res = node2list(Solution().removeNthFromEnd(head, n))
    assert res == expected
