import pytest
from typing import List
from prac.TwoSum import Solution

solution = Solution()

def test_example_1():
    nums = [2,7,11,15]
    target = 9
    result = solution.twoSum(nums, target)
    assert sorted(result) == sorted([0,1])

def test_example_2():
    nums = [3,2,4]
    target = 6
    result = solution.twoSum(nums, target)
    assert sorted(result) == sorted([1,2])

def test_example_3():
    nums = [3,3]
    target = 6
    result = solution.twoSum(nums, target)
    assert sorted(result) == sorted([0,1])

def test_negative_numbers():
    nums = [-1, -3, 7, 15]
    target = 4
    result = solution.twoSum(nums, target)
    assert sorted(result) == sorted([1,2]) # -3 + 7 = 4

def test_zero_in_numbers():
    nums = [0, 4, 3, 0]
    target = 0
    result = solution.twoSum(nums, target)
    assert sorted(result) == sorted([0,3])
