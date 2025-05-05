# Products of Array Except Self
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

from typing import List
import pytest

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        # fill an array with the products of the prior numbers up to i
        prefix = 1
        for i in range(len(nums)):
            products[i] = prefix
            prefix *= nums[i]
        
        # work backwards and multiply by the numbers from i + 1 to n
        suffix = 1
        # Iterate backwards through indices (from len(nums)-1 down to 0)
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= suffix
            suffix *= nums[i]

        return products


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

# To run these tests, navigate to the directory containing the file
# in your terminal and run the command: pytest ProductsOfArrayExceptSelf.py

