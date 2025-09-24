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

class _2025_09_24_Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list
        _numbers = sorted(nums)
        n = len(nums)
        triplets = []
        # loop over all numbers
        #print(f" The list is: {_numbers}")
        for i in range(n - 2):
            # fix i (lowest)
            # skip duplicates for i
            if i > 0 and _numbers[i] == _numbers[i-1]:
                continue
        
            # initialize j equal to the next highest, and k equal to the highest
            j = i + 1
            k = n - 1
            while j < k:
                #print(f"i: {i}, j: {j}, k: {k}")
                #print(f"i_val: {_numbers[i]}, j_val: {_numbers[j]}, k_val: {_numbers[k]}")
                _sum = _numbers[i] + _numbers[j] + _numbers[k]
                #print(f"The sum is: {_sum}")
                # if _sum is negative, then increase j bc _sum needs to go up towards 0
                if _sum < 0:
                    j += 1
                    while j < k and _numbers[j] == _numbers[j-1]:
                        j += 1
                # if _sum is positive, then decrease k bc _sum needs to go down towards 0
                elif 0 < _sum:
                    k -= 1
                    while j < k and _numbers[k] == _numbers[k+1]:
                        k -= 1
                # if _sum is zero, this is a triplet, so add it then increase j and decrease k
                elif 0 == _sum:
                    triplets.append([_numbers[i],_numbers[j],_numbers[k]])
                    j += 1
                    while j < k and _numbers[j] == _numbers[j-1]:
                        j += 1
                    k -= 1
                    while j < k and _numbers[k] == _numbers[k+1]:
                        k -= 1
                else:
                    assert 0, "impossible"
        return triplets

class _2025_09_10_Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
		# ThreeSum is a two-pointer problem
        # algorithm: first sort array
        # then fix the minimum value and do a two-pointer search the mid, hi val to find a sum
        # be careful about duplicates
        nums.sort()
        n = len(nums)
        triplets = []
        for low_idx in range(n - 2):
            mid_idx = low_idx+1
            hi_idx = n-1
            # handle duplicate values of low_id
            if 0 < low_idx and nums[low_idx] == nums[low_idx-1]:
                continue

            while mid_idx < hi_idx:
                # evaluate the sum
                triplet = [nums[low_idx], nums[mid_idx], nums[hi_idx]]
                total = sum(triplet)
                # if spot on, add ascending triplet to results list, advance ptrs
                if total == 0:
                    triplets.append(triplet)
                    # increment mid_idx; skip duplicates
                    mid_idx += 1
                    while mid_idx < hi_idx and nums[mid_idx] == nums[mid_idx - 1]:
                        mid_idx +=1

                    # decrement hi_idx while skipping duplicates
                    hi_idx -= 1
                    while mid_idx < hi_idx and nums[hi_idx] == nums[hi_idx + 1]:
                        hi_idx -= 1

                # if too low, increment the mid_idx
                elif(total < 0):
                    mid_idx += 1
                    while mid_idx < hi_idx and nums[mid_idx] == nums[mid_idx - 1]:
                        mid_idx +=1
                # if too high, decrement the hi_idx
                elif(0 < total):
                    hi_idx -= 1
                    while mid_idx < hi_idx and nums[hi_idx] == nums[hi_idx + 1]:
                        hi_idx -= 1
                else:
                    assert 0, "should be impossible"

        return triplets


class Old_Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for lo in range(len(nums)-2):
            if lo > 0 and nums[lo] == nums[lo - 1]:  # skip duplicates after nums[0]
                continue
            # want -num[c] = num[l] + num[r], where num[l] <= num[r] if l < r
            mid = lo + 1 # mid starts in the middle
            hi = len(nums) - 1 # hi starts at last index
            while mid < hi: # increase mid if value is too low, decrease hi if value is too high
                total = nums[lo] + nums[mid] + nums[hi]
                if total == 0:
                    triplets.append([nums[lo], nums[mid], nums[hi]])
                    mid += 1
                    hi -= 1
                    while mid < hi and nums[mid] == nums[mid-1]: # while not complete, skip dupllicates
                        mid += 1
                    while mid < hi and nums[hi] == nums[hi+1]: # while not complete, skip duplicates
                        hi -= 1
                elif total < 0:
                    mid += 1
                else:
                    hi -= 1
                # maintain invariant: lo < mid < hi
                assert lo+1 <= mid <= hi+1, "bad pointer move"

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

Solution = _2025_09_24_Solution
