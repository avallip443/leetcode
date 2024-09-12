"""
Solution: Prefix sum. Initalize prefix and max to 0. Iterate over array and add the current altitude to the prefix, then update the max based on the current prefix (net gain in altitude at ih pos). Return max.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        prefix = 0
        max_alt = 0

        for a in gain:
            prefix += a
            max_alt = max(max_alt, prefix)
        
        return max_alt
        
