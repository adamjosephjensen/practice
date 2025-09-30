# Products of Array Except Self
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

from typing import List

class _2025_09_30_Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, return an array output
        where output[i] is the product of all the elements of nums except nums[i].
        
        Lower bound: O(n) to scan the numbers
        Brute force: for each i, multiply all values except i, O(n^2)

        Key idea: make a forward-multiplied array, then go backwards and multiply from the end
        Combine the two arrays.
        """
        n = len(nums)
        pre, suf, ans = [1] * n, [1] * n, [1] * n

        for i in range(1, n): # skip the first element
            pre[i] = pre[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1): # skip the last element, include 0
            suf[i] = suf[i+1] * nums[i+1]
        
        for i in range(n):
            ans[i] = pre[i] * suf[i]

        return ans

class OldSolution:
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

Solution = _2025_09_30_Solution
