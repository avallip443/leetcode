"""
Solution: Use 2 pointers - one tracks pos where next non-zero element should be place and the other iterates over the array
- When curr is non-zero, swap it with non-zero pos pointer, then inc pointer

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        non_zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero], nums[i] = nums[i], nums[non_zero]
                non_zero += 1
        
        return nums
