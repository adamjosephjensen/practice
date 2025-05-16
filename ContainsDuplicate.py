from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Based on the second, more concise Solution from the notebook
        return len(nums) != len(set(nums))
