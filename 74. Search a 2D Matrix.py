'''
Since numbers are all sorted, use binary search to find the row with the range that may contain the target. Then, use binary search to find the target within that row. Return false is the row or the target could not be found.

Time complexity: O(logm + logn)
Space complexity: O(1)
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1

        while top <= bottom:
            currRow = (top + bottom) // 2

            if target > matrix[currRow][-1]:
                top = currRow + 1
            elif target < matrix[currRow][0]:
                bottom = currRow - 1
            else:
                break
            
        if not (top <= bottom):
            return False
        
        row = (top + bottom) // 2
        l, r = 0, cols -1

        while l <= r:
            m = (l + r) // 2

            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else: 
                return True

        return False
