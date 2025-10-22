# source/prac/DailyTemperatures.py
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        You are given an array of integers temperatures where temperatures[i]
        represents the daily temperatures on the ith day.

        Return an array result where result[i] is the number of days after the ith day
        before a warmer temperature appears on a future day.
        If there is no day in the future where a warmer temperature will appear
        for the ith day, set result[i] to 0 instead.
        
        Brute force: for every temp, look forward in the array at each element until
        you find a bigger element. O(n^2)

        """
        n = len(temperatures)
        res = [0] * n
        stack: List[tuple[int,int]] = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res
