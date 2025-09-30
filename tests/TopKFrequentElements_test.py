import pytest
from typing import List, Dict # Keep Dict if any test helpers might use it
from prac.TopKFrequentElements import Solution

# --- Test Cases using pytest ---

def test_example_case():
    """Tests the example provided in many problem descriptions."""
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    expected = [1, 2]
    result = solution.topKFrequent(nums, k)
    assert set(result) == set(expected)
    assert len(result) == k

def test_k_equals_one():
    """Tests finding the single most frequent element."""
    solution = Solution()
    nums = [1, 2, 2, 3, 3, 3, 4]
    k = 1
    expected = [3]
    result = solution.topKFrequent(nums, k)
    assert set(result) == set(expected)
    assert len(result) == k

def test_k_equals_unique_elements():
    """Tests when k is the total number of unique elements."""
    solution = Solution()
    nums = [1, 1, 2, 3, 3, 3]
    k = 3
    expected = [3, 1, 2]
    result = solution.topKFrequent(nums, k)
    assert set(result) == set(expected)
    assert len(result) == k

def test_tie_in_frequency_within_top_k():
    """Tests when multiple numbers share the same frequency within the top k."""
    solution = Solution()
    nums = [4, 1, -1, 2, -1, 2, 1]
    k = 3
    expected = [1, -1, 2]
    result = solution.topKFrequent(nums, k)
    assert set(result) == set(expected)
    assert len(result) == k

def test_negative_numbers():
    """Tests handling of negative numbers."""
    solution = Solution()
    nums = [-1, -1, -2, -2, -2, 0]
    k = 2
    expected = [-2, -1]
    result = solution.topKFrequent(nums, k)
    assert set(result) == set(expected)
    assert len(result) == k

def test_empty_input_list():
    """Tests the behavior with an empty input list."""
    solution = Solution()
    nums = []
    k = 1
    expected = []
    result = solution.topKFrequent(nums, k)
    assert set(result) == set(expected)
    assert len(result) == 0

def test_single_element_list():
    """Tests a list with only one element."""
    solution = Solution()
    nums = [5]
    k = 1
    expected = [5]
    result = solution.topKFrequent(nums, k)
    assert set(result) == set(expected)
    assert len(result) == k

def test_all_elements_same():
    """Tests when all elements in the list are identical."""
    solution = Solution()
    nums = [7, 7, 7, 7]
    k = 1
    expected = [7]
    result = solution.topKFrequent(nums, k)
    assert set(result) == set(expected)
    assert len(result) == k
