"""
Solution: Use hashmap to store visited values/indexes and check if target-current in hash.

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
        
        visited = {}

        for i, t in enumerate(nums):
            diff = target - t
            
            if diff in visited:
                return [i, visited[diff]]
            visited[t] = i
    
