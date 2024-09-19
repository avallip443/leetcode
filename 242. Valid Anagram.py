"""
Solution: Both are anagrams if they have the same length, characters, and quantity of each character. Use hashmaps to count occurances and compare if their counts are the same.

Time complexity: O(s + t)
Space complexity: O(s + t)
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t): return False
        
        hashS = {}
        hashT = {}

        # count occurances of letters
        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)

        # check if they have same keys and values
        for k in hashS:
            if hashS.get(k) != hashT.get(k):
                return False
            
        return True
        
