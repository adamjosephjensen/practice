import pytest
from typing import List
from ContainsDuplicate import Solution

solution = Solution()

def test_example_1():
    nums = [1,2,3,1]
    assert solution.hasDuplicate(nums) == True

def test_example_2():
    nums = [1,2,3,4]
    assert solution.hasDuplicate(nums) == False

def test_example_3():
    nums = [1,1,1,3,3,4,3,2,4,2]
    assert solution.hasDuplicate(nums) == True

def test_empty_list():
    nums = []
    assert solution.hasDuplicate(nums) == False

def test_single_element_list():
    nums = [1]
    assert solution.hasDuplicate(nums) == False

def test_all_duplicates():
    nums = [7,7,7,7]
    assert solution.hasDuplicate(nums) == True
