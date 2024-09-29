from typing import List, Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"val: {self.val}\nnext: {self.next}"


def list2node(nums: List[int]) -> ListNode:
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
