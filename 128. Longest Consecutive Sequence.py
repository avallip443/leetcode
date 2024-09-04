"""
Brute: Sort the array and check for sequences, but sorting is O(nlogn) time

Solution: Find the beginning of a possible sequence and track how many subsequent numbers exist.
- Convert the given array into a set to check existance of element in O(1) time
- Eg. if the seq should start with 1, check if 0 exists to prove its the start
- Track how many are in the seq and if its the longest length so far

Time complexity: O(n) - elements visited max 2 times
Space complexity: O(1)
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numsSet = set(nums)
        longest_len = 0
        length = 0
        
        for n in nums:
            if (n - 1) not in numsSet:
                length = 0
                
                while (n + length) in numsSet:
                    length += 1
                
                longest_len = max(longest_len, length)

        return longest_len
