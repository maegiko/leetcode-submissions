# Last updated: 08/04/2026, 12:40:02
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = 0
        original = x
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        return rev == original
