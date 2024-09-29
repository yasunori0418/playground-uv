from .add_two_numbers import Solution
from .utils.linked_list import node2list, list2node


def test_add_two_numbers():
    assert node2list(
        Solution().addTwoNumbers(list2node([2, 4, 3]), list2node([5, 6, 4]))
    ) == [7, 0, 8]
    assert node2list(
        Solution().addTwoNumbers(list2node([0]), list2node([0]))
    ) == [0]
