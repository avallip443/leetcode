"""
Cases for lengths:
1. word1 == word2
2. word1 > word2
3. word1 < word2

Solution: Find min length and iterate through chars for both strings simultaneously 
- Once the min length of chars are added, add the remaining chars from both word1 and word2

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        min_length = min(len(word1), len(word2))
        res = ""
        i = 0

        for i in range(min_length):
            res += word1[i] + word2[i]
            i += 1
        res += word2[i:]
        res += word1[i:]
            
        return res
