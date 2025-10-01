import pytest
from prac.ContainerWithTheMostWater import Solution

solution = Solution()

def test_example_1():
    heights = [1,7,2,5,4,7,3,6]
    ans = solution.maxArea(heights)
    assert ans == 36

def test_example_2():
    heights = [2,2,2]
    ans = solution.maxArea(heights)
    assert ans == 4
