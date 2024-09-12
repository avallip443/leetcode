"""
Solution: Use variable sliding window. Iterate over list and track number of zeros encountered. If zeroes > 1, increment l and decrement the zeroes count if a removed value was a zero until zeroes <= 1. Update the max length (just r - l to account for the 'removed' zero)

Time complexity: O(m)
Space complexity: O(1)
"""

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        zeroes = 0
        max_len = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes += 1
            
            while zeroes > 1:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1
            
            max_len = max(max_len, (r - l))
        
        return max_len
    
