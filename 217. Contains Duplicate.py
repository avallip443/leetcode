"""
Solution 1: Initalize set and add elements to it. Return true if the current element already exists in the set.
Solution 2: Return if len(nums) != len(set(nums)), since set(nums) contains distinct elements and duplicates should mean the number of elements in it is fewer. 
"""

class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Solution 1
        my_set = set()

        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False

        # Solution 2
        return len(nums) != len(set(nums))
