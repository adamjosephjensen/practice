from typing import List
from heapq import nlargest, heapify, heappop, heappush
# Note: No unittest import needed for pytest style tests


class KthLargest:
    """
    Design a class to find the kth largest integer in a stream of values,
    including duplicates.
    """
    def __init__(self, k: int, nums: List[int]):
        """
        Initializes the object given an integer k and the stream of integers nums.
        """
        self.k = k
        self.h = nlargest(self.k, nums)
        heapify(self.h)

    def add(self, val: int) -> int:
        """
        Adds the integer val to the stream and returns the kth largest integer
        in the stream.
        """
        # case 1: heap size is less than k
        if len(self.h) < self.k:
            heappush(self.h, val)
        elif val > self.h[0]: # case: heap is already of size k, need to pop
            heappop(self.h) # discard previous kth largest
            heappush(self.h, val)

        return self.h[0] # always return kth_largest

# --- Pytest Tests ---

def test_example_from_prompt():
    """
    Tests the example scenario provided in the problem description.
    E.g. the 2nd largest from [1, 2, 3, 3] is 3.
    """
    k = 2
    nums = [1, 2, 3, 3]
    kth_largest = KthLargest(k, nums)
    # After init with [1, 2, 3, 3], the 2nd largest is 3.
    # The internal state should reflect this, though the constructor doesn't return.
    # Let's test the add method as per typical problem constraints.
    # If we add 4, stream is [1, 2, 3, 3, 4], 2nd largest is 3.
    assert kth_largest.add(4) == 3, "Test Case: Add 4"
    # If we add 3, stream is [1, 2, 3, 3, 4, 3], 2nd largest is 3.
    assert kth_largest.add(3) == 3, "Test Case: Add 3"
    # If we add 5, stream is [1, 2, 3, 3, 4, 3, 5], 2nd largest is 4.
    assert kth_largest.add(5) == 4, "Test Case: Add 5"


def test_standard_case():
    """
    Tests a standard sequence of operations.
    """
    k = 3
    nums = [4, 5, 8, 2]
    kth_largest = KthLargest(k, nums)
    # Initial stream [4, 5, 8, 2]. Sorted: [2, 4, 5, 8]. 3rd largest is 4.
    assert kth_largest.add(3) == 4, "Test Case 1: Add 3" # Stream [4, 5, 8, 2, 3]. Sorted: [2, 3, 4, 5, 8]. 3rd largest is 4.
    assert kth_largest.add(5) == 5, "Test Case 2: Add 5" # Stream [4, 5, 8, 2, 3, 5]. Sorted: [2, 3, 4, 5, 5, 8]. 3rd largest is 5.
    assert kth_largest.add(10) == 5, "Test Case 3: Add 10" # Stream [4, 5, 8, 2, 3, 5, 10]. Sorted: [2, 3, 4, 5, 5, 8, 10]. 3rd largest is 5.
    assert kth_largest.add(9) == 8, "Test Case 4: Add 9" # Stream [4, 5, 8, 2, 3, 5, 10, 9]. Sorted: [2, 3, 4, 5, 5, 8, 9, 10]. 3rd largest is 8.
    assert kth_largest.add(4) == 8, "Test Case 5: Add 4" # Stream [4, 5, 8, 2, 3, 5, 10, 9, 4]. Sorted: [2, 3, 4, 4, 5, 5, 8, 9, 10]. 3rd largest is 8.

def test_k_is_one():
    """
    Tests when k=1 (finding the largest element).
    """
    k = 1
    nums = [0]
    kth_largest = KthLargest(k, nums)
    assert kth_largest.add(-1) == 0, "Test Case k=1: Add -1" # Stream [0, -1]. Largest is 0.
    assert kth_largest.add(1) == 1, "Test Case k=1: Add 1"  # Stream [0, -1, 1]. Largest is 1.
    assert kth_largest.add(-2) == 1, "Test Case k=1: Add -2" # Stream [0, -1, 1, -2]. Largest is 1.
    assert kth_largest.add(3) == 3, "Test Case k=1: Add 3"  # Stream [0, -1, 1, -2, 3]. Largest is 3.

def test_initial_list_smaller_than_k():
    """
    Tests behavior when the initial list has fewer than k elements.
    The add method should still work correctly as elements are added.
    """
    k = 3
    nums = [1, 1]
    kth_largest = KthLargest(k, nums)
    # Stream [1, 1]. Not enough elements for 3rd largest yet.
    # The behavior here depends on implementation if add is called before k elements exist.
    # Let's assume add returns the kth largest *once k elements are available*.
    # Add 1: Stream [1, 1, 1]. 3rd largest is 1.
    assert kth_largest.add(1) == 1, "Test Case Small Init 1: Add 1"
    # Add 2: Stream [1, 1, 1, 2]. 3rd largest is 1.
    assert kth_largest.add(2) == 1, "Test Case Small Init 2: Add 2"
    # Add 5: Stream [1, 1, 1, 2, 5]. 3rd largest is 1.
    assert kth_largest.add(5) == 1, "Test Case Small Init 3: Add 5"
    # Add 0: Stream [1, 1, 1, 2, 5, 0]. 3rd largest is 1.
    assert kth_largest.add(0) == 1, "Test Case Small Init 4: Add 0"

# Note: The if __name__ == "__main__": block is removed as pytest handles test execution.
