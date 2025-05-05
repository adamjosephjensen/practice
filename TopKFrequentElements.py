# Top K Frequent Elements
# Solved 
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        # from -1000 to 1000
        # create mapping from num to frequency
        counts = dict()
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
    
        # create 1 dimensional lookup from frequency, to the numbers
        freq_to_nums = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            freq_to_nums[freq].append(num)

        # scan lookup list from the right. learned range(...) takes start, end, step:
        k_frequent = []
        for freq in range(len(nums), 0, -1):
            for num in freq_to_nums[r]:
                k_frequent.append(num)
            if len(k_frequent) == k:
                break
        return k_frequent


