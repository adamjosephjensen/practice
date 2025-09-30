import pytest
from prac.ClimbStairs import Solution

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
