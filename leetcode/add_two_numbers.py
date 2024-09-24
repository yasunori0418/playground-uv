from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
