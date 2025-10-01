import pytest
from prac.LongestSubstringWithoutRepeatingCharacters import Solution

solution = Solution()

def test_example_1():
    input = "zxyzxyz"
    ans = solution.lengthOfLongestSubstring(input)
    assert ans == 3

def test_example_2():
    input = "xxx"
    ans = solution.lengthOfLongestSubstring(input)
    assert ans == 1
