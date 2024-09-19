"""
Solution: Strings are anagrams if they have the same characters and counts. Use hashmap (with values as lists) to group words with the same letter/counts (use array of 26 for anagram signature).
Eg. key [1, 1, 1] will map to list of strings like 'abc', 'bca', etc

Time complexity: O(m * n) - m = # of given strings, n = avg len of str
Space compelxity: O(n)
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        groups = defaultdict(list)
        res = []

        for s in strs:
            signature = [0] * 26  # idx for each letter
            for c in s:
                signature[ord(c) - ord('a')] += 1

            groups[tuple(signature)].append(s)
        
        return groups.values()
        
