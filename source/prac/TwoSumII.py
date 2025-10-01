from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Given an array of integers numbers that is sorted in non-decreasing order.
        Return the indices (1-indexed) of two numbers, [index1, index2]

        such that they add up to a given target number target and index1 < index2

        There will always be exactly one valid solution.
        """
        n = len(numbers)
        l = 0
        r = n - 1
        while l < r:
            _sum = numbers[l] + numbers[r] - target
            if _sum < 0: # _sum too small
                l += 1
            elif 0 < _sum: # _sum too big
                r -= 1
            elif _sum == 0: # we found the root
                return [l + 1, r + 1]
            else:
                assert 0
        assert 0 
