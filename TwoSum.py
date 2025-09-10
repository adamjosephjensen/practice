from typing import List

class Pre_2025_09_09_Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Based on the cleaner solution from the notebook
        indices = {}
        for idx, n in enumerate(nums):
            complement = target - n
            if complement in indices:
                complement_index = indices[complement]
                return [complement_index, idx]
            indices[n] = idx
        return [] # Should not be reached if problem guarantees a solution

Solution = Pre_2025_09_09_Solution
