"""
Brute: Use nested lists to check every possible pair and return true if a pair has the same value
- O(n^2) time complexity

Optimized: Use set to store visited values. A value appears at least twice if the value being checked it already in the set.
- O(n) time complexity since each value is only visited once
"""

class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """

        my_set = set()

        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False
