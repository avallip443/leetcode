"""
Solution: Use 2 pointers to track the start/end of the range. Find the midpoint and compare to target; left pointer is m+1 if target is larger, right pointer is m-1 if target is smaller, and return m if it's equal to target.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1
