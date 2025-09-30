import pytest
from typing import List # Ensure List is imported
from prac.ProductsOfArrayExceptSelf import Solution

# Test Cases using pytest

def test_example_case():
    solution = Solution()
    nums = [1, 2, 3, 4]
    expected = [24, 12, 8, 6]
    assert solution.productExceptSelf(nums) == expected

def test_with_zero():
    solution = Solution()
    nums = [1, 2, 0, 4]
    expected = [0, 0, 8, 0]
    assert solution.productExceptSelf(nums) == expected

def test_with_multiple_zeros():
    solution = Solution()
    nums = [1, 0, 3, 0]
    expected = [0, 0, 0, 0]
    assert solution.productExceptSelf(nums) == expected

def test_with_negative_numbers():
    solution = Solution()
    nums = [-1, 1, 0, -3, 3]
    expected = [0, 0, 9, 0, 0]
    assert solution.productExceptSelf(nums) == expected

def test_all_negative_numbers():
    solution = Solution()
    nums = [-1, -2, -3, -4]
    expected = [-24, -12, -8, -6]
    assert solution.productExceptSelf(nums) == expected

def test_two_elements():
    solution = Solution()
    nums = [2, 3]
    expected = [3, 2]
    assert solution.productExceptSelf(nums) == expected

def test_all_ones():
    solution = Solution()
    nums = [1, 1, 1, 1]
    expected = [1, 1, 1, 1]
    assert solution.productExceptSelf(nums) == expected

def test_mixed_positive_negative():
    solution = Solution()
    nums = [1, -2, 3, -4]
    expected = [24, -12, 8, -6]
    assert solution.productExceptSelf(nums) == expected
