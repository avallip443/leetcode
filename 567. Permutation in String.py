"""
Solution: Use 2 arrays to track the occurances of each letter in both string and track the number of matches they have.
- First populate the arrays with the first len(s1) chars (window for problem)
- Then count the matches
- If matches == 26 (same occurances for all 26 letters), return True
- Otherwise, slide the window right (and update matches) and remove the leftmost element from the old window 

Time complexity: O(n) -> 26 * n 
Space complexity: O(n)
"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if len(s1) > len(s2): return False 

        s1Count, s2Count = [0] * 26, [0] * 26
        matches = 0
        l = 0

        for i in range(len(s1)):  # populate occurances
            s1Count[ord(s1[i]) - ord('a')] += 1 
            s2Count[ord(s2[i]) - ord('a')] += 1 
        
        for i in range(26):  # check matches
            matches += 1 if s1Count[i] == s2Count[i] else 0
        
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            # check new right element added
            i = ord(s2[r]) - ord('a')
            s2Count[i] += 1
            if s2Count[i] == s1Count[i]:
                matches += 1
            elif s2Count[i] - 1 == s1Count[i]:  # matching before incr
                matches -= 1

            # check old left element to remove
            i = ord(s2[l]) - ord('a')
            s2Count[i] -= 1
            if s2Count[i] == s1Count[i]:
                matches += 1
            elif s2Count[i] + 1 == s1Count[i]:  # matching before decr
                matches -= 1
            
            l += 1

        return matches == 26
