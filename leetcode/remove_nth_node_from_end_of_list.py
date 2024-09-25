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


def node2list(head: Optional[ListNode], result: List[int] = []) -> List[int]:
    if not head:
        return result
    result.append(head.val)
    next_node = head.next
    return node2list(next_node, result)


assert node2list(gen_list_node([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize(
    [
        "head",
        "n",
        "expected",
    ],
    [
        pytest.param(gen_list_node([1, 2, 3, 4, 5]), 2, gen_list_node([1, 2, 3, 5])),
        pytest.param(gen_list_node([1]), 1, ListNode()),
        pytest.param(gen_list_node([1, 2]), 1, gen_list_node([1])),
    ],
)
def test_remove_nth_from_end(head: ListNode, n: int, expected: ListNode):
    res = Solution().removeNthFromEnd(head, n)
    while res or expected:
        if not res or not expected:
            assert False
        assert res.val == expected.val
        res = res.next
        expected = expected.next
