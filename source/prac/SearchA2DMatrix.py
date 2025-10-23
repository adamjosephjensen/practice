from typing import List

class _2025_10_23_Solution:
    def get(self, matrix: List[List[int]], index: int) -> int:
        """
        use a linear index to get a value from the 2d matrix
        scratch:
        0,1,2,3
        4,5,6,7

        index 5:
        row = 5 // 4 = 1
        col = 5 % 4 = 1
        """
        n_cols = len(matrix[0]) 
        row = index // n_cols
        col = index % n_cols
        return matrix[row][col]


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        goal: just run binary search ignoring the matrix
        use the get method to get the value
        """
        lo = 0
        hi = len(matrix) * len(matrix[0]) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            guess = self.get(matrix, mid)
            if guess == target:
                return True
            if guess < target: # guess too low, increase guess by increasing lo
                lo = mid + 1
            else: # guess too high, decrease guess by decreasing hi
                hi = mid - 1
        return False

Solution = _2025_10_23_Solution
