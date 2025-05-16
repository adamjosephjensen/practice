import pytest # Add pytest import
from typing import List # Ensure List is imported if needed by tests
from kth_largest import KthLargest

# --- Pytest Tests ---

def test_example_from_prompt():
    """
    Tests the example scenario provided in the problem description.
    E.g. the 2nd largest from [1, 2, 3, 3] is 3.
    """
    k = 2
    nums = [1, 2, 3, 3]
    kth_largest_obj = KthLargest(k, nums)
    assert kth_largest_obj.add(4) == 3, "Test Case: Add 4"
    assert kth_largest_obj.add(3) == 3, "Test Case: Add 3"
    assert kth_largest_obj.add(5) == 4, "Test Case: Add 5"


def test_standard_case():
    """
    Tests a standard sequence of operations.
    """
    k = 3
    nums = [4, 5, 8, 2]
    kth_largest_obj = KthLargest(k, nums)
    assert kth_largest_obj.add(3) == 4, "Test Case 1: Add 3"
    assert kth_largest_obj.add(5) == 5, "Test Case 2: Add 5"
    assert kth_largest_obj.add(10) == 5, "Test Case 3: Add 10"
    assert kth_largest_obj.add(9) == 8, "Test Case 4: Add 9"
    assert kth_largest_obj.add(4) == 8, "Test Case 5: Add 4"

def test_k_is_one():
    """
    Tests when k=1 (finding the largest element).
    """
    k = 1
    nums = [0]
    kth_largest_obj = KthLargest(k, nums)
    assert kth_largest_obj.add(-1) == 0, "Test Case k=1: Add -1"
    assert kth_largest_obj.add(1) == 1, "Test Case k=1: Add 1"
    assert kth_largest_obj.add(-2) == 1, "Test Case k=1: Add -2"
    assert kth_largest_obj.add(3) == 3, "Test Case k=1: Add 3"

def test_initial_list_smaller_than_k():
    """
    Tests behavior when the initial list has fewer than k elements.
    """
    k = 3
    nums = [1, 1]
    kth_largest_obj = KthLargest(k, nums)
    assert kth_largest_obj.add(1) == 1, "Test Case Small Init 1: Add 1"
    assert kth_largest_obj.add(2) == 1, "Test Case Small Init 2: Add 2"
    assert kth_largest_obj.add(5) == 1, "Test Case Small Init 3: Add 5"
    assert kth_largest_obj.add(0) == 1, "Test Case Small Init 4: Add 0"
