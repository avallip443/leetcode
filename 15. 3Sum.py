"""
Solution: Given an anchor, find two other numbers whose total sum = 0. To find these numbers, use two pointers at the start/end and inc/decr depending on if the sum is smaller/larger than 0.
- To prevent duplicates, sort the array and if the curr == next, skip since that pair has already been used.

Time complexity: O(n^2)
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            
            start, end = i + 1, len(nums) - 1

            while start < end:
                curr_sum = n + nums[start] + nums[end]

                if curr_sum < 0:
                    start += 1
                elif curr_sum > 0:
                    end -= 1
                else:
                    res.append([n, nums[start], nums[end]])
                    start += 1
                    
                    while nums[start] == nums[start-1] and start < end:
                        start += 1
            
        return res
            
