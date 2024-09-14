"""
Solution: Use a stack to store operation results. Iterate over tokens and when an operator is encountered, pop the last two items from the stack, calculate the operation, and append it. Finally, return the first element in the list.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for n in tokens:
            if n == "+":
                stack.append(stack.pop() + stack.pop())
            elif n == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif n == "*":
                stack.append(stack.pop() * stack.pop())
            elif n == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(n))

        return stack[0]
