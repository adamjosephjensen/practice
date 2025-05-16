import pytest
from typing import List # Add List if not already present from Solution
from LongestConsecutiveSequence import Solution

# Instantiate the solution class
solution = Solution()

def test_example_1():
    """Test case from example 1: nums = [2,20,4,10,3,4,5], expected output 4"""
    nums = [2,20,4,10,3,4,5]
    expected = 4
    assert solution.longestConsecutive(nums) == expected

def test_example_2():
    """Test case from example 2: nums = [0,3,2,5,4,6,1,1], expected output 7"""
    nums = [0,3,2,5,4,6,1,1]
    expected = 7
    assert solution.longestConsecutive(nums) == expected

def test_empty_list():
    """Test with an empty list, expected output 0"""
    nums = []
    expected = 0
    assert solution.longestConsecutive(nums) == expected

def test_single_element_list():
    """Test with a single element list, expected output 1"""
    nums = [100]
    expected = 1
    assert solution.longestConsecutive(nums) == expected

def test_all_elements_consecutive():
    """Test with all elements forming a consecutive sequence"""
    nums = [1, 2, 3, 4, 5]
    expected = 5
    assert solution.longestConsecutive(nums) == expected

def test_no_consecutive_sequence():
    """Test with no consecutive elements (all unique, far apart)"""
    nums = [10, 20, 30, 40]
    expected = 1
    assert solution.longestConsecutive(nums) == expected

def test_duplicates_affecting_sequence_count():
    """Test with duplicates that are part of the sequence"""
    nums = [1, 2, 2, 3, 4, 4, 4]
    expected = 4 # Sequence is 1, 2, 3, 4
    assert solution.longestConsecutive(nums) == expected

def test_duplicates_not_affecting_longest_sequence():
    """Test with duplicates where the longest sequence does not involve them directly extending it"""
    nums = [1, 2, 3, 10, 10, 10, 11, 12, 12]
    expected = 3
    assert solution.longestConsecutive(nums) == 3


def test_negative_numbers():
    """Test with negative numbers forming a sequence"""
    nums = [-1, -2, -3, 1, 0] # Sequence: -3, -2, -1, 0, 1
    expected = 5
    assert solution.longestConsecutive(nums) == expected

def test_sequence_around_zero():
    """Test with a sequence that includes zero"""
    nums = [-2, -1, 0, 1, 2]
    expected = 5
    assert solution.longestConsecutive(nums) == expected

def test_unsorted_list_clear_longest_sequence():
    """Test with an unsorted list that has a clear longest sequence"""
    nums = [100, 4, 200, 1, 3, 2] # Sequence: 1, 2, 3, 4
    expected = 4
    assert solution.longestConsecutive(nums) == expected

def test_multiple_sequences_pick_longest():
    """Test with multiple consecutive sequences, ensure the longest is returned"""
    nums = [1, 2, 3, 10, 11, 12, 13, 5, 6] # Longest is [10,11,12,13]
    expected = 4
    assert solution.longestConsecutive(nums) == expected

def test_sequence_with_large_gaps():
    """Test sequence with large gaps between numbers"""
    nums = [0, 100, 1, 200, 2, 300] # Longest is [0,1,2]
    expected = 3
    assert solution.longestConsecutive(nums) == expected

def test_all_same_numbers():
    """Test with all numbers being the same"""
    nums = [5, 5, 5, 5, 5]
    expected = 1
    assert solution.longestConsecutive(nums) == expected

def test_long_list_no_consecutive():
    """Test a longer list with no consecutive numbers"""
    nums = [i * 10 for i in range(100)] # 0, 10, 20, ..., 990
    expected = 1
    assert solution.longestConsecutive(nums) == expected

def test_long_list_all_consecutive():
    """Test a longer list with all numbers consecutive"""
    nums = list(range(100)) # 0, 1, ..., 99
    expected = 100
    assert solution.longestConsecutive(nums) == expected
