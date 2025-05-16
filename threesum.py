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
