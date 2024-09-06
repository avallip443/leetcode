"""
Solution: Use 2 pointers to track max left/right and use the difference between the smaller max left/right and current height to find how much water the ith position holds.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height:
            return 0

        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        volume = 0

        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                volume += max_l - height[l]
            else: 
                r -= 1
                max_r = max(max_r, height[r])
                volume += max_r - height[r]

        return volume
