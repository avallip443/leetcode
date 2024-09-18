"""
Solution: When adding an asteroid, there is either no collision (same sign) or a collision (only when left is pos and right is neg):
i. Left > right (pop right)
ii. Right > left (pop left)
iii. Left = right (pop both)
Use stack since elements are accessed in linear order and only the top would be affect for each collision check.
- Iterate through array. While a collision can happend, check the 3 conditions. Otherwise, add the element to the stack.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if abs(a) > abs(stack[-1]): stack.pop()  # right > left
                elif abs(a) < abs(stack[-1]): break  # left > right
                else: stack.pop(); break
            else: 
                stack.append(a)
        
        return stack
