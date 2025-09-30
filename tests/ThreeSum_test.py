import pytest
from typing import List
from prac.ThreeSum import Solution # Assuming the file is renamed to threesum.py or adjust import

# Helper function to sort the results for robust comparison
# The order of triplets in the output list and the order of numbers within a triplet do not matter.
def sort_triplets_for_comparison(result: List[List[int]]) -> List[List[int]]:
    return sorted([sorted(triplet) for triplet in result])

# Instantiate the solution class for use in tests
solution = Solution()

def test_example_1():
    """Tests the first example from the problem description."""
    nums = [-1,0,1,2,-1,-4]
    # print(sorted(nums)) # This print can be removed or kept for debugging
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
    nums = [-1, 0, 1, 2, -1, -4, -1, 2]
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
    nums = [1, 2, 3]
    expected = []
    actual = solution.threeSum(nums)
    assert sort_triplets_for_comparison(actual) == sort_triplets_for_comparison(expected)

def test_larger_numbers_and_varied_signs():
    """Tests with larger numbers and a mix of positive and negative values."""
    nums = [-25, 10, 15, -5, -10, 20, 0]
    expected = [[-25,10,15], [-10,-5,15], [-10,0,10]]
    actual = solution.threeSum(nums)
    assert sort_triplets_for_comparison(actual) == sort_triplets_for_comparison(expected)

def test_input_requiring_careful_duplicate_handling():
    """Tests a scenario that can easily produce duplicate triplets if not handled well."""
    nums = [-1,0,1,0]
    expected = [[-1,0,1]]
    actual = solution.threeSum(nums)
    assert sort_triplets_for_comparison(actual) == sort_triplets_for_comparison(expected)

def test_input_with_many_duplicates_and_zeros():
    nums = [0,0,0,0,-1,-1,-1,1,1,1,2,2,-2,-2]
    expected = [[0,0,0], [-1,-1,2], [-1,0,1], [-2,0,2], [-2,1,1]]
    actual = solution.threeSum(nums)
    assert sort_triplets_for_comparison(actual) == sort_triplets_for_comparison(expected)
