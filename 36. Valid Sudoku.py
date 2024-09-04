"""
Note: Don't need to check if sudoku is solvable (eg. contradicting values in row even if 3 conditions are fulfilled)

Solution: Use hashsets for rows, columns, and squares to check for duplicates
- Create a hashset for rows/cols/square. While iterating over each element, check if a duplicate exists
- Each square is associated with 3 rows and 3 cols, so the key for each square will be x // 3, where x is the specific row/col being accessed 

Time complexity: O(n^2)
Space complexity: O(n)
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)  # key = (row / 3, col / 3)

        for row in range(9):
            for col in range(9):
                curr = board[row][col]
                if curr == ".":
                    continue
                if (curr in rows[row]
                    or curr in cols[col]
                    or curr in squares[(row // 3, col // 3)]):
                    return False
                
                rows[row].add(curr)
                cols[col].add(curr)
                squares[(row // 3, col // 3)].add(curr)

        return True
