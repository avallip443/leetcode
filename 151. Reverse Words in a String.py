"""
Solution: Use split() to split words by whitespace, then reverse the result and return the joint list as a string
Time complexity: O(n+m) - n = str len, m = # words
Space complexity: O(n) - n = str len
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = s.split()
        res = res[::-1]
        return " ".join(res)
