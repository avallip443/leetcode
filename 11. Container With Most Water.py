"""
Solution: Use two pointers to track heights and inc/decr the smaller one.
- Calculate volume and update max_vol is necessary
- If the left height < right height, inc left
- If the right height < left height, decr right

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        max_vol = 0
        l, r = 0, len(height) - 1

        while l < r:
            volume = (r - l) * min(height[l], height[r])
            max_vol = max(max_vol, volume)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_vol
