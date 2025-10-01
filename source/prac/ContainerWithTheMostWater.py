from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Step one: make sure I understand how to compute the "water"
        All heights are 1 unit apart
        The "heights" are infinitely thin, making the area the area height * width
        where width is the number of indices between the bars
        and the height is the minimum of the two bars that are collecting the water

        Brute force: try every height with every other height, pick the maximum one O(n*n)
        """
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            this_area = (r-l) * min(heights[l], heights[r])
            max_area = max(this_area, max_area)
            # trick for incrementing l or decrementing r
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area

