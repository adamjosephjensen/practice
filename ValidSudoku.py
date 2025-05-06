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

class Solution:
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

import pytest
from typing import List

# Test Cases using pytest

def test_valid_board_example():
    solution = Solution()
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert solution.isValidSudoku(board) == True

def test_invalid_board_example_sub_box():
    solution = Solution()
    board = [
        ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","1",".",".",".",".",".","3"], # Duplicate '1' in top-left 3x3 sub-box
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert solution.isValidSudoku(board) == False

def test_empty_board():
    solution = Solution()
    board = [
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]
    ]
    assert solution.isValidSudoku(board) == True

def test_full_valid_board():
    solution = Solution()
    board = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]
    assert solution.isValidSudoku(board) == True

def test_invalid_row_duplicate():
    solution = Solution()
    board = [
        ["5","3",".",".","7",".",".",".","5"], # Duplicate '5' in first row
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","."],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert solution.isValidSudoku(board) == False

def test_invalid_column_duplicate():
    solution = Solution()
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        ["5",".",".",".","8",".",".","7","9"] # Duplicate '5' in first column
    ]
    assert solution.isValidSudoku(board) == False

def test_invalid_sub_box_duplicate_different_from_example():
    solution = Solution()
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".","8","5"], # '8' here
        [".",".",".",".","8",".",".","7","8"]  # Duplicate '8' in bottom-right 3x3 sub-box
    ]
    assert solution.isValidSudoku(board) == False

def test_partially_filled_valid_board():
    solution = Solution()
    board = [
        ["1",".",".",".",".",".",".",".","."],
        [".","2",".",".",".",".",".",".","."],
        [".",".","3",".",".",".",".",".","."],
        [".",".",".","4",".",".",".",".","."],
        [".",".",".",".","5",".",".",".","."],
        [".",".",".",".",".","6",".",".","."],
        [".",".",".",".",".",".","7",".","."],
        [".",".",".",".",".",".",".","8","."],
        [".",".",".",".",".",".",".",".","9"]
    ]
    assert solution.isValidSudoku(board) == True

# To run these tests, navigate to the directory containing the file
# in your terminal and run the command: pytest ValidSudoku.py
