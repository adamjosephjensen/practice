# Top K Frequent Elements
# Solved 
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Import necessary types
from typing import List, Dict
import pytest # Used by the test runner

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create mapping from num to frequency
        counts: Dict[int, int] = dict()
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        # create 1 dimensional lookup from frequency, to the numbers
        # The maximum frequency can be len(nums)
        freq_to_nums: List[List[int]] = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            freq_to_nums[freq].append(num)

        # scan lookup list from the right (highest frequency)
        k_frequent: List[int] = []
        # Iterate from max possible frequency down to 1
        for freq in range(len(nums), 0, -1):
            # Check if any numbers had this frequency
            if freq_to_nums[freq]:
                # Add all numbers with this frequency
                # Using extend is slightly more efficient than a loop with append
                k_frequent.extend(freq_to_nums[freq])
            # Stop once we have found k elements
            if len(k_frequent) >= k:
                # Since the problem guarantees a unique answer set for the top k,
                # we don't need to worry about ties exactly at the k boundary.
                # We might collect slightly more than k if multiple numbers share
                # the k-th highest frequency, but the problem implies this won't
                # lead to ambiguity for the *set* of top k elements.
                # However, to return exactly k elements:
                return k_frequent[:k]
        # Return the collected elements, slicing to k if necessary (e.g., if nums was empty or k > len(unique_nums))
        return k_frequent[:k]

# --- Test Cases using pytest ---

def test_example_case():
    """Tests the example provided in many problem descriptions."""
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    expected = [1, 2] # Freqs: 1 (3), 2 (2), 3 (1). Top 2 are 1 and 2.
    result = solution.topKFrequent(nums, k)
    # Use set comparison because the order doesn't matter
    assert set(result) == set(expected)
    assert len(result) == k

def test_k_equals_one():
    """Tests finding the single most frequent element."""
    solution = Solution()
    nums = [1, 2, 2, 3, 3, 3, 4]
    k = 1
    expected = [3] # 3 is the most frequent (freq 3)
    result = solution.topKFrequent(nums, k)
    assert set(result) == set(expected)
    assert len(result) == k

def test_k_equals_unique_elements():
    """Tests when k is the total number of unique elements."""
    solution = Solution()
    nums = [1, 1, 2, 3, 3, 3]
    k = 3 # Number of unique elements
    expected = [3, 1, 2] # Freqs: 3 (3), 1 (2), 2 (1). Top 3 are 3, 1, 2.
    result = solution.topKFrequent(nums, k)
    assert set(result) == set(expected)
    assert len(result) == k

def test_tie_in_frequency_within_top_k():
    """Tests when multiple numbers share the same frequency within the top k."""
    solution = Solution()
    # Freqs: 4(1), 1(2), -1(2), 2(2), 3(1). Top 3 freqs are 2, 2, 2.
    nums = [4, 1, -1, 2, -1, 2, 1]
    k = 3
    expected = [1, -1, 2] # All have frequency 2
    result = solution.topKFrequent(nums, k)
    assert set(result) == set(expected)
    assert len(result) == k

def test_negative_numbers():
    """Tests handling of negative numbers."""
    solution = Solution()
    nums = [-1, -1, -2, -2, -2, 0] # Freqs: -2(3), -1(2), 0(1)
    k = 2
    expected = [-2, -1]
    result = solution.topKFrequent(nums, k)
    assert set(result) == set(expected)
    assert len(result) == k

def test_empty_input_list():
    """Tests the behavior with an empty input list."""
    solution = Solution()
    nums = []
    k = 1 # k can be anything here, result should be empty
    expected = []
    result = solution.topKFrequent(nums, k)
    assert set(result) == set(expected) # Should be []
    assert len(result) == 0 # Specifically check length is 0

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

# To run these tests, save the file (e.g., TopKFrequentElements.py)
# and run `pytest TopKFrequentElements.py` in your terminal.

