from typing import List, Optional
import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
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


class Solution:
    def addTwoNumbersFirst(
        self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0
    ) -> Optional[ListNode]:
        """一番最初に答え見ながら書いた奴

        初期化したリンクリストを使って、pointerに計算結果をリンクさせていく
        carry(桁上がり)は、初回は0、次回以降は前回のループ処理のcarryを計算に含める
        計算が終ったl1, l2は次のnodeにアクセスする
        """
        dummy_head = ListNode(0)
        pointer = dummy_head
        while (
            l1 or l2 or carry
        ):  # l1とl2とcarryが存在したら、存在しなかったら(計算対象が無い)ループ終了
            temp_num = l1.val if l1 else 0
            temp_num += l2.val if l2 else 0
            summation = temp_num + carry
            num = summation % 10
            carry = summation // 10
            new_node = ListNode(num)
            pointer.next = new_node
            pointer = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy_head.next

    def addTwoNumbersRec(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
        carry: int = 0,
        result_node=ListNode(0),
    ):
        """ryoppippiさんに教わりながら再帰関数で書いた別回答"""
        # if not (l1 or l2 or carry): ## ↓ドモルガンの法則で書き変えたやつ
        if not l1 and not l2 and not carry:
            return None
        temp_num = l1.val if l1 else 0
        temp_num += l2.val if l2 else 0
        summation = temp_num + carry
        num = summation % 10
        new_carry = summation // 10
        new_node = ListNode(num)
        result_node.next = new_node
        result_node = new_node
        self.addTwoNumbersRec(
            l1.next if l1 else None, l2.next if l2 else None, new_carry, result_node
        )
        return result_node

class Solution2:
    def addTwoNumbers(
        self, 
        l1: Optional[ListNode],
        l2: Optional[ListNode],
        carry=0
    ) -> Optional[ListNode]:
        if not l1 and not l2 and carry == 0:
            return None

        first_num = l1.val if l1 else 0
        second_num = l2.val if l2 else 0
        summation = first_num + second_num + carry

        new_num = summation % 10
        new_carry = summation // 10

        new_node = ListNode(new_num)
        new_node.next = self.addTwoNumbers(
            l1.next if l1 else None,
            l2.next if l2 else None,
            new_carry
        )

        return new_node
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


@pytest.mark.parametrize(
    ["input1", "input2", "expected_data"],
    [
        pytest.param(
            gen_list_node([2, 4, 3]), gen_list_node([5, 6, 4]), gen_list_node([7, 0, 8])
        ),
        pytest.param(gen_list_node([0]), gen_list_node([0]), gen_list_node([0])),
        pytest.param(
            gen_list_node([9, 9, 9, 9, 9, 9, 9]),
            gen_list_node([9, 9, 9, 9]),
            gen_list_node([8, 9, 9, 9, 0, 0, 0, 1]),
        ),
    ],
)
def test_add_two_numbers_first(
    input1: ListNode, input2: ListNode, expected_data: ListNode
):
    res = Solution().addTwoNumbersFirst(input1, input2)
    while res or expected_data:
        if not res or not expected_data:
            assert False
        assert res.val == expected_data.val
        res = res.next
        expected_data = expected_data.next
