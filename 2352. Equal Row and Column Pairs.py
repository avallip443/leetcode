"""
Solution: Use hash to store all rows and their frequencies. Then, iterate and get all cols, then check if the col exists in the row hash (i.e. ri and ci are the same). If so increment count by the row's frequencies. 

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows = defaultdict(int)
        count = 0
        
        for row in grid:
            rows[str(row)] += 1

        for i in range(len(grid)):
            col = [grid[row][i] for row in range(len(grid))]  # get col
            count += rows[str(col)]
        
        return count
