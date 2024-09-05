"""
Solution:
- Return len(chars) if len < 2
- Initalize 2 points - index to write and index to start of char group
- Iterate over chars and check if curr != next/end of list to insert current char
- Then check if i > start to insert count
- Finally, delete chars after last write and return len

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        length = len(chars)

        if length < 2:
            return length

        start = 0  # start of curr char group
        write = 0  # pos to write next

        for i, c in enumerate(chars):
            if (i + 1 == length) or (c != chars[i+1]):
                chars[write] = c
                write += 1

                if i > start:
                    count = i - start + 1
                    for n in str(count):  # accounts for counts > 9
                        chars[write] = n
                        write += 1
                    start = i + 1
                else: 
                    start += 1
        
        del chars[write:]
        return len(chars)
