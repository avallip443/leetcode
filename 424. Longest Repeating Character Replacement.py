"""
Solution: Use sliding window - window is valid if the length - most frequent char <= k
- Use a hashmap to map letters in window to frequency
- Use two pointers to iterate through the array (tracks start/end of window)
- If len - most freq <= k, inc right pointer
- Otherwise, decr left pointer and remove current letter count

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        count = {}
        max_len = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len
        
