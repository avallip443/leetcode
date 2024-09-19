"""
Solution: If element in beginning of sequence, check if subsequent elements exist. Update max based on lengths of each seqeunce.
- Use set for O(1) access 

Time complexity: O(n) 
Space complexity: O(1)
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numsSet = set(nums)
        max_len = 0
        curr_len = 0

        for n in nums:
            if (n - 1) not in numsSet:  # start of seq
                length = 0

                while (n + length) in numsSet:  # next element exists
                    length += 1

                max_len = max(max_len, length)
        
        return max_len
        
