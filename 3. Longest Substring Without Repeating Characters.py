"""
Solution: Use sliding window to get max length withut duplicates
- Initalize left pointer and set to storing visited values
- Use right pointer to iterate over s
- While the current char is in the set, remove the leftmost char, otherwise add the current char in the set
- Update the max length if needed

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        """
        :type s: str
        :rtype: int
        """

        visited = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len
      
