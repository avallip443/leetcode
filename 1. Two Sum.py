"""
Brute: Use nested loops to add every pair to check if their sum is the target.
- Time complexity: O(n^2)

Optimized: Use a hashmap to map visited values and their indexes.
- Iterate over list and check if target - current value = value in hashmap.
Time complexity: O(n)
Space complexity: O(n)

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hash = {}

        for i, num in enumerate(nums):
            target_summand = target - num

            if target_summand in hash:
                return [hash[target_summand], i]
            hash[num] = i
        
