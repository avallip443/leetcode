"""
Solution: Use sliding window. Expand the window rightwards until all the characters of t are in the window, then remove the leftmost character until it isnt't (trims unnecessary leftmost chars)
- Use vars to track need and have chars
- Use vars to track pointers for res substring and min length

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        # edge case
        if t == "": return ""

        # hashmaps for t, window in s
        countT, window = {}, {}

        # populate countT
        for i in t:
            countT[i] = 1 + countT.get(i, 0)
        
        have, need = 0, len(countT)
        resPtr, resLen = [-1, -1], float('infinity')
        l = 0

        for r in range(len(s)):
            # add r ptr value
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            # char in t also in window
            if char in countT and window[char] == countT[char]:
                have += 1

                while have == need:
                    # update res
                    if (r - l + 1) < resLen:
                        resLen = r - l + 1
                        resPtr = [l, r]

                    # trim unneeded leftmost chars
                    window[s[l]] -= 1
                    if s[l] in countT and window[s[l]] < countT[s[l]]:
                        have -= 1

                    l += 1
        
        l, r = resPtr
        return s[l:r+1] if resLen != float('infinity') else ""
