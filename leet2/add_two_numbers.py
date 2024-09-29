from .utils.linked_list import ListNode
from typing import Optional


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
        carry: int = 0,
        result_node: ListNode = ListNode(),
    ) -> Optional[ListNode]:
        if not l1 and not l2 and not carry:
            return None
        temp_sum = l1.val if l1 else 0
        temp_sum += l2.val if l2 else 0
        summation = temp_sum + carry
        num = summation % 10
        new_carry = summation // 10
        new_node = ListNode(num)
        result_node.next = new_node
        result_node = new_node
        self.addTwoNumbers(
            l1.next if l1 else None,
            l2.next if l2 else None,
            new_carry,
            new_node
        )
        return result_node

