"""
Solution: Both are anagrams if they have the same length, characters, and quantity of each character.
- Check if strings are the same length
- Use two hash maps to map characters to its occurances in each string
- Iterate through one hash map's keys and compare it to the other's values
- True if all values are the same
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

        if len(s) != len(t):
            return False


        hash_s, hash_t = {}, {}

        for i in range(len(s)):
            hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
            hash_t[t[i]] = 1 + hash_t.get(t[i], 0)
        
        for i in hash_s:
            if hash_s.get(i) != hash_t.get(i, 0):
                return False

        return True
