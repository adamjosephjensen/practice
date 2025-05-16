# Top K Frequent Elements
# Solved 
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Import necessary types
from typing import List, Dict

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

