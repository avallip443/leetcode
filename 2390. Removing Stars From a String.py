"""
Solution: Use a stack to store the valid character. Iterate over the string. If the char is a star and the stack is not empty, pop the stack (remove the char left of the string). Otherwise add the char.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for c in s:
            if stack and c == "*":
                stack.pop()
            else:
                stack.append(c)
            
        return "".join(stack)
    
