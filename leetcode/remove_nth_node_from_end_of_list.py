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


class Solution:
    """19. Remove Nth Node From End of List
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    連結リストの先頭を指定すると、リストの末尾から`n`番目のノードを削除し、その先頭を返します。
    """

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pass


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


def target_node(head: ListNode, n: int) -> ListNode:
    pointer = head
    listed_node = node2list(pointer)
    until_cnt = len(listed_node) - n
    if len(listed_node) == 1 or until_cnt == 1:
        return pointer
    for _ in range(until_cnt):
        pointer = pointer.next
    return pointer


assert target_node(gen_list_node([1, 2, 3, 4, 5]), 2).val == 4
assert target_node(gen_list_node([1]), 1).val == 1
assert target_node(gen_list_node([1, 2]), 1).val == 1


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
    assert node2list(Solution().removeNthFromEnd(head, n)) == expected
