"""
Solution: Use stack to track pairs [tempterature, index]. The goal is to append the [temp, index] when the temp is less than the stack top's temp and pop when it is greater. 
- If the temp is less, append the value since it is not greater than previous temperature
- If the temp is greater, continue to pop the top element until the current is less than the top. At the same time, update the difference in days for each popped element.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        res = [0] * len(temperatures)
        stack = []  # holds pairs [temp, idx]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:  # curr greater temp than prev
                stackT, stackI = stack.pop()
                res[stackI] = (i - stackI)  # different in days
            stack.append([t, i])
        
        return res
