"""
Solution: Use hashmap to get count for each character. Return is the len of the set of hashmap's values == len(hashmap) (true if each key has unique value)

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        count = {}

        for n in arr:
            count[n] = 1 + count.get(n, 0)
        
        return len(set(count.values())) == len(count)
        
