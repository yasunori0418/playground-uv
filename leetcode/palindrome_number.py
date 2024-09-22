class Solution:
    """9. Palindrome Number
    Given an integer x, return true if x is a palindrome, and false otherwise.
    整数 x を指定すると、x が回文の場合は true を返し、それ以外の場合は false を返します。
    """
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if str(x) == str(x)[::-1]:
            return True
        return False

assert Solution().isPalindrome(121)
assert not Solution().isPalindrome(-121)
assert not Solution().isPalindrome(10)
