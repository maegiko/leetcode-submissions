# Last updated: 08/04/2026, 12:39:59
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0
        right = len(numbers) - 1

        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                array = [left + 1, right + 1]
                return array
            if current > target:
                right -= 1
            else:
                left += 1

        