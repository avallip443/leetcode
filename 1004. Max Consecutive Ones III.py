"""
Solution: Use variable sliding window. While iterating over list, keep track of the number of zeros in the window. If the zeros > k, then increment l and decrement the zero count if the old l value was a 0 until zeros <= k. Otherwise, update max value

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        max_count = 0
        zeros = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            max_count = max(max_count, r + 1 - l)
        
        return max_count
    
