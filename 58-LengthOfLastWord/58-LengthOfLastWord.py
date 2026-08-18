# Last updated: 18/08/2026, 14:58:01
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s) - 1
        lastChar = s[index]

        while lastChar == " ":
            index -= 1
            lastChar = s[index]
        
        count = 0
        while s[index] != " " and index >= 0:
            count += 1
            index-= 1
        
        return count
