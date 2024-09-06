"""
Solution: Sort nums and set 2 pointers at the start/end
- Get sum of boht pointers' value and compare against k
- If less -> inc l
- If greater -> decr r
- If equal -> inc count and l, decr r

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if len(nums) < 2:
            return 0

        nums.sort()
        l, r = 0, len(nums) - 1
        count = 0

        while l < r:
            curr_sum = nums[l] + nums[r]

            if curr_sum < k:
                l += 1
            elif curr_sum > k: 
                r -= 1
            else:
                count += 1
                l += 1
                r -= 1
        
        return count
