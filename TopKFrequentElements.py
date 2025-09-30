# Top K Frequent Elements
# Solved 
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Import necessary types
from typing import List, Dict
from collections import defaultdict

class _2025_09_30_Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given nums and k, return k most frequent from nums, in any order
        Lower bound: O(n) to count the frequency for each element
        Brute force: count the frequency using a dictionary (defaultdict(int)),
        sort the frequencies, return the top K, complexity: (O) n * log(n).
        Insight: we don't need to sort because the return order doesn't matter
        and the frequencies are bounded (the max frequency is len(nums)).
        So we can use half of Bucket Sort with len(nums) buckets, but without sorting
        the buckets to retain O(n) runtime.
        """
        val_to_freq = defaultdict(int)
        for val in nums:
            val_to_freq[val] +=1
        
        # create empty buckets (max n)
        freq_to_val: List[List[int]] = [[] for _ in range(len(nums) + 1)]
        # for all buckets
        for val, freq in val_to_freq.items():
            # add val to the appropriate frequency bucket
            freq_to_val[freq].append(val)
        
        top_k: List[int] = []
        # in order of decreasing frequency, build the return list
        for freq in range(len(nums), 0, -1):
            if freq_to_val[freq]: # [] is false
                top_k.extend(freq_to_val[freq]) # put the whole bucket on the list
        
        return top_k[:k]
    

class OldSolution:
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

Solution = _2025_09_30_Solution

