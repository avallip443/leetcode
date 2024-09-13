"""
Solution: 
Operation 1 - check if they have the same letters with same frequencies
Operation 2 - check if they have the ame frequencies (since letters can change)

Time complexity: O(n + m) - len of word1, word2
Space complexity: O(n + m) - len of word1, word2
"""

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        
        c1 = Counter(word1)
        c2 = Counter(word2)

        n1 = Counter([v for v in c1.values()])
        n2 = Counter([v for v in c2.values()])

        return (c1 == c2) or (n1 == n2 and set(c1) == set(c2))
