import pytest

# 1 way to climb 1 or 0 stairs
## 2 ways to climb 2 stairs (1+1, 2)
### 3 ways to climb 3 steps (1+1+1, 2+1, 1+2)
#### 3 + 2 = 5 ways to climb 4 steps
##### 5+3 = 8 ways to climb 5 steps
######

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculates the number of distinct ways to climb to the top of n stairs,
        taking either 1 or 2 steps at a time. Uses memoization for efficiency.
        """
        # Use a fresh memo dictionary for each call to climbStairs
        memo = {}
        def climb(n, memo):
            if n <= 1: return 1
            if n in memo: return memo[n]
            memo[n] = climb(n-1, memo) + climb(n-2, memo)
            return memo[n]
        return climb(n, memo)

# --- Test Cases ---

def test_zero_stairs():
    """Tests the case with 0 stairs."""
    solution = Solution()
    assert solution.climbStairs(0) == 1

def test_one_stair():
    """Tests the case with 1 stair."""
    solution = Solution()
    assert solution.climbStairs(1) == 1

def test_two_stairs():
    """Tests the case with 2 stairs."""
    solution = Solution()
    assert solution.climbStairs(2) == 2

def test_four_stairs():
    """Tests the case with 4 stairs."""
    solution = Solution()
    assert solution.climbStairs(4) == 5

def test_thirty_stairs():
    """Tests the case with 30 stairs."""
    solution = Solution()
    # The expected value for 30 stairs is the 31st Fibonacci number (starting F0=1, F1=1)
    # F(30) = 1346269
    assert solution.climbStairs(30) == 1346269
