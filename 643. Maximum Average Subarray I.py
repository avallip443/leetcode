"""
Solution: Use sliding window. The average of first window to initialize the max (accounts of max avg being negative)
- Starting from k, iterate through the rest of the windows and update the max

Time complexity: O(n)
Space complexity: O(1)
"""
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        curr_sum = sum(nums[:k])
        max_avg = curr_sum / float(k)

        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]            
            max_avg = max(max_avg, curr_sum / float(k))
        
        return max_avg
