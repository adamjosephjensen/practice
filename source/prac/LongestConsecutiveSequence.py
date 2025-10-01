# Longest Consecutive Sequence
# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:

# Input: nums = [0,3,2,5,4,6,1,1]

# Output: 7
# Constraints:

# 0 <= nums.length <= 1000
# -10^9 <= nums[i] <= 10^9
from typing import List

class _2025_09_30_Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Given an array of integers nums
        return the length of the longest consecutive sequence
        of elements that can be formed.

        Input: [2, 20, 4, 10, 3, 4, 5]
        Output: 4

        Naive: sort the list, then scan it for sequences, tracking the current + max
        """
        _set = set(nums)
        _max = 0
        for n in nums:
            if n - 1 not in _set:
                val = n
                while val + 1 in _set:
                    val += 1
                _max = max(val - n + 1, _max)
        
        return _max

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        bag = frozenset(nums)
        longest = 0
        for n in nums:
            if n - 1 not in bag:
                # number could be the start of the longest sequence
                seq = n
                while seq + 1 in bag:
                    seq += 1
                longest = max(seq - n + 1, longest)

        return longest

Solution = _2025_09_30_Solution 
