"""
Solution: Use two pointers - one tracks chars in s and the other in t
- If curr t char matches curr s char, incr s pointer
- If s pointer = s length, return True

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) < 1:
            return True

        substr_pointer = 0

        for c in t:
            if c == s[substr_pointer]:
                substr_pointer += 1
                if substr_pointer == len(s):
                    return True
        
        return False
      
