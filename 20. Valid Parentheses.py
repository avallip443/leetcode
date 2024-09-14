"""
Solution: Use stack to track open brackets and pop them when the corresponding closing bracket is encountered.
- Initalize stack and hashmap to map closing to opening brackers
- Iterate over s. If curr is a closing bracket, check if the corresponding closing bracket is the top of the stack and remove it, otherwise return False. If curr is an opening bracket, add it to the stack.
- Return True if the stack it empty at the end

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        closingBrackets = { "}" : "{", "]" : "[", ")" : "(" }

        for i in s:
            if i in closingBrackets:
                if stack and closingBrackets[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False
        
