from typing import List

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

# Example 2:

# Input: nums = [0,1,1]

# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]

# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# Constraints:

# 3 <= nums.length <= 1000
# -10^5 <= nums[i] <= 10^5V
# Input: nums = [-4,-1,-1,0,1,2]
from typing import List # Ensure List is imported for the test functions if not globally


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for c in range(len(nums)-2):
            if c >= 1 and nums[c] == nums[c - 1]:  # skip duplicates
                continue
            # want -num[c] = num[l] + num[r], where num[l] <= num[r] if l < r
            l, r = c+1, len(nums) - 1 # last index
            while l < r:
                total = nums[c] + nums[l] + nums[r]
                if total == 0:
                    triplets.append([nums[c], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return triplets

                    






class FirstSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        val_to_index = dict(zip(nums, range(len(nums)))) # how does this work with repeats? I think later nums will just overwrite earlier nums
        triplets = set()
        for o_i, o_val in enumerate(nums):
            for i_i, i_val in enumerate(nums):
                # want o_val + i_val + x == 0, where the indices are all distinct
                complement = -1 * (o_val + i_val)
                triplet = (complement in val_to_index)
                if triplet and o_i != i_i and o_i != val_to_index[complement] and i_i != val_to_index[complement]:
                    triplets.add(tuple(sorted([o_val, i_val, complement])))

        return [list(t) for t in triplets]


# tests
import pytest

# Helper function to sort the results for robust comparison
# The order of triplets in the output list and the order of numbers within a triplet do not matter.
def sort_triplets_for_comparison(result: List[List[int]]) -> List[List[int]]:
    return sorted([sorted(triplet) for triplet in result])

# Instantiate the solution class for use in tests
solution = Solution()

def test_example_1():
    """Tests the first example from the problem description."""
    nums = [-1,0,1,2,-1,-4]
    print(sorted(nums))
    expected = [[-1,-1,2],[-1,0,1]]
    actual = solution.threeSum(nums)
    assert sort_triplets_for_comparison(actual) == sort_triplets_for_comparison(expected)

def test_example_2():
    """Tests the second example from the problem description (no solution)."""
    nums = [0,1,1]
    expected = []
    actual = solution.threeSum(nums)
    assert sort_triplets_for_comparison(actual) == sort_triplets_for_comparison(expected)

def test_example_3():
    """Tests the third example from the problem description (all zeros)."""
    nums = [0,0,0]
    expected = [[0,0,0]]
    actual = solution.threeSum(nums)
    assert sort_triplets_for_comparison(actual) == sort_triplets_for_comparison(expected)

def test_no_solution_simple():
    """Tests a case where no three numbers sum to zero."""
    nums = [1, 2, 3, 4, 5]
    expected = []
    actual = solution.threeSum(nums)
    assert sort_triplets_for_comparison(actual) == sort_triplets_for_comparison(expected)

def test_all_zeros_multiple_inputs():
    """Tests with more than three zeros, should still result in one [0,0,0] triplet."""
    nums = [0,0,0,0,0]
    expected = [[0,0,0]]
    actual = solution.threeSum(nums)
    assert sort_triplets_for_comparison(actual) == sort_triplets_for_comparison(expected)

def test_mixed_numbers_multiple_solutions():
    """Tests with mixed positive and negative numbers leading to multiple solutions."""
    nums = [-2, 0, 1, 1, 2, -1] # [-2,0,2], [-2,1,1], [-1,0,1]
    expected = [[-2,0,2], [-2,1,1], [-1,0,1]]
    actual = solution.threeSum(nums)
    assert sort_triplets_for_comparison(actual) == sort_triplets_for_comparison(expected)

def test_duplicates_in_input_handled_correctly():
    """Tests that duplicate numbers in input don't lead to duplicate triplets in output."""
    nums = [-1, 0, 1, 2, -1, -4, -1, 2] # [-1,-1,2], [-1,0,1]
    # Sorted: -4, -1, -1, -1, 0, 1, 2, 2
    # Triplets:
    # (-1, -1, 2)
    # (-1, 0, 1)
    # (-4, 2, 2)
    expected = [[-1,-1,2], [-1,0,1], [-4,2,2]]
    actual = solution.threeSum(nums)
    assert sort_triplets_for_comparison(actual) == sort_triplets_for_comparison(expected)

def test_min_length_input_sum_to_zero():
    """Tests with the minimum allowed length (3) that sums to zero."""
    nums = [-10, 3, 7]
    expected = [[-10, 3, 7]]
    actual = solution.threeSum(nums)
    assert sort_triplets_for_comparison(actual) == sort_triplets_for_comparison(expected)

def test_min_length_input_not_sum_to_zero():
    """Tests with the minimum allowed length (3) that does not sum to zero."""
    nums = [1, 2, 3] # Constraint: 3 <= nums.length
    expected = []
    actual = solution.threeSum(nums)
    assert sort_triplets_for_comparison(actual) == sort_triplets_for_comparison(expected)

def test_larger_numbers_and_varied_signs():
    """Tests with larger numbers and a mix of positive and negative values."""
    nums = [-25, 10, 15, -5, -10, 20, 0]
    # Possible:
    # (-25, 10, 15)
    # (-10, -5, 15)
    # (-25, 5, 20) -> no 5
    # (-10, 0, 10)
    # (-5, -10, 15) - already covered
    # (0, 10, -10) - already covered
    expected = [[-25,10,15], [-10,-5,15], [-10,0,10]]
    actual = solution.threeSum(nums)
    assert sort_triplets_for_comparison(actual) == sort_triplets_for_comparison(expected)

def test_input_requiring_careful_duplicate_handling():
    """Tests a scenario that can easily produce duplicate triplets if not handled well."""
    nums = [-1,0,1,0] # Should be [[-1,0,1]]
    expected = [[-1,0,1]]
    actual = solution.threeSum(nums)
    assert sort_triplets_for_comparison(actual) == sort_triplets_for_comparison(expected)

def test_input_with_many_duplicates_and_zeros():
    nums = [0,0,0,0,-1,-1,-1,1,1,1,2,2,-2,-2]
    # Expected:
    # [0,0,0]
    # [-1,-1,2]
    # [-1,0,1]
    # [-2,0,2]
    # [-2,1,1]
    expected = [[0,0,0], [-1,-1,2], [-1,0,1], [-2,0,2], [-2,1,1]]
    actual = solution.threeSum(nums)
    assert sort_triplets_for_comparison(actual) == sort_triplets_for_comparison(expected)
