# Products of Array Except Self
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

from typing import List

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

