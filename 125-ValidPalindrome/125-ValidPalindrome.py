# Last updated: 18/08/2026, 14:57:31
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and (not s[l].isalnum() or not s[r].isalnum()):
                if s[l].isalnum() is False:
                    l += 1
                
                if s[r].isalnum() is False:
                    r -= 1

            if l >= r:
                return True

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        
        return True