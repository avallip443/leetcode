"""
Solution: Area of rectange - height = smallest col in given section, width = # indexes that have height >= smallest. Use a stack to store increasing heights as an (index, height) pair where the index is that start of the rectange (eg. for ex 1, 4th pos height has (2, 2)).
-  Pop the stack if the current height is less than the top. Use the popped idx/height to calculate the rectangle defined by the popped col (height * (curr_index - popped_index)) and update max if needed. 
- The start index will either be the current index or the popped index.
- Add the current height/index otherwise.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        stack = []  # pairs of (idx, height)

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:  # height decreases, so update tracked heights
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area
