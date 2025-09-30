from typing import List

class BinarySearch:
    def search(self, nums: List[int], target: int) -> int:
        # Using iterative approach from notebook as it's generally preferred
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # Recursive version from notebook for completeness, though iterative is often used.
    def recursive_search(self, nums: List[int], target: int) -> int:
        def _search(left, right):
            if left > right:
                return -1
            guess_index = (left + right) // 2
            guess_val = nums[guess_index]
            if guess_val == target:
                return guess_index
            if guess_val < target:
                return _search(guess_index + 1, right)
            return _search(left, guess_index - 1)
        return _search(0,len(nums)-1)
