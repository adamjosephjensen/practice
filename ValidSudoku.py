# Valid Sudoku
# You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

# Input: board = 
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: true

# Input: board = 
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: false
# Explanation: There are two 1's in the top-left 3x3 sub-box.

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

from typing import List

class _2025_09_29_Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        keep track of contents with 27 set objects
        for each cell i, j
            check row contraints
            check col constraints
            check box constraints
        
        incremental plan: could make test cases for each check
        then test it one at a time
        """
        n = 9
        _row = [set() for _ in range(n)] 
        _col = [set() for _ in range(n)]
        _box = [set() for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                # print(f"considering value: {board[r][c]} at row: {r} col: {c}")
                if board[r][c] == ".":
                    continue
                
                val = int(board[r][c])

                # gotta be in 1-9
                if val not in set([1,2,3,4,5,6,7,8,9]):
                    return False
                
                # check row duplicate
                if val in _row[r]:
                    print(f"row duplicate at row: {r} col: {c} value: {val}")
                    print(f"_row[r]: {_row[r]}")
                    return False
                else:
                    print(f"adding {val} to row: {r}")
                    _row[r].add(val)
                # check column duplicate
                if val in _col[c]:
                    print("col duplicate")
                    return False
                else:
                    # print(f"adding {val} to col: {c}")
                    _col[c].add(val)
                # check box duplicate
                sub_box_row = r // 3
                sub_box_col = c // 3
                flattened_i = sub_box_row * 3 + sub_box_col

                if val in _box[flattened_i]:
                    print("sub-box duplicate")
                    return False
                else:
                    # print(f"adding {val} to flattened_i: {flattened_i}")
                    _box[flattened_i].add(val)

        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """ uses three lists of 9 sets to check the duplicate constraints """
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        gridsets = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                s = board[row][col]
                if s == ".":
                    continue
                i = int(s)
                g = (row // 3) * 3 + col // 3
                
                if i in row_sets[row] or i in col_sets[col] or i in gridsets[g]:
                    return False
                
                row_sets[row].add(i)
                col_sets[col].add(i)
                gridsets[g].add(i)

        return True


class FirstAttemptSolution:
    @staticmethod
    def parse_int_or_none(s):
        try:
            return int(s)
        except (ValueError, TypeError):
            return None

    @staticmethod
    def check_row(s: List[str]) -> bool:
        print("LOG check_row | row: ", s)
        row = [i for i in [Solution.parse_int_or_none(x) for x in s] if i]
        
        # check duplicates
        as_set = frozenset(row)
        return len(row) == len(as_set)
    
    @staticmethod
    def check_box(box: List[List[str]]) -> bool:
        nums = []
        for row in range(3):
            for col in range(3):
                val = box[row][col]
                if val in '0123456789':
                    nums.append(int(val))

        as_set = frozenset(nums)
        return len(as_set) == len(nums)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [Solution.check_row(row) for row in board]
        if False in rows:
            return False

        cols = []
        for slow in range(9):
            is_valid_column = Solution.check_row([board[f][slow] for f in range(9)])
            cols.append(is_valid_column)
        if False in cols:
           return False

        # check nine three by three grids
        top_left = [board[r][:3] for r in range(0, 3)]
        mid_left = [board[r][:3] for r in range(3, 6)]
        bot_left = [board[r][:3] for r in range(6, 9)]

        top_midd = [board[r][3:6] for r in range(0, 3)]
        mid_midd = [board[r][3:6] for r in range(3, 6)]
        bot_midd = [board[r][3:6] for r in range(6, 9)]

        top_righ = [board[r][6:9] for r in range(0, 3)]
        mid_righ = [board[r][6:9] for r in range(3, 6)]
        bot_righ = [board[r][6:9] for r in range(6, 9)]
        
        sub_grids = [top_left, mid_left, bot_left, top_midd, mid_midd, bot_midd, top_righ, mid_righ, bot_righ]
        valid_grids = [Solution.check_box(g) for g in sub_grids]
        if False in valid_grids:
            return False

        return True

Solution = _2025_09_29_Solution
