from typing import List
from heapq import nlargest, heapify, heappop, heappush, heappushpop
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
        self.heap = nlargest(self.k, nums)
        heapify(self.heap)

    def add(self, val: int) -> int:
        """
        Adds the integer val to the stream and returns the kth largest integer
        in the stream.
        """
        # case 1: heap size is less than k
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        elif val > self.heap[0]: # case: heap is already of size k, need to pop
            heappushpop(self.heap, val)

        return self.heap[0] # always return kth_largest

