"""
Solution: Strings are anagrams if they have the same characters and quantity for each character.
- Use a hashmap to map the quantity and combination of characters to a list of strings that match it
- Key: array of len 26 (for each letter) where each index represents the number of each character
- Index of chars will be determined by subtracing the ASCII value of the char from the ASCII value of 'a'
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

        my_hash = defaultdict(list)

        for s in strs:
            countChars = [0] * 26  # each index for each letter

            for char in s:
                countChars[ord(char) - ord("a")] += 1  # add for each letter occurance
            
            my_hash[tuple(countChars)].append(s)

        return my_hash.values()
        
