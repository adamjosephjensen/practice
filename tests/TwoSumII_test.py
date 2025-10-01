import pytest
from typing import List
from prac.TwoSumII import Solution


def _check_pair(numbers, target, ans):
    # 1 indexed, strictly increasing
    assert isinstance(ans, list)
    assert len(ans) == 2
    i, j = ans
    assert 1 <= i < j <= len(numbers)
    assert numbers[i-1] + numbers[j-1] == target

@pytest.fixture
def sol():
    return Solution()

@pytest.mark.parametrize(
        "numbers,target,expected_exact",
     [
        # unique-solution cases → check exact indices
        ([1, 2], 3, [1, 2]),                        # minimal length
        ([2, 7, 11, 15], 9, [1, 2]),                # simple, move right ptr
        ([2, 7, 11, 15], 26, [3, 4]),               # simple, move left ptr
        ([-5, -2, -2, 0, 2, 4, 6], 1, [1, 7]),      # negatives + positives
        ([1, 2, 3, 4, 9], 10, [1, 5]),              # extremes pair
        ([1,2,3,4],3,[1,2]),                        # from example
        ([1_000_000, 2_000_000, 3_000_000, 5_000_000], 5_000_000, [2, 3]),  # large ints
    ],
)       
def test_exact_unique_cases(sol, numbers, target, expected_exact):
    ans = sol.twoSum(numbers, target)
    assert ans == expected_exact
    _check_pair(numbers, target, ans)

def test_no_solution_raises(sol):
    """
    must assert if there is no solution
    """
    numbers, target = [1,2,3], 7
    with pytest.raises(AssertionError):
        sol.twoSum(numbers, target)
