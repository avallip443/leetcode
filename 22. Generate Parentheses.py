"""
Solution: 
i. Only add ) when there are more ( and both are <= n.
ii. Only add ( when both numbers of (, ) are equal and ( <= n
iii. Sequence valid until ( == ) == n
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        stack = []
        res = []

        def backtrack(openC, closeC):
            if openC == closeC == n:
                res.append("".join(stack))
                return
            
            if openC < n:
                stack.append("(")
                backtrack(openC + 1, closeC)
                stack.pop()
            if closeC < openC:
                stack.append(")")
                backtrack(openC, closeC + 1)
                stack.pop()

        backtrack(0, 0)
        return res
