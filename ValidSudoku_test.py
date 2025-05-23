import pytest
from typing import List
from ValidSudoku import Solution

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
