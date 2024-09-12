"""
Solution: Use prefix/suffix sum. Initalize prefix to 0, suffix to sum(nums). Iterate pver th array, update suffix (subtract), check if suffix == prefix (return i), update prefix (add). Return -1 otherwise.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = 0
        suffix = sum(nums)

        for i in range(len(nums)):
            suffix -= nums[i]

            if suffix == prefix:
                return i
            
            prefix += nums[i]
        
        return -1
